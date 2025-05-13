import numpy as np
import gym
import pygame
import sys
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

GRID_SIZE = 10
CELL_SIZE = 40
AGENT_COLOR = (0, 0, 255)
GOAL_COLOR = (255, 0, 0)
OBSTACLE_COLOR = (128, 128, 128)
SECOND_AGENT_COLOR = (255, 255, 0)

class Policy(nn.Module):
    def __init__(self, input_size, output_size):
        super(Policy, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        return F.softmax(self.fc(x), dim=-1)

class PPOAgent:
    def __init__(self, env):
        self.env = env
        self.policy = Policy(env.observation_space.n, env.action_space.n)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=0.01)

    def choose_action(self, state):
        state = torch.FloatTensor(state)
        action_probs = self.policy(state)
        action = torch.multinomial(action_probs, 1).item()
        return action

    def learn(self, total_timesteps=10000):
        # Тут нужно добавить обучение агента PPO
        pass

# Остальной код остается без изменений
