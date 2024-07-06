import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

# Sun turtle
sun = turtle.Turtle()
sun.speed(1)  # Faster speed for animation
sun.shape("circle")
sun.penup()
sun.goto(0, -250)
sun_colors = ["red", "orange", "yellow"]  # List of sun colors

while True:
  screen.update()
  # Move sun up and change color
  sun.forward(5)
  if sun.ycor() > screen.window_height() / 2:
    sun.penup()
    sun.goto(0, -250)
    sun.pendown()
  index = sun.color()[0]  # Get current color index
  sun.color(sun_colors[(index + 1) % len(sun_colors)])  # Cycle through colors

screen.exitonclick()
