# sb3-envchecker-bug

Code for reproducing a bug in `stable-baselines3 = 2.0.0a5` where `stable_baselines3.common.env_checker.check_env`
incorrectly assumes that the checked environment will have >1 steps available.

## Installation

For local development:
```shell
# Create a virtual environment
$ python -m venv venv/
# Install PyPI dependencies
$ venv/bin/python -m ensurepip --default-pip
$ venv/bin/pip install -e .
```

Optionally, to use a local copy of `stable-baselines3`:
```shell
# Install phoebe-common as a local dependency
$ venv/bin/pip install -e '/path/to/stable-baselines3' --no-binary ':all:'
```

# Running

Expect a `BugTriggeredException`:
```shell
$ venv/bin/python main.py
```
