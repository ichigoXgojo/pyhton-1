import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle (optional, for visualization)
t.speed(1) 

# Define the side length of the square
side_length = 100

# Draw the square using a loop
for _ in range(4):  # A square has 4 sides
    t.forward(side_length)  # Move the turtle forward by the side length
    t.left(90)              # Turn the turtle left by 90 degrees

# Keep the window open until closed manually
turtle.done() 
