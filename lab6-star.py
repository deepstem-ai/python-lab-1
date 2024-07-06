import turtle

# Create turtle object
t = turtle.Turtle()

# Define function to draw a single line of the star
def draw_star_line(size, color):
    t.pensize(size)
    t.pencolor(color)
    t.forward(100)
    t.left(144)

# Draw first two lines with increasing size and different colors
draw_star_line(2, "pink")
draw_star_line(4, "blue")

# Draw next three lines with decreasing size and the same color
for _ in range(3):
    t.pensize(t.pensize() - 1)
    draw_star_line(t.pensize(), "gray")

# Keep window open until closed manually
turtle.done()
