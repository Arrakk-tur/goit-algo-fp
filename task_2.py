import turtle
import math


# Функція для малювання гілки дерева Піфагора
def draw_pifagor_tree(t, length, depth, angle):
    if depth == 0:
        return
    else:
        t.forward(length * depth)  # Малюємо гілку
        t.right(angle)  # Поворот направо
        draw_pifagor_tree(t, length, depth-1, angle)  # Рекурсивно малюємо праву гілку
        t.left(2 * angle)  # Поворот наліво
        draw_pifagor_tree(t, length, depth-1, angle)  # Рекурсивно малюємо ліву гілку
        t.right(angle)  # Поворот направо
        t.backward(length * depth)  # Повертаємось назад


# Функція для налаштування та виклику малювання дерева Піфагора
def main():
    # Налаштування вікна для малювання
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найбільша швидкість малювання
    t.left(90)
    t.penup()
    t.goto(0, -250)  # Початкова позиція черепашки
    t.pendown()

    # Введення користувача для глибини рекурсії та кута
    depth = int(input("Введіть глибину рекурсії (ціле число, рекомендовано 6-12): "))
    angle = 45

    # Малюємо дерево Піфагора
    draw_pifagor_tree(t, 10, depth, angle)

    # Завершення програми при кліку на вікно
    screen.exitonclick()


if __name__ == "__main__":
    main()
