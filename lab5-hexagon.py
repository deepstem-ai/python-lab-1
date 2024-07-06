import turtle

# Create turtle object
t = turtle.Turtle()

# Define color list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    # Set pen color
    t.pencolor(colors[i])

    # Draw hexagon
    t.forward(120)
    t.left(60)

# Keep window open until closed manually
turtle.done()
