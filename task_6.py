def greedy_algorithm(items, budget):
    # Створюємо список кортежів (страва, вартість, калорії, калорії/вартість)
    item_list = [(item, data['cost'], data['calories'], data['calories'] / data['cost']) for item, data in
                 items.items()]

    # Сортуємо список за співвідношенням калорій/вартість у спадаючому порядку
    item_list.sort(key=lambda x: x[3], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item in item_list:
        if total_cost + item[1] <= budget:
            total_cost += item[1]
            total_calories += item[2]
            chosen_items.append(item[0])

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    # Створюємо матрицю dp для збереження максимальної калорійності для кожного бюджету від 0 до заданого
    dp = [[0] * (budget + 1) for _ in range(n)]

    # Заповнюємо матрицю dp
    for i in range(n):
        name, data = item_list[i]
        cost = data['cost']
        calories = data['calories']

        for b in range(budget + 1):
            if i == 0:
                dp[i][b] = calories if cost <= b else 0
            else:
                dp[i][b] = dp[i - 1][b]
                if cost <= b:
                    dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    # Відновлюємо оптимальний набір страв
    optimal_set = []
    b = budget
    for i in range(n - 1, -1, -1):
        if i == 0 and dp[i][b] > 0:
            optimal_set.append(item_list[i][0])
        elif dp[i][b] != dp[i - 1][b]:
            optimal_set.append(item_list[i][0])
            b -= item_list[i][1]['cost']

    optimal_set.reverse()

    return optimal_set, dp[n - 1][budget]


# Дані про їжу:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
chosen_items, total_cost, total_calories = greedy_algorithm(items, budget)
print(f"Обрані страви: {chosen_items}")
print(f"Загальна вартість: {total_cost}")
print(f"Загальна калорійність: {total_calories}")

print("\nАлгоритм динамічного програмування:")
optimal_set, max_calories = dynamic_programming(items, budget)
print(f"Оптимальний набір страв: {optimal_set}")
print(f"Максимальна кількість калорій: {max_calories}")
