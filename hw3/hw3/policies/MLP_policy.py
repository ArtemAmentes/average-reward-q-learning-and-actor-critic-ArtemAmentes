import abc
import itertools

import numpy as np
import torch
from torch import nn, optim
from torch import distributions

from hw3.infrastructure import pytorch_util as ptu
from hw3.policies.base_policy import BasePolicy


class MLPPolicy(BasePolicy, nn.Module, metaclass=abc.ABCMeta):

    def __init__(self,
                 ac_dim,
                 ob_dim,
                 n_layers,
                 size,
                 discrete=False,
                 learning_rate=1e-4,
                 training=True,
                 nn_baseline=False,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        # init vars
        self.ac_dim = ac_dim
        self.ob_dim = ob_dim
        self.n_layers = n_layers
        self.discrete = discrete
        self.size = size
        self.learning_rate = learning_rate
        self.training = training
        self.nn_baseline = nn_baseline

        if self.discrete:
            self.logits_na = ptu.build_mlp(input_size=self.ob_dim,
                                           output_size=self.ac_dim,
                                           n_layers=self.n_layers,
                                           size=self.size)
            self.logits_na.to(ptu.device)
            self.mean_net = None
            self.logstd = None
            self.optimizer = optim.Adam(self.logits_na.parameters(),
                                        self.learning_rate)
        else:
            self.logits_na = None
            self.mean_net = ptu.build_mlp(input_size=self.ob_dim,
                                          output_size=self.ac_dim,
                                          n_layers=self.n_layers, size=self.size)
            self.logstd = nn.Parameter(
                torch.zeros(self.ac_dim, dtype=torch.float32, device=ptu.device)
            )
            self.mean_net.to(ptu.device)
            self.logstd.to(ptu.device)
            self.optimizer = optim.Adam(
                itertools.chain([self.logstd], self.mean_net.parameters()),
                self.learning_rate
            )

        if nn_baseline:
            self.baseline = ptu.build_mlp(
                input_size=self.ob_dim,
                output_size=1,
                n_layers=self.n_layers,
                size=self.size,
            )
            self.baseline.to(ptu.device)
            self.baseline_optimizer = optim.Adam(
                self.baseline.parameters(),
                self.learning_rate,
            )
        else:
            self.baseline = None

    ##################################

    def save(self, filepath):
        torch.save(self.state_dict(), filepath)

    ##################################

    # query the policy with observation(s) to get selected action(s)
    def get_action(self, obs: np.ndarray) -> np.ndarray:
        if len(obs.shape) > 1:
            observation = obs
        else:
            observation = obs[None]

        if self.discrete:
            action = self(ptu.from_numpy(observation)).sample()
        else:
            action = self(ptu.from_numpy(observation)).rsample()

        return ptu.to_numpy(action)

    # update/train this policy
    def update(self, observations, actions, **kwargs):
        raise NotImplementedError

    # This function defines the forward pass of the network.
    # You can return anything you want, but you should be able to differentiate
    # through it. For example, you can return a torch.FloatTensor. You can also
    # return more flexible objects, such as a
    # `torch.distributions.Distribution` object. It's up to you!
    def forward(self, observation: torch.FloatTensor):
        if self.discrete:
            action_distribution = distributions.Categorical(logits=self.logits_na(observation))
        else:
            mean = self.mean_net(observation)
            scale_tril = torch.diag(torch.exp(self.logstd))
            batch_dim = mean.shape[0]
            batch_scale_tril = scale_tril.repeat(batch_dim, 1, 1)
            action_distribution = distributions.MultivariateNormal(loc=mean, scale_tril=batch_scale_tril)

        return action_distribution


#####################################################
#####################################################


class MLPPolicyAC(MLPPolicy):
    def update(self, observations, actions, adv_n=None):
        observations = ptu.from_numpy(observations)
        actions = ptu.from_numpy(actions)
        advantages = ptu.from_numpy(adv_n)

        log_probs = self(observations).log_prob(actions)
        loss = -1 * torch.sum(log_probs * advantages)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()
