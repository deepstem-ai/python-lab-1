import turtle

# Create turtle object
t = turtle.Turtle()

# Set line width to 5
t.pensize(25)

# Set pen color to blue, pink, red, green, gray, black, yellow, skyblue
t.pencolor("skyblue")

# Draw square
for _ in range(4):
    t.forward(200)
    t.left(90)

# Keep window open until closed manually
turtle.done()
