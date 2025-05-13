import numpy as np
import pygame
import gym
from gym import spaces
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions import Categorical

# Определение окружения
class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()

        self.grid_size = 10
        self.cell_size = 40

        self.observation_space = spaces.Box(low=0, high=255, shape=(self.grid_size, self.grid_size, 3), dtype=np.uint8)
        self.action_space = spaces.Discrete(4)

        self.agent1_position = np.array([0, 0])
        self.agent2_position = np.array([9, 9])
        self.goal_position = np.random.randint(1, self.grid_size-1, size=2)
        self.obstacle_positions = np.array([[3, 5], [7, 2]])

        self.agent1_color = (0, 0, 255)  # Синий
        self.agent2_color = (0, 255, 0)  # Зеленый
        self.goal_color = (255, 0, 0)    # Красный
        self.obstacle_color = (128, 128, 128)  # Серый

    def reset(self):
        self.agent1_position = np.array([0, 0])
        self.agent2_position = np.array([9, 9])
        self.goal_position = np.random.randint(1, self.grid_size-1, size=2)
        return self._get_obs()

    def _get_obs(self):
        img = np.zeros((self.grid_size, self.grid_size, 3), dtype=np.uint8)
        img[self.agent1_position[0], self.agent1_position[1]] = self.agent1_color
        img[self.agent2_position[0], self.agent2_position[1]] = self.agent2_color
        img[self.goal_position[0], self.goal_position[1]] = self.goal_color
        for obstacle_pos in self.obstacle_positions:
            img[obstacle_pos[0], obstacle_pos[1]] = self.obstacle_color
        return img

    def step(self, action1, action2):
        reward1, reward2 = 0, 0

        # Движение агента 1
        if action1 == 0 and self.agent1_position[0] > 0 and not self._check_collision(self.agent1_position[0] - 1, self.agent1_position[1]):
            self.agent1_position[0] -= 1  # Вверх
        elif action1 == 1 and self.agent1_position[0] < self.grid_size - 1 and not self._check_collision(self.agent1_position[0] + 1, self.agent1_position[1]):
            self.agent1_position[0] += 1  # Вниз
        elif action1 == 2 and self.agent1_position[1] > 0 and not self._check_collision(self.agent1_position[0], self.agent1_position[1] - 1):
            self.agent1_position[1] -= 1  # Влево
        elif action1 == 3 and self.agent1_position[1] < self.grid_size - 1 and not self._check_collision(self.agent1_position[0], self.agent1_position[1] + 1):
            self.agent1_position[1] += 1  # Вправо

        # Движение агента 2
        if action2 == 0 and self.agent2_position[0] > 0 and not self._check_collision(self.agent2_position[0] - 1, self.agent2_position[1]):
            self.agent2_position[0] -= 1  # Вверх
        elif action2 == 1 and self.agent2_position[0] < self.grid_size - 1 and not self._check_collision(self.agent2_position[0] + 1, self.agent2_position[1]):
            self.agent2_position[0] += 1  # Вниз
        elif action2 == 2 and self.agent2_position[1] > 0 and not self._check_collision(self.agent2_position[0], self.agent2_position[1] - 1):
            self.agent2_position[1] -= 1  # Влево
        elif action2 == 3 and self.agent2_position[1] < self.grid_size - 1 and not self._check_collision(self.agent2_position[0], self.agent2_position[1] + 1):
            self.agent2_position[1] += 1  # Вправо

        # Проверка на цель
        if np.array_equal(self.agent1_position, self.goal_position):
            reward1 = 1
        if np.array_equal(self.agent2_position, self.goal_position):
            reward2 = 1

        # Формирование изображения
        obs = self._get_obs()

        # Проверка на завершение эпизода
        done = np.array_equal(self.agent1_position, self.goal_position) and np.array_equal(self.agent2_position, self.goal_position)

        return obs, reward1, reward2, done

    def _check_collision(self, x, y):
        for obstacle_pos in self.obstacle_positions:
            if np.array_equal([x, y], obstacle_pos):
                return True
        return False

# Определение архитектуры нейросети для агента
class Policy(nn.Module):
    def __init__(self, input_size, output_size):
        super(Policy, self).__init__()
        self.fc = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, output_size)

    def forward(self, x):
        x = F.relu(self.fc(x))
        x = self.fc2(x)
        return F.softmax(x, dim=0)

def select_action(policy, state):
    state = torch.from_numpy(state).float().view(-1)
    probs = policy(state)
    m = Categorical(probs)
    action = m.sample()
    return action.item(), m.log_prob(action)

# Создание среды
env = CustomEnv()

# Инициализация агента 1
state_size = np.prod(env.observation_space.shape)
action_size = env.action_space.n
policy1 = Policy(state_size, action_size)
optimizer1 = optim.Adam(policy1.parameters(), lr=0.01)

# Инициализация агента 2
policy2 = Policy(state_size, action_size)
optimizer2 = optim.Adam(policy2.parameters(), lr=0.01)

# Количество эпизодов
num_episodes = 1000

# Цикл обучения
for episode in range(num_episodes):
    state = env.reset()
    total_reward1, total_reward2 = 0, 0

    while True:
        # Выбор действий для обоих агентов
        action1, log_prob1 = select_action(policy1, state)
        action2, log_prob2 = select_action(policy2, state)

        # Выполнение действий и получение нового состояния и вознаграждений
        next_state, reward1, reward2, done = env.step(action1, action2)

        # Обновление сети агента 1
        loss1 = -log_prob1 * reward1

        # Обновление сети агента 2
        loss2 = -log_prob2 * reward2

        optimizer1.zero_grad()
        loss1.backward()
        optimizer1.step()

        optimizer2.zero_grad()
        loss2.backward()
        optimizer2.step()

        total_reward1 += reward1
        total_reward2 += reward2

        state = next_state

        if done:
            print(f"Эпизод {episode + 1} завершен. Награда агента 1: {total_reward1}, Награда агента 2: {total_reward2}")
            if total_reward1 > total_reward2:
                print("Агент 1 обучился быстрее!")
            elif total_reward1 < total_reward2:
                print("Агент 2 обучился быстрее!")
            else:
                print("Оба агента обучились одинаково.")
            break
