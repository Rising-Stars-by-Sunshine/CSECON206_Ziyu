import gym
from gym import spaces
import numpy as np
import random

# Defining the Trust Game Environment
class TrustGameEnv(gym.Env):
    def __init__(self):
        super(TrustGameEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # In Trust game, action can be amount of money to send or return
        # Here, for simplicity, we'll use a discrete action space (0 or 1)
        self.action_space = spaces.Discrete(2)
        
        # Observation space - the state contains the amount of money sent by the investor
        # For simplicity, it's also a discrete space (0 or 1)
        self.observation_space = spaces.Discrete(2)

    def reset(self):
        # Reset the state of the environment to an initial state
        self.state = 0  # Initial state - no money sent
        return self.state

    def step(self, action):
        # Execute one time step within the environment
        # The action can be 0 (do nothing/send back nothing) or 1 (send money/return money)
        if self.state == 0:  # Investor's turn
            self.state = action  # Investor sends money or not
            reward = 0
            done = False  # Game is not finished yet
        else:  # Trustee's turn
            if action == 1:  # Trustee returns money
                reward = 1  # Investor gains a reward
            else:
                reward = -1  # Investor loses
            done = True  # End of episode

        return self.state, reward, done, {}

    def render(self, mode='console'):
        if mode != 'console':
            raise NotImplementedError()
        # Render the environment to the screen
        if self.state == 0:
            print("Investor's turn")
        else:
            print("Trustee's turn")

# Test the environment
env = TrustGameEnv()
env.reset()
for _ in range(2):  # Play two turns
    random_action = env.action_space.sample()  # Choose a random action
    state, reward, done, info = env.step(random_action)  # Take the action
    env.render()  # Render the state
    if done:
        break
