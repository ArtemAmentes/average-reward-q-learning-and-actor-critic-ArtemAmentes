# Setup

You can run this code on your own machine or on Google Colab.

1. **Local option:** If you choose to run locally, you will need to install MuJoCo and some Python packages; see HW2 [installation.md](installation.md). If you completed the installation for homework 1 before, you will find only small additional installation step.
2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badge below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pkuderov/mipt-rl-hw-2022/blob/main/hw2/hw2/scripts/run_hw2.ipynb)

## Complete the code

The following files have blanks to be filled with your solutions from homework 1. The relevant sections are marked with "TODO: get this from hw1".

- [infrastructure/rl_trainer.py](hw2/infrastructure/rl_trainer.py)
- [infrastructure/utils.py](hw2/infrastructure/utils.py)
- [policies/MLP_policy.py](hw2/policies/MLP_policy.py)

You will then need to complete the following new files for homework 2. The relevant sections are marked with "TODO".

- [agents/pg_agent.py](hw2/agents/pg_agent.py)
- [policies/MLP_policy.py](hw2/policies/MLP_policy)

You will also want to look through [scripts/run_hw2.py](hw2/scripts/run_hw2.py) (if running locally) or [scripts/run_hw2.ipynb](hw2/scripts/run_hw2.ipynb) (if running on Colab), though you will not need to edit this files beyond changing runtime arguments in the Colab notebook.

You will be running your policy gradients implementation in five experiments total, investigating the effects of design decisions like reward-to-go estimators, neural network baselines and generalized advantage estimation for variance reduction, and advantage normalization. See the [assignment PDF](cs285_hw2.pdf) for more details. Commands to run the experiments are presented below.

## Experiments

### Experiment 1: CartPole

Run the following commands:

```bash
python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 1000 \
    -dsa --exp_name q1_sb_no_rtg_dsa

python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 1000 \
    -rtg -dsa --exp_name q1_sb_rtg_dsa

python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 1000 \
    -rtg --exp_name q1_sb_rtg_na

python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 5000 \
    -dsa --exp_name q1_lb_no_rtg_dsa

python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 5000 \
    -rtg -dsa --exp_name q1_lb_rtg_dsa

python scripts/run_hw2.py \
    --env_name CartPole-v0 -n 100 -b 5000 \
    -rtg --exp_name q1_lb_rtg_na
```

What’s happening here:

- `-n` : Number of iterations.
- `-b` : Batch size (number of state-action pairs sampled while acting according to the current policy at each iteration).
- `-dsa` : Flag: if present, sets standardize_advantages to False. Otherwise, by default, standardizes
advantages to have a mean of zero and standard deviation of one.
- `-rtg` : Flag: if present, sets `reward_to_go=True`. Otherwise, `reward_to_go=False` by default.
- `--exp_name` : Name for experiment, which goes into the name for the data logging directory.

Various other command line arguments will allow you to set batch size, learning rate, network architecture, and more. You can change these as well, but keep them fixed between the 6 experiments mentioned above.

### Experiment 2: InvertedPendulum

Use this command template:

```bash
python scripts/run_hw2.py \
    --env_name InvertedPendulum-v2 \
    --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 \
    -b <b*> -lr <r*> -rtg \
    --exp_name q2_b<b*>_r<r*>
```

to test different batch size `b*` and learning rate `r*`. Your task is to find the smallest `b*` and largest `r*` that gets to optimum
(maximum score of 1000) in less than 100 iterations.

### Experiment 3: LunarLander

Run the following command:

```bash
python scripts/run_hw2.py \
    --env_name LunarLanderContinuous-v2 --ep_len 1000 \
    --discount 0.99 -n 100 -l 2 -s 64 -b 40000 -lr 0.005 \
    --reward_to_go --nn_baseline --exp_name q3_b40000_r0.005
```

### Experiment 4: HalfCheetah

Search over batch sizes b ∈ [10000, 30000, 50000] and learning rates r ∈ [0.005, 0.01, 0.02] to replace `<b>` and `<r>` below

```bash
python scripts/run_hw2.py \
    --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 \
    -b <b> -lr <r> -rtg --nn_baseline \
    --exp_name q4_search_b<b>_lr<r>_rtg_nnbaseline
```

Once you’ve found optimal values `b*` and `r*`, use them to run the following commands (replace the terms in angle brackets):

```bash
python scripts/run_hw2.py \
    --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 \
    -b <b*> -lr <r*> \
    --exp_name q4_b<b*>_r<r*>

python scripts/run_hw2.py \
    --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 \
    -b <b*> -lr <r*> -rtg \
    --exp_name q4_b<b*>_r<r*>_rtg

python scripts/run_hw2.py \
    --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 \
    -b <b*> -lr <r*> --nn_baseline \
    --exp_name q4_b<b*>_r<r*>_nnbaseline

python scripts/run_hw2.py \
    --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 \
    -b <b*> -lr <r*> -rtg --nn_baseline \
    --exp_name q4_b<b*>_r<r*>_rtg_nnbaseline
```

### Experiment 5: Hopper

Search over λ ∈ [0, 0.95, 0.99, 1] to replace `<λ>` below. *Please, do not change any of the other hyperparameters (e.g. batch size,
learning rate)!*

```bash
python scripts/run_hw2.py \
    --env_name Hopper-v2 --ep_len 1000
    --discount 0.99 -n 300 -l 2 -s 32 -b 2000 -lr 0.001 \
    --reward_to_go --nn_baseline \
    --action_noise_std 0.5 --gae_lambda <λ> \
    --exp_name q5_b2000_r0.001_lambda<λ>
```

## Credits

This homework is based on [Berkeley CS285 Deep RL Course HW2](https://github.com/berkeleydeeprlcourse/homework_fall2021/tree/main/hw2).
