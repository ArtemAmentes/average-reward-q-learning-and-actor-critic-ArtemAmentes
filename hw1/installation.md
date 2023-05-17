# Installation guide

## Install main dependencies

There are two options: a) conda-based install or b) pip-based. The former contains python virtual environment management, for the latter you have to manage it on your own (see [understanding pip and conda](https://www.anaconda.com/blog/understanding-conda-and-pip) for details).

### (Recommended) Install with conda/mamba

1. Install `conda` or even better `mamba`: [Mamba + Miniforge = Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), or [Miniforge](https://github.com/conda-forge/miniforge)
   1. If you chose mamba, just replace `conda` to `mamba` for the rest of the scripts below or just add an alias `alias conda=mamba` to your .bashrc, .zshrc or alike.

2. Init conda for your shell:

    ```bash
    conda init
    ```

3. Create conda environment `cds_rl`:

    ```bash
    conda env create -f requirements.yml
    ```

4. Activate the environment (do this every time you open a new terminal):

    ```bash
    conda activate cds_rl
    ```

5. Additionally install requirements that can be installed only with pip:

    ```bash
    pip install opencv-python
    ```

6. Install locally all your code as a package `cds_rl` in development mode:

    ```bash
    cd <path_to_hw1>
    pip install -e .
    ```

The conda environment requires activating it every time you open a new terminal (in order to run code), but the benefit is that the required dependencies for this codebase will not affect existing/other versions of things on your computer. This stand-alone environment will have everything that is necessary.

### Or install all with pip

Make sure you understand where you install with pip (is it system python or virtual environment)!

```bash
pip install -r requirements.txt
cd <path_to_hw1>
pip install -e .
```

## Install mujoco-py

Finally, we will install mujoco-py package. If you are on Mac M1, check out this [script](./scripts/install_mujoco_mac_m1.sh) - follow the guide linked there and then run the script itself.

Otherwise, try following:

```bash
pip install free-mujoco-py

# for the first run it should take time to cythonize pkg
python -c "import mujoco_py"

# check installation - it should show an image from the HalfCheetah environment
python -c "import mujoco_py, gym, matplotlib.pyplot as plt; plt.imshow(gym.make('HalfCheetah-v3').render('rgb_array')); plt.show(block=True)
```

If nothing [even googling] works, you may find using Colab as the preferred option.
