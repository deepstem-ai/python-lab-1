import turtle
import random

# Create turtle object
t = turtle.Turtle()

# Set pen size to 3
t.pensize(3)

for _ in range(5):
    # Generate random color
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(f"#{red:02x}{green:02x}{blue:02x}")

    # Draw pentagon
    t.forward(100)
    t.left(72)

# Keep window open until closed manually
turtle.done()
