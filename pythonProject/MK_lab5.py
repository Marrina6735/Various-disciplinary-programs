import numpy as np
import gym
import pygame
import sys

GRID_SIZE = 10  # Размер сетки
CELL_SIZE = 40  # Размер ячейки сетки
AGENT_COLOR = (0, 0, 255)  # Синий цвет
SECOND_AGENT_COLOR = (255, 255, 0)  # Желтый цвет
GOAL_COLOR = (255, 0, 0)  # Красный цвет
OBSTACLE_COLOR = (128, 128, 128)  # Серый цвет для препятствий


class WorldGridEnv(gym.Env):
    def __init__(self):  # Инициализация окружения, пространства состояний и действий
        super(WorldGridEnv, self).__init__()

        self.grid_size = GRID_SIZE
        self.cell_size = CELL_SIZE

        # Определение пространства состояний и действий
        self.observation_space = gym.spaces.Discrete(self.grid_size ** 2)
        self.action_space = gym.spaces.Discrete(4)  # Вверх, вниз, влево, вправо

        # Инициализация окружения
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.agent_position = np.array([0, 0])
        self.second_agent_position = np.array([0, 0])
        self.goal_position = np.array([self.grid_size - 1, self.grid_size - 1])

        # Инициализация препятствий
        self.obstacle_positions = np.array([[2, 3], [3, 4]])

        # Инициализация Q-таблиц
        self.q_table = np.zeros((self.grid_size ** 2, self.action_space.n))
        self.second_q_table = np.zeros((self.grid_size ** 2, self.action_space.n))

        # Параметры Q-learning
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1

        # Инициализация Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.grid_size * self.cell_size, self.grid_size * self.cell_size))
        pygame.display.set_caption("Grid World Environment")

    def state_to_index(self, state):  # Метод для преобразования состояния (позиции агента) в индекс для Q-таблицы
        return state[0] * self.grid_size + state[1]

    def reset(self):
        # Сброс окружения с выбором случайного начального состояния
        self.agent_position = np.random.randint(0, self.grid_size, size=2)
        self.second_agent_position = np.random.randint(0, self.grid_size, size=2)

        while np.array_equal(self.agent_position, self.second_agent_position):
            self.second_agent_position = np.random.randint(0, self.grid_size, size=2)

        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.grid[self.agent_position[0], self.agent_position[1]] = 1  # Агент
        self.grid[self.second_agent_position[0], self.second_agent_position[1]] = 4  # Второй агент
        self.grid[self.goal_position[0], self.goal_position[1]] = 2  # Цель

        # Размещение препятствий
        for obstacle_pos in self.obstacle_positions:
            self.grid[obstacle_pos[0], obstacle_pos[1]] = 3

        return self.state_to_index(self.agent_position)

    def choose_action(self, state, q_table):  # Выбор действия агента с учетом вероятности epsilon для исследования
        if np.random.rand() < self.epsilon:
            return self.action_space.sample()  # Рандомное действие с вероятностью epsilon
        else:
            return np.argmax(q_table[state, :])  # Выбор действия с наилучшей оценкой Q

    def step(self, action, agent_position, q_table):  # Общий метод для выполнения действия
        old_state = self.state_to_index(agent_position)
        if action == 0 and agent_position[0] > 0 and self.grid[agent_position[0] - 1, agent_position[1]] != 3:
            agent_position[0] -= 1  # Вверх
        elif action == 1 and agent_position[0] < self.grid_size - 1 and self.grid[agent_position[0] + 1, agent_position[1]] != 3:
            agent_position[0] += 1  # Вниз
        elif action == 2 and agent_position[1] > 0 and self.grid[agent_position[0], agent_position[1] - 1] != 3:
            agent_position[1] -= 1  # Влево
        elif action == 3 and agent_position[1] < self.grid_size - 1 and self.grid[agent_position[0], agent_position[1] + 1] != 3:
            agent_position[1] += 1  # Вправо

        new_state = self.state_to_index(agent_position)

        # Вычисление награды
        if np.array_equal(agent_position, self.goal_position):
            reward = 1  # Агент достиг цели
        else:
            reward = -0.5  # Штраф за каждый шаг

        # Обновление Q-таблицы по уравнению Беллмана
        q_table[old_state, action] += self.learning_rate * (
                reward + self.discount_factor * np.max(q_table[new_state, :]) - q_table[old_state, action])

        return new_state, reward, agent_position

    def render_q_values(self):  # Визуализация Q-значений
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                state = self.state_to_index(np.array([i, j]))
                q_values = self.q_table[state, :]
                second_q_values = self.second_q_table[state, :]

                max_q_value = np.max(q_values)
                max_second_q_value = np.max(second_q_values)

                color = int(255 * max_q_value)
                second_color = int(255 * max_second_q_value)

                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def render(self):  # Отрисовка сетки и агентов/цели/препятствий
        self.screen.fill((255, 255, 255))  # Белый фон

        self.render_q_values()

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)

                if self.grid[i, j] == 1:  # Первый агент
                    pygame.draw.circle(self.screen, AGENT_COLOR,
                                       (j * self.cell_size + self.cell_size // 2, i * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2)
                elif self.grid[i, j] == 2:  # Цель
                    pygame.draw.rect(self.screen, GOAL_COLOR,
                                     (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
                elif self.grid[i, j] == 3:  # Препятствие
                    pygame.draw.rect(self.screen, OBSTACLE_COLOR,
                                     (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
                elif self.grid[i, j] == 4:  # Второй агент
                    pygame.draw.polygon(self.screen, SECOND_AGENT_COLOR, [
                        (j * self.cell_size + self.cell_size // 2, i * self.cell_size),
                        (j * self.cell_size, i * self.cell_size + self.cell_size),
                        (j * self.cell_size + self.cell_size, i * self.cell_size + self.cell_size)
                    ])

        pygame.display.flip()

        pygame.time.delay(20)


# Создание среды
env = WorldGridEnv()

# Цикл обучения
for episode in range(1000):
    state = env.reset()
    second_state = env.state_to_index(env.second_agent_position)  # Получаем начальное состояние для второго агента
    total_reward = 0

    while True:
        env.render()

        action = env.choose_action(state, env.q_table)
        next_state, reward, env.agent_position = env.step(action, env.agent_position, env.q_table)

        second_action = env.choose_action(second_state, env.second_q_table)
        next_second_state, second_reward, env.second_agent_position = env.step(second_action, env.second_agent_position,
                                                                                env.second_q_table)

        total_reward += reward + second_reward
        state = next_state
        second_state = next_second_state

        if np.array_equal(env.agent_position, env.goal_position) and np.array_equal(env.second_agent_position,
                                                                                    env.goal_position):
            print(f"Эпизод {episode + 1} завершен. Награда: {total_reward}")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
