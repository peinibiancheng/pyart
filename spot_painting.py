"""
Damien Hirst 'Spot Paintings'-inspired artwork using Python's turtle module.
Generates a grid of colorful circles with pop art aesthetics.

Usage:
    python spot_painting.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, random)

Features:
    - 10x10 grid of perfectly aligned colored spots
    - High-saturation pop art color palette
    - Consistent spacing and centering
    - Clean, minimal aesthetic with no borders
"""

import turtle
import random


def draw_spot_painting():
    """
    Generate a Damien Hirst 'Spot Paintings'-inspired artwork.
    
    Creates a 10x10 grid of colorful circles with:
    - High-saturation pop art colors randomly selected for each spot
    - Perfect grid alignment with consistent spacing
    - Centered composition on a white canvas
    """
    # Canvas setup: 600x600 white background
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Spot Painting - Damien Hirst Inspired")
    
    # Turtle setup: fastest speed for efficiency
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    
    # High-saturation pop art color palette (RGB hex codes)
    # Colors inspired by Damien Hirst's vibrant, bold aesthetic
    colors = [
        "#FF0000",  # Bright Red
        "#00BFFF",  # Deep Sky Blue
        "#FFD700",  # Gold/Bright Yellow
        "#00FF00",  # Lime Green
        "#FF1493",  # Deep Pink/Magenta
        "#FF4500",  # Orange Red
        "#9400D3",  # Dark Violet/Purple
        "#00CED1",  # Dark Turquoise
        "#FF69B4",  # Hot Pink
        "#32CD32",  # Lime Green (variant)
        "#FF6347",  # Tomato Red
        "#4169E1",  # Royal Blue
        "#FFFF00",  # Pure Yellow
        "#FF00FF",  # Magenta/Fuchsia
        "#00FA9A",  # Medium Spring Green
    ]
    
    # Grid configuration
    rows = 10  # Number of rows in the grid
    cols = 10  # Number of columns in the grid
    spot_diameter = 20  # Diameter of each circle in pixels
    spot_radius = spot_diameter / 2  # Radius for turtle.circle()
    spacing = 50  # Distance between center points of adjacent circles
    
    # Calculate starting position to center the grid on canvas
    # Grid dimensions: (cols - 1) * spacing gives total width of grid
    # We want the grid centered, so we calculate offset from center (0, 0)
    grid_width = (cols - 1) * spacing
    grid_height = (rows - 1) * spacing
    start_x = -grid_width / 2  # Left edge of grid (centered horizontally)
    start_y = grid_height / 2   # Top edge of grid (centered vertically)
    
    # Disable border/outline for clean aesthetic
    t.penup()  # Never draw lines between spots
    
    # Nested loops to create 10x10 grid
    for row in range(rows):
        for col in range(cols):
            # Calculate coordinates for current spot
            # x: start from left edge, move right by col * spacing
            # y: start from top edge, move down by row * spacing
            x = start_x + col * spacing
            y = start_y - row * spacing
            
            # Position turtle at spot location
            # Note: turtle.circle() draws from the bottom of the circle
            # so we offset y by radius to center the circle at (x, y)
            t.goto(x, y - spot_radius)
            
            # Select random color from palette for this spot
            color = random.choice(colors)
            t.fillcolor(color)
            
            # Draw filled circle with no border
            t.begin_fill()
            t.circle(spot_radius)
            t.end_fill()
    
    # Hide turtle arrow for clean final presentation
    t.hideturtle()
    
    # Keep window open
    screen.update()
    turtle.done()


if __name__ == "__main__":
    draw_spot_painting()
