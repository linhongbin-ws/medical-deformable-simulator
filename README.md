medical-deformable-simulator


## Install mujoco-py

The origin [mujoco-py](https://github.com/openai/mujoco-py) cannot render soft object. Check out this [issue](https://github.com/openai/mujoco-py/issues/373)

Here is the fixing method:

```sh
pip3 uninstall  -y mujoco_py

git clone git@github.com:fantasyRqg/mujoco-py.git

cd mujoco-py

python3 setup.py build

python3 setup.py install

```