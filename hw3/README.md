# Setup

You can run this code on your own machine or on Google Colab. 

1. **Local option:** If you choose to run locally, you will need to install MuJoCo and some Python packages; see HW3 [installation.md](installation.md).

2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badges below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pkuderov/mipt-rl-hw-2022/blob/main/hw3/hw3/scripts/run_hw3_dqn.ipynb) **Part I (Q-learning)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pkuderov/mipt-rl-hw-2022/blob/main/hw3/hw3/scripts/run_hw3_actor_critic.ipynb)  **Part II (Actor-critic)**

## Complete the code

The following files have blanks to be filled with your solutions from homework 1. The relevant sections are marked with `TODO: get this from hw1 or hw2`.

- [infrastructure/rl_trainer.py](hw3/infrastructure/rl_trainer.py)
- [infrastructure/utils.py](hw3/infrastructure/utils.py)
- [policies/MLP_policy.py](hw3/policies/MLP_policy.py)

You will then need to implement new routines in the following files for homework 3 part 1 (Q-learning):

- [agents/dqn_agent.py](hw3/agents/dqn_agent.py)
- [critics/dqn_critic.py](hw3/critics/dqn_critic.py)
- [policies/argmax_policy.py](hw3/policies/argmax_policy.py)

and in the following files for part 2 (actor-critic):

- [agents/ac_agent.py](hw3/agents/ac_agent.py)
- [critics/bootstrapped_continuous_critic.py](hw3/critics/bootstrapped_continuous_critic.py)
- [policies/MLP_policy.py](hw3/policies/MLP_policy.py)

The relevant sections are marked with `TODO`.

You may also want to look through [scripts/run_hw3_dqn.py](hw3/scripts/run_hw3_dqn.py) and [scripts/run_hw3_actor_critic.py](hw3/scripts/run_hw3_actor_critic.py) (if running locally) or [scripts/run_hw3_dqn.ipynb](hw3/scripts/run_hw3_dqn.ipynb) and [scripts/run_hw3_actor_critic.ipynb](hw3/scripts/run_hw3_actor_critic.ipynb) (if running on Colab), though you will not need to edit this files beyond changing runtime arguments in the Colab notebook.

See the [assignment PDF](assignment.pdf) for more details on what files to edit.

## Experiments

### Experiment 1. Base Q-learning

Run the following command:

```bash
python hw3/scripts/run_hw3_dqn.py --env_name MsPacman-v0 --exp_name q1
```

### Experiment 2. DQN vs DDQN

Run the following commands:

```bash
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_1 --seed 1
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_2 --seed 2
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_3 --seed 3

python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_1 -- double_q --seed 1
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_2 -- double_q --seed 2
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_3 -- double_q --seed 3
```

### Experiment 3. DQN hyperparameters

Compare different hyperparameters setups with the following commands:

```bash
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam1
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam2
python hw3/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam3
```

### Experiment 4. Sanity check with CartPole

Check that your solution works with the following command:

```bash
python hw3/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_ac_1_1 -ntu 1 -ngsptu 1
```

In the example above, as we alternate between performing one target update and one gradient update step for the critic, this probably doesn’t work, and you need to increase both the number of target updates and number of gradient updates.

Compare the results for the following settings and report which worked best:

```bash
python hw3/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_100_1 -ntu 100 -ngsptu 1

python hw3/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_1_100 -ntu 1 -ngsptu 100

python hw3/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_10_10 -ntu 10 -ngsptu 10
```

At the end, the best setting from above should match the policy gradient results from Cartpole in hw2 (200).

### Experiment 5. Run actor-critic with more difficult tasks

Use the best setting from the previous experiment to run InvertedPendulum

```bash
python hw3/scripts/run_hw3_actor_critic.py --env_name InvertedPendulum-v2 --ep_len 1000 --discount 0.95 -n 100 -l 2 -s 64 -b 5000 -lr 0.01 --exp_name q5_<ntu?>_<ngsptu?> -ntu <ntu?> -ngsptu <ngsptu?>
```

and HalfCheetah

```bash
python hw3/scripts/run_hw3_actor_critic.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.90 --scalar_log_freq 1 -n 150 -l 2 -s 32 -b 30000 -eb 1500 -lr 0.02 --exp_name q5_<ntu?>_<ngsptu?> -ntu <ntu?> -ngsptu <ngsptu?>
```

, where `<ntu?>` and `<ngsptu?>` is replaced with the parameters you chose in previous task.

Your results should roughly match those of policy gradient. After 150 iterations, your HalfCheetah return should be around 150. After 100 iterations, your InvertedPendulum return should be around 1000.
