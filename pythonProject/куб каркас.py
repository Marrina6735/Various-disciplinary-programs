import numpy as np
import gym
import pygame
import sys

GRID_SIZE = 10
CELL_SIZE = 40
AGENT_COLOR = (0, 0, 255)  # Синий цвет
GOAL_COLOR = (255, 0, 0)   # Красный цвет

class GridWorldEnv(gym.Env):
    def __init__(self):
        super(GridWorldEnv, self).__init__()

        self.grid_size = GRID_SIZE
        self.cell_size = CELL_SIZE

        # Определение пространства состояний и действий
        self.observation_space = gym.spaces.Discrete(self.grid_size**2)
        self.action_space = gym.spaces.Discrete(4)  # Вверх, вниз, влево, вправо

        # Инициализация окружения
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.agent_pos = np.array([0, 0])
        self.goal_pos = np.array([self.grid_size - 1, self.grid_size - 1])

        # Инициализация Q-таблицы
        self.q_table = np.zeros((self.grid_size**2, self.action_space.n))

        # Параметры Q-learning
        self.learning_rate = 1
        self.discount_factor = 0.9
        self.epsilon = 0.05

        # Инициализация Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.grid_size * self.cell_size, self.grid_size * self.cell_size))
        pygame.display.set_caption("Grid World Environment")

    def state_to_index(self, state):
        return state[0] * self.grid_size + state[1]

    def reset(self):
        # Сброс окружения с выбором случайного начального состояния
        self.agent_pos = np.random.randint(0, self.grid_size, size=2)
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Агент
        self.grid[self.goal_pos[0], self.goal_pos[1]] = 2    # Цель

        return self.state_to_index(self.agent_pos)

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return self.action_space.sample()  # Рандомное действие с вероятностью epsilon
        else:
            return np.argmax(self.q_table[state, :])  # Выбор действия с наилучшей оценкой Q

    def step(self, action):
        # Выполнение действия
        old_state = self.state_to_index(self.agent_pos)
        if action == 0 and self.agent_pos[0] > 0:
            self.agent_pos[0] -= 1  # Вверх
        elif action == 1 and self.agent_pos[0] < self.grid_size - 1:
            self.agent_pos[0] += 1  # Вниз
        elif action == 2 and self.agent_pos[1] > 0:
            self.agent_pos[1] -= 1  # Влево
        elif action == 3 and self.agent_pos[1] < self.grid_size - 1:
            self.agent_pos[1] += 1  # Вправо

        new_state = self.state_to_index(self.agent_pos)

        # Вычисление награды
        if np.array_equal(self.agent_pos, self.goal_pos):
            reward = 1  # Агент достиг цели
        else:
            reward = -0.5  # Штраф за каждый шаг

        # Обновление Q-таблицы по уравнению Беллмана
        self.q_table[old_state, action] += self.learning_rate * (reward + self.discount_factor * np.max(self.q_table[new_state, :]) - self.q_table[old_state, action])

        # Проверка на завершение эпизода
        done = np.array_equal(self.agent_pos, self.goal_pos)

        # Обновление состояния среды
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Агент
        self.grid[self.goal_pos[0], self.goal_pos[1]] = 2    # Цель

        return new_state, reward, done, {}

    def render_q_values(self):
        # Визуализация Q-значений
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                state = self.state_to_index(np.array([i, j]))
                q_values = self.q_table[state, :]
                max_q_value = np.max(q_values)
                color = int(255 * max_q_value)
                pygame.draw.rect(self.screen, (255, 255, 255), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def render(self):
        # Отрисовка сетки и агента/цели
        self.screen.fill((255, 255, 255))  # Белый фон

        self.render_q_values()

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(self.screen, (0, 0, 0), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)

                if self.grid[i, j] == 1:  # Агент
                    pygame.draw.circle(self.screen, AGENT_COLOR, (j * self.cell_size + self.cell_size // 2, i * self.cell_size + self.cell_size // 2), self.cell_size // 2)
                elif self.grid[i, j] == 2:  # Цель
                    pygame.draw.rect(self.screen, GOAL_COLOR, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

        pygame.display.flip()

        pygame.time.delay(20)

    # Создание среды
env = GridWorldEnv()

# Цикл обучения
for _ in range(1000):
    state = env.reset()
    total_reward = 0

    while True:
        env.render()

        action = env.choose_action(state)
        next_state, reward, done, _ = env.step(action)

        total_reward += reward
        state = next_state

        if done:
            print(f"Эпизод завершен. Награда: {total_reward}")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
