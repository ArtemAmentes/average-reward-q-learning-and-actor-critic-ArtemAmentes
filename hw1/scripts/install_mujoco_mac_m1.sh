# Full guide is here: https://github.com/geyang/jaynes-starter-kit/blob/2fb0864ae10e1a52b15b592393738c6f2ff839cc/docker/m1_mac_mujoco_setup.md
# Check and fulfill the prerequisites, then run this shell script

mkdir -p $HOME/.mujoco/mujoco210
ln -sf /Applications/MuJoCo.app/Contents/Frameworks/MuJoCo.framework/Versions/Current/Headers/ $HOME/.mujoco/mujoco210/include

mkdir -p $HOME/.mujoco/mujoco210/bin
ln -sf /Applications/MuJoCo.app/Contents/Frameworks/MuJoCo.framework/Versions/Current/libmujoco.2.1.1.dylib $HOME/.mujoco/mujoco210/bin/libmujoco210.dylib
sudo ln -sf /Applications/MuJoCo.app/Contents/Frameworks/MuJoCo.framework/Versions/Current/libmujoco.2.1.1.dylib /usr/local/lib/

# For M1 (arm64) mac users:
# brew install glfw
ln -sf /opt/homebrew/lib/libglfw.3.dylib $HOME/.mujoco/mujoco210/bin

# remove old installation. Uncomment and fill in if needed
#rm -rf <conda_env_root>/<env_name>/lib/python3.8/site-packages/mujoco_py

# which python
# exit

export CC=/opt/homebrew/bin/gcc-11         # see https://github.com/openai/mujoco-py/issues/605
pip install mujoco-py && python -c 'import mujoco_py'