import turtle


def draw_tree():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    t = turtle.Turtle()
    t.speed(3)

    # Funkcja do rysowania trójkąta (koloru zielonego), który będzie reprezentował liście choinki
    def draw_triangle(t, length, color):
        t.begin_fill()
        t.fillcolor(color)
        for _ in range(3):
            t.forward(length)
            t.left(120)
        t.end_fill()

    # Funkcja do rysowania prostokąta (koloru brązowego), który będzie reprezentował pień choinki
    def draw_rectangle(t, width, height, color):
        t.begin_fill()
        t.fillcolor(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    # Rysowanie choinki
    t.penup()
    t.goto(-50, -120)
    t.pendown()
    draw_triangle(t, 100, "green")
    t.penup()
    t.goto(-40, -160)
    t.pendown()
    draw_triangle(t, 80, "green")
    t.penup()
    t.goto(-30, -190)
    t.pendown()
    draw_triangle(t, 60, "green")
    t.penup()
    t.goto(-20, -210)
    t.pendown()
    draw_rectangle(t, 40, 20, "brown")

    # Ukrycie żółwia i wyświetlenie gotowego rysunku
    t.hideturtle()
    screen.mainloop()


draw_tree()
