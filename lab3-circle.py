import turtle

# Create turtle object
t = turtle.Turtle()

for i in range(1, 21):
    # Set line size based on loop iteration
    t.pensize(i)

    # Set pen color to green
    t.pencolor("green")

    # Draw circle
    t.circle(50)

    # Lift pen and move to next position
    t.penup()
    t.goto(0, -i * 10)
    t.pendown()

# Keep window open until closed manually
turtle.done()
