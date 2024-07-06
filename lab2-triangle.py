import turtle

# Create turtle object
t = turtle.Turtle()

# Set pen style to dashed line


# Set pen color to red
t.pencolor("red")

# Draw triangle
for _ in range(3):
    t.forward(150)
    t.left(120)

# Keep window open until closed manually
turtle.done()
