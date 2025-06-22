import turtle
import math


def draw_branch(t, length, level):
    if level == 0:
        return

    t.forward(length)

    pos = t.pos()
    angle = t.heading()

    t.left(45)
    draw_branch(t, length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.setpos(pos)
    t.setheading(angle)
    t.pendown()

    t.right(45)
    draw_branch(t, length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.setpos(pos)
    t.setheading(angle)
    t.pendown()


def main():
    level = int(input("Вкажіть рівень рекурсії (наприклад 5–12): "))

    screen = turtle.Screen()
    screen.title("Фрактал: Дерево Піфагора")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("red")
    t.pensize(2)
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0, -250)
    t.setheading(90)  
    t.pendown()

    draw_branch(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
