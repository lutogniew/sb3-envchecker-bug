import random
from typing import Any, Dict, Optional, Tuple

import gymnasium as gym
import numpy as np
from gymnasium import spaces
from stable_baselines3.common.env_checker import check_env


class BugTriggeredException(Exception):
    pass


class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {'render_modes': ['human'], 'render_fps': 1}

    def __init__(self, steps_before_termination: int = 1):
        super().__init__()

        assert steps_before_termination >= 1
        self._steps_before_termination = steps_before_termination

        self._steps_called = 0
        self._terminated = False

        self.action_space = spaces.Discrete(n=2)
        self.observation_space = spaces.Discrete(n=2)
        self.reward_range = (-1., 1.,)

    def reset(self, *, seed: Optional[int] = None, options: Optional[Dict] = None) -> Tuple[np.ndarray, Dict]:
        """
        Resets the environment to an initial state, required before calling step.
        Returns the first agent observation for an episode and information, i.e. metrics, debug info.
        """
        super().reset(seed=seed)

        self._steps_called = 0
        self._terminated = False

        return self.observation_space.sample(), {}

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        self._steps_called += 1

        if self._terminated:
            raise BugTriggeredException

        observation = self.observation_space.sample()
        reward = random.uniform(*self.reward_range)
        self._terminated = self._steps_called >= self._steps_before_termination
        truncated = False

        return observation, reward, self._terminated, truncated, {}

    def render(self, mode: str = 'human') -> None:
        pass

    def close(self):
        pass


if __name__ == '__main__':
    env = CustomEnv(steps_before_termination=1)
    check_env(env)
