# Setup

You can run this code on your own machine or on Google Colab.

1. **Local option:** If you choose to run locally, you will need to install MuJoCo and some Python packages; see [installation.md](installation.md) for instructions.
2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badge below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pkuderov/mipt-rl-hw-2022/blob/main/hw1/cds_rl/scripts/run_hw1.ipynb)

## Complete the code

Fill in sections marked with `TODO`. In particular, see

- [infrastructure/rl_trainer.py](cds_rl/infrastructure/rl_trainer.py)
- [policies/MLP_policy.py](cds_rl/policies/MLP_policy.py)
- [infrastructure/replay_buffer.py](cds_rl/infrastructure/replay_buffer.py)
- [infrastructure/utils.py](cds_rl/infrastructure/utils.py)
- [infrastructure/pytorch_util.py](cds_rl/infrastructure/pytorch_util.py).

Look for the sections marked with `HW1` to see how the edits you make will be used.

Some other files that you may find relevant

- [scripts/run_hw1.py](cds_rl/scripts/run_hw1.py) (if running locally) or [scripts/run_hw1.ipynb](cds_rl/scripts/run_hw1.ipynb) (if running on Colab)
- [agents/bc_agent.py](cds_rl/agents/bc_agent.py)

## Run the code

Tip: While debugging, you probably want to keep the flag `--video_log_freq -1` which will disable video logging and speed up the experiment. However, feel free to remove it to save videos of your awesome policy!

If running on Colab, adjust the `#@params` in the `Args` class according to the commmand line arguments above.

### Behavior Cloning

Run command for problem BC.1:

```bash
cd cds_rl

python scripts/run_hw1.py \
    --expert_policy_file policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
    --expert_data expert_data/expert_data_Ant-v2.pkl \
    --video_log_freq -1
```

### DAgger

Run command for DA.1:

```bash
cd cds_rl

python scripts/run_hw1.py \
    --expert_policy_file policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name dagger_ant --n_iter 10 \
    --do_dagger --expert_data expert_data/expert_data_Ant-v2.pkl \
    --video_log_freq -1
```

Note the `--do_dagger` flag, and the higher value for `n_iter`.

## Visualization the saved tensorboard event file

You can visualize your runs using tensorboard:

```bash
tensorboard --logdir data
```

You will see scalar summaries as well as videos of your trained policies (in the 'images' tab).

You can choose to visualize specific runs with a comma-separated list:

```bash
tensorboard --logdir data/run1,data/run2,data/run3...
```

If running on Colab, you will be using the `%tensorboard` [line magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) to do the same thing; see the [notebook](cds_rl/scripts/run_hw1.ipynb) for more details.

## Credits

This homework is based on [Berkeley CS285 Deep RL Course HW1](https://github.com/berkeleydeeprlcourse/homework_fall2021/tree/main/hw1).
