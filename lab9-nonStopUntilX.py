import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightgray")
screen.listen()  # Enable key press listener

# Function to handle user exit
def stop_drawing(key):
  if key.upper() == "X":
    screen.bye()  # Close the screen

screen.onkeypress(stop_drawing, "x")  # Bind 'x' or 'X' to stop_drawing

# Create a circle turtle
circle = turtle.Turtle()

# Set speed for animation
circle.speed(0)  # Adjust for desired animation speed

circle.shape("circle")
circle.penup()
circle.goto(random.randint(-screen.window_width() // 2, screen.window_width() // 2),
             random.randint(-screen.window_height() // 2, screen.window_height() // 2))
circle.pendown()
circle.pensize(2)

def move_circle():
  # Randomly choose direction and distance
  direction = random.randint(0, 360)
  distance = random.randint(10, 30)

  # Set heading and move circle
  circle.setheading(direction)
  circle.forward(distance)

  # Check if circle reaches the edge and bounce back
  if circle.xcor() > screen.window_width() / 2 - 10 or circle.xcor() < -screen.window_width() / 2 + 10:
    circle.setheading(180 - circle.heading())  # Bounce horizontally
  if circle.ycor() > screen.window_height() / 2 - 10 or circle.ycor() < -screen.window_height() / 2 + 10:
    circle.setheading(360 - circle.heading())  # Bounce vertically

  # Set random color
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)
  circle.pencolor(f"#{red:02x}{green:02x}{blue:02x}")

# Keep updating the animation
while True:
  screen.update()
  move_circle()

# Exit on screen close (in case user closes window)
screen.exitonclick()
