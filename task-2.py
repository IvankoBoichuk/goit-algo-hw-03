import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Отримуємо рівень рекурсії від користувача
    order = int(input("Введіть рівень рекурсії (ціле число): "))
    
    # Налаштовуємо вікно turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    
    # Налаштовуємо turtle
    t = turtle.Turtle()
    t.speed('fastest')  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Малюємо сніжинку Коха
    size = 400  # Розмір сніжинки
    koch_snowflake(t, order, size)

    # Завершуємо роботу turtle
    turtle.done()

if __name__ == "__main__":
    main()
