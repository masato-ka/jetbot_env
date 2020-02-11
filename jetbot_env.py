import numpy as np
from gym import Env, spaces
from jetbot import Robot

from config import IMAGE_SIZE, MIN_STEERING, MAX_STEERING, IMAGE_HEIGHT, IMAGE_WIDTH
from core.controller import RobotController
from core.observer import Observer


class JetbotEnv(Env):

    def __init__(self):
        super(JetbotEnv, self).__init__()
        self.controller = RobotController()
        self.observer = Observer(IMAGE_WIDTH, IMAGE_HEIGHT)
        self.observation_space = spaces.Box(low=np.finfo(np.float32).min,
                                            high=np.finfo(np.float32).max,
                                            shape=IMAGE_SIZE,
                                            dtype=np.float32)
        self.action_space = spaces.Box(ow=np.array([MIN_STEERING, MIN_STEERING]),
                                       high=np.array([MAX_STEERING, MAX_STEERING]), dtype=np.float32)
        self.ie = {}

    def step(self, action):
        self.controller.action(action[0], action[1])
        obs = self.observer.observation()
        reward = 1.0
        done = False
        return obs, reward, done, self.ie
        pass

    def reset(self):
        self.controller.action(0,0)
        obs = self.observer.observation()
        return obs

    def render(self, mode='human'):
        pass

    def seed(self,seed):
        pass

    def close(self):
        #TODO theredown thread.
        pass