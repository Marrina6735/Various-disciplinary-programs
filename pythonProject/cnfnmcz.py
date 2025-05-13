import itertools
import random

random.seed(42)

# Шаг 1: Определение множеств кандидатов, должностей и видов обучения
candidates = ['v1', 'v2', 'v3']  # Претенденты
positions = ['d1', 'd2', 'd3']  # Вакансии
trainings = ['o1', 'o2', 'o3']  # Виды обучения

edges = {}
edge_count = 1

for candidate in candidates:
    for position in positions:
        for training in trainings:
            # Генерация случайных значений весов
            w1 = random.randint(5, 20)  # Экономический эффект (руб.)
            w2 = random.randint(50, 100)  # Социально-психологический эффект (баллы)
            edge_id = f'e{edge_count}'
            edges[edge_id] = (candidate, position, training, w1, w2)
            edge_count += 1

        # Шаг 3: Функция для вывода таблицы весов ребер с выровненными столбцами


def print_weights_table(edges):
    print("Таблица весов ребер:")
    header = f"{'e':<4} | {'v*':<3} | {'d*':<3} | {'o*':<3} | {'w1(e)':<6} | {'w2(e)':<6}"
    print(header)
    print("-" * len(header))
    for edge, data in edges.items():
        v, d, o, w1, w2 = data
        print(f"{edge:<4} | {v:<3} | {d:<3} | {o:<3} | {w1:<6} | {w2:<6}")
    print()  # Пустая строка для разделения


# Шаг 4: Функция для построения множества допустимых решений (МДР)
def get_valid_combinations(edges, num_candidates):
    all_combinations = []

    # Генерация всех возможных сочетаний ребер размера num_candidates
    for combination in itertools.combinations(edges.items(), num_candidates):
        # Извлекаем кандидатов и должности из текущего сочетания
        candidates_in_comb = [edge[1][0] for edge in combination]
        positions_in_comb = [edge[1][1] for edge in combination]

        # Проверяем уникальность кандидатов и должностей
        if (len(set(candidates_in_comb)) == num_candidates) and (len(set(positions_in_comb)) == num_candidates):
            all_combinations.append(combination)

    return all_combinations


# Шаг 5: Функция для вычисления значений критериев F1(x) и F2(x)
def calculate_criteria(combination):
    F1 = sum(edge[1][3] for edge in combination)  # Сумма w1(e)
    F2 = sum(edge[1][4] for edge in combination)  # Сумма w2(e)
    return F1, F2


# Шаг 6: Функция для поиска Парето-множества (ПМ)
def find_pareto_optimal(solutions, criteria_directions, criteria_priorities):
    """
    Найти Парето-множество из списка решений.

    :param solutions: Список решений, каждое решение представлено как (combination, F1, F2, ...)
    :param criteria_directions: Список направлений для критериев ('min' или 'max')
    :param criteria_priorities: Список приоритетов для критериев (целые числа, меньше = выше приоритет)
    :return: Список Парето-оптимальных решений
    """
    pareto_optimal = []
    for i, (comb_i, *criteria_i) in enumerate(solutions):
        dominated = False
        for j, (comb_j, *criteria_j) in enumerate(solutions):
            if i == j:
                continue
            better_or_equal = True
            strictly_better = False
            for k in range(len(criteria_i)):
                dir = criteria_directions[k]
                if dir == 'max':
                    if criteria_j[k] < criteria_i[k]:
                        better_or_equal = False
                        break
                    elif criteria_j[k] > criteria_i[k]:
                        strictly_better = True
                elif dir == 'min':
                    if criteria_j[k] > criteria_i[k]:
                        better_or_equal = False
                        break
                    elif criteria_j[k] < criteria_i[k]:
                        strictly_better = True
            if better_or_equal and strictly_better:
                dominated = True
                break
        if not dominated:
            pareto_optimal.append((comb_i, *criteria_i))
    return pareto_optimal


# Шаг 7: Основная логика программы
def main():
    # Вывод таблицы весов ребер
    print_weights_table(edges)

    # Определяем количество кандидатов и должностей
    num_candidates = len(candidates)  # В нашем примере 3

    # Построение множества допустимых решений (МДР)
    valid_combinations = get_valid_combinations(edges, num_candidates)

    # Проверка наличия допустимых решений
    if not valid_combinations:
        print("Нет допустимых решений.")
        return

        # Рассчитываем значения целевых функций для каждого сочетания
    solutions = []
    for combination in valid_combinations:
        F1, F2 = calculate_criteria(combination)
        solutions.append((combination, F1, F2))

        # Вывод множества допустимых решений (МДР) в виде списка
    print("Множество допустимых решений (МДР):")
    for idx, (comb, _, _) in enumerate(solutions, 1):
        comb_str = ', '.join([edge[0] for edge in comb])
        print(f"x{idx}=({comb_str})")

        # Вывод таблицы ВЦФ с выровненными столбцами
    print("\nТаблица ВЦФ:")
    header = f"{'x':<4} | {'F1(x)':<6} | {'F2(x)':<6}"
    print(header)
    print("-" * len(header))
    for idx, (_, F1, F2) in enumerate(solutions, 1):
        print(f"x{idx:<2} | {F1:<6} | {F2:<6}")
    print()  # Пустая строка для разделения

    # Пункт 2: Поиск Парето-множества (ПМ)
    print("Поиск Парето-множества (ПМ):")

    # Ввод пользователем направлений оптимизации для критериев
    print("Введите направление оптимизации для каждого критерия (min/max):")
    criteria_directions = []
    for i in range(2):
        while True:
            direction = input(f"Направление для F{i + 1}(x) (min/max): ").strip().lower()
            if direction in ['min', 'max']:
                criteria_directions.append(direction)
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите 'min' или 'max'.")

                # Ввод пользователем приоритетов критериев
    print("\nВведите приоритеты для критериев (1 - самый высокий, 2 - ниже и т.д.):")
    criteria_priorities = []
    for i in range(2):
        while True:
            try:
                priority = int(input(f"Приоритет для F{i + 1}(x): "))
                if priority > 0:
                    criteria_priorities.append(priority)
                    break
                else:
                    print("Приоритет должен быть положительным целым числом.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

                # Поиск Парето-множества
    pareto_optimal = find_pareto_optimal(solutions, criteria_directions, criteria_priorities)

    # Вывод Парето-множества
    if pareto_optimal:
        print("\nПарето-оптимальные решения:")
        for idx, (comb, F1, F2) in enumerate(pareto_optimal, 1):
            comb_str = ', '.join([edge[0] for edge in comb])
            print(f"x{idx}=({comb_str}) | F1(x)={F1} | F2(x)={F2}")
    else:
        print("Парето-множество пусто. Нет оптимальных решений.")

        # Дополнительно: Вывод таблицы Парето-множества
    if pareto_optimal:
        print("\nТаблица Парето-множества (ПМ):")
        header_pm = f"{'x':<4} | {'F1(x)':<6} | {'F2(x)':<6}"
        print(header_pm)
        print("-" * len(header_pm))
        for idx, (_, F1, F2) in enumerate(pareto_optimal, 1):
            print(f"x{idx:<2} | {F1:<6} | {F2:<6}")
        print()


if __name__ == "__main__":
    main()
