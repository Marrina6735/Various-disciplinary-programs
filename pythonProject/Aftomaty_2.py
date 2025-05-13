import torch
import torch.nn as nn
import torch.optim as optim
import gym
import numpy as np
import pygame
import sys

# Определение среды Gym
class CustomEnv(gym.Env):
    def __init__(self, agent_start_pos):
        super(CustomEnv, self).__init__()
        self.agent_start_pos = np.array(agent_start_pos)  # Сохраняем начальную позицию
        self.agent_position = np.array(agent_start_pos)
        self.target_position = np.array([0, 0])  # Начальная позиция цели
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Discrete(100)

        # Инициализация препятствий
        self.obstacle1_position = np.array([3, 4])
        self.obstacle2_position = np.array([5, 2])

    def step(self, action):
        if action == 0:  # Вверх
            self.agent_position[0] = max(0, self.agent_position[0] - 1)
        elif action == 1:  # Вниз
            self.agent_position[0] = min(9, self.agent_position[0] + 1)
        elif action == 2:  # Влево
            self.agent_position[1] = max(0, self.agent_position[1] - 1)
        elif action == 3:  # Вправо
            self.agent_position[1] = min(9, self.agent_position[1] + 1)

        # Проверка на столкновение с препятствиями
        if np.array_equal(self.agent_position, self.obstacle1_position) or np.array_equal(self.agent_position, self.obstacle2_position):
            done = True
            reward = -3  # Штраф за столкновение с препятствием
        else:
            done = np.array_equal(self.agent_position, self.target_position)
            reward = -1 if not done else 0

        return self.agent_position, reward, done, {}

    def reset(self):
        self.agent_position = self.agent_start_pos.copy()  # Сброс к начальной позиции
        # Рандомно выбираем новую позицию для цели
        self.target_position[0] = np.random.randint(0, 10)
        self.target_position[1] = np.random.randint(0, 10)
        return self.agent_position

# Преобразование состояния в индекс
def state_to_index(state):
    return state[0] * 10 + state[1]

# Определение Q-обучения агента
class QLearningAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))
        self.learning_rate = 0.1
        self.discount_factor = 0.99
        self.epsilon = 0.1

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.action_size)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.discount_factor * np.max(self.q_table[next_state, :])
        self.q_table[state, action] += self.learning_rate * (target - predict)

# Определение нейронной сети для PPO
class PolicyNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(),
        )
        self.action_head = nn.Linear(64, output_dim)
        self.value_head = nn.Linear(64, 1)

    def forward(self, x):
        x = self.fc(x)
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        state_values = self.value_head(x)
        return action_probs, state_values

# Определение PPO-агента
class PPOAgent:
    def __init__(self, state_dim, action_dim):
        self.policy_network = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy_network.parameters(), lr=0.001)

    def choose_action(self, state):
        state = torch.FloatTensor(state)  # Преобразовать состояние в тензор
        with torch.no_grad():
            action_probs, _ = self.policy_network(state)
            action = torch.multinomial(action_probs, 1).item()
        return action

    def update_policy(self, states, actions, rewards, action_probs):
        policy_probs, _ = self.policy_network(torch.FloatTensor(states))
        policy_actions = torch.tensor(actions)
        selected_action_probs = torch.gather(policy_probs, 1, policy_actions.unsqueeze(1)).squeeze()

        advantages = rewards - np.mean(rewards)
        loss = -torch.mean(torch.log(selected_action_probs) * torch.FloatTensor(advantages) * torch.FloatTensor(action_probs))

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

# Инициализация среды и агентов
env_q = CustomEnv([8, 5])  # Среда для Q-learning агента
env_ppo = CustomEnv([0, 9])  # Среда для PPO агента

q_agent = QLearningAgent(env_q.observation_space.n, env_q.action_space.n)
ppo_agent = PPOAgent(2, env_ppo.action_space.n)

# Инициализация Pygame
pygame.init()
cell_size = 50  # Уменьшенный размер клетки
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("CustomEnv Visualization")

# Обучение агентов
for episode in range(1000):
    state_q = env_q.reset()
    state_ppo = env_ppo.reset()
    total_reward_q = 0
    total_reward_ppo = 0

    while True:
        # Q-learning агент
        action_q = q_agent.choose_action(state_to_index(state_q))
        next_state_q, reward_q, done_q, _ = env_q.step(action_q)
        q_agent.update_q_table(state_to_index(state_q), action_q, reward_q, state_to_index(next_state_q))
        state_q = next_state_q
        total_reward_q += reward_q

        # PPO агент
        action_ppo = ppo_agent.choose_action(state_ppo.flatten())
        next_state_ppo, reward_ppo, done_ppo, _ = env_ppo.step(action_ppo)
        state_ppo = next_state_ppo
        total_reward_ppo += reward_ppo

        # Визуализация
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size), 1)
                if np.array_equal(state_q, [i, j]):
                    pygame.draw.circle(screen, (255, 0, 0), (i * cell_size + cell_size // 2, j * cell_size + cell_size // 2), cell_size // 2)  # Q-agent
                if np.array_equal(state_ppo, [i, j]):
                    pygame.draw.circle(screen, (0, 0, 255), (i * cell_size + cell_size // 2, j * cell_size + cell_size // 2), cell_size // 2)  # PPO-agent
                if np.array_equal(env_q.target_position, [i, j]):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size))  # Цель
                if np.array_equal([i, j], env_q.obstacle1_position) or np.array_equal([i, j], env_q.obstacle2_position):
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size))  # Препятствие

        pygame.display.flip()

        if done_q or done_ppo:
            break

    print(f"Episode {episode}: Q-learning Total Reward: {total_reward_q}, PPO Total Reward: {total_reward_ppo}")

pygame.quit()
