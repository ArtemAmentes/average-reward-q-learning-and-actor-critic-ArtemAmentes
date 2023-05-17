# Installation guide

HW3 has the same requirements as HW1, so if you have followed the installation [guide](../hw1/installation.md) for HW1, you are almost set up!

There is a single new package requirement (`gym[atari]`) beyond what was used in the previous assignments; make sure to install it if you are running the assignment locally:

```bash
pip install "gym[atari]"
```

Additionally, you only need to install hw3 codebase as a development package `hw3`:

```bash
cd <path_to_hw3>
pip install -e .
```
