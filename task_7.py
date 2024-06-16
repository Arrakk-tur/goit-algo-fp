import random


def simulate_dice_rolls(num_trials):
    """
    Симулює кидки двох кубиків num_trials разів і повертає список з частотами сум кожної можливої суми.
    """
    freq = [0] * 13  # індекси від 2 до 12, тому треба freq[0] до freq[12]

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        freq[total] += 1

    return freq[2:]  # повертаємо частоти для сум від 2 до 12


def calculate_probabilities(freq, num_trials):
    """
    Розраховує ймовірності для кожної можливої суми на основі частот.
    """
    probabilities = []
    total_possible_outcomes = num_trials * 1.0

    for i, count in enumerate(freq, start=2):
        prob_percent = (count / total_possible_outcomes) * 100
        prob_fraction = f"{count}/{num_trials}"
        probabilities.append((i, prob_percent, prob_fraction))

    return probabilities


def main():
    num_trials = 120  # кількість симуляцій
    freq = simulate_dice_rolls(num_trials)
    probabilities = calculate_probabilities(freq, num_trials)

    # Вивід результатів
    print("\nРезультати обчислень\n")
    print("+---------------------------+")
    print(f"|{'Сума':^6}|{'Імовірність':^20}|")
    print("+------+--------------------+")

    # Вивід результатів у вигляді таблиці
    for sum_value, prob_percent, prob_fraction in probabilities:
        prob_formatted = f"{prob_percent:.2f}% ({prob_fraction})"
        print(f"|{sum_value:^6}|{prob_formatted:^20}|")
        print("+------+--------------------+")


if __name__ == "__main__":
    main()
