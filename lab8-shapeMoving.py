import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightgray")

# Create two turtles for the circles
circle1 = turtle.Turtle()
circle2 = turtle.Turtle()

# Set speeds for animation
circle1.speed(0)  # Faster speed (adjust for desired animation speed)
circle2.speed(0)

# Circle 1 properties
circle1.shape("circle")
circle1.color("red")
circle1.penup()
circle1.goto(0, 300)  # Start at top
circle1.pendown()
circle1.pensize(3)
radius1 = 50

# Circle 2 properties
circle2.shape("circle")
circle2.color("blue")
circle2.penup()
circle2.goto(400, 0)  # Start at right
circle2.pendown()
circle2.pensize(2)
radius2 = 30

def move_circles():
  # Move circle 1 diagonally towards center
  circle1.setheading(225)  # Angle for diagonal movement
  circle1.forward(radius1 + 2)  # Move with circle radius + offset

  # Check if circle 1 reaches bottom left corner
  if circle1.xcor() < -screen.window_width() / 2 and circle1.ycor() < -screen.window_height() / 2:
    # Reposition at top right corner
    circle1.penup()
    circle1.goto(screen.window_width() / 2, screen.window_height() / 2)
    circle1.pendown()

  # Move circle 2 diagonally towards center
  circle2.setheading(315)  # Angle for diagonal movement
  circle2.forward(radius2 + 2)  # Move with circle radius + offset

  # Check if circle 2 reaches bottom right corner
  if circle2.xcor() > screen.window_width() / 2 and circle2.ycor() < -screen.window_height() / 2:
    # Reposition at top left corner
    circle2.penup()
    circle2.goto(-screen.window_width() / 2, screen.window_height() / 2)
    circle2.pendown()

# Keep updating the animation
while True:
  screen.update()
  move_circles()

# Exit on screen close
screen.exitonclick()
