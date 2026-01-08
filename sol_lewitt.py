"""
Sol LeWitt-inspired geometric line drawing using Python's turtle module.
Homage to Sol LeWitt's 'Wall Drawing' series focusing on line arrangement, 
overlap, and direction.

Usage:
    python sol_lewitt.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, math)

Features:
    - Canvas divided into four quadrants
    - Quadrant 1 (top-right): Vertical lines
    - Quadrant 2 (top-left): Horizontal lines
    - Quadrant 3 (bottom-left): Diagonal lines (45° left tilt)
    - Quadrant 4 (bottom-right): Diagonal lines (45° right tilt)
    - Lines maintain strict equal spacing (10 pixels for vertical/horizontal,
      14 pixels for diagonals to maintain consistent visual density)
    - Simple color palette: black and primary colors
    - Precise mathematical calculation for line placement
"""

import math
import turtle


# Constant for diagonal line spacing adjustment (sqrt(2))
SQRT_2 = math.sqrt(2)


def draw_sol_lewitt():
    """
    Generate a Sol LeWitt-inspired geometric line drawing.
    
    Creates a canvas divided into four quadrants, each filled with lines
    in different orientations:
    - Quadrant 1 (top-right): Vertical lines
    - Quadrant 2 (top-left): Horizontal lines
    - Quadrant 3 (bottom-left): Diagonal lines (45° left tilt)
    - Quadrant 4 (bottom-right): Diagonal lines (45° right tilt)
    """
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Sol LeWitt - Wall Drawing Inspired")
    
    t = turtle.Turtle()
    t.speed(20)  # Fastest drawing speed
    t.hideturtle()
    
    # Define quadrant dimensions
    # Canvas is 800x800, so each quadrant is 400x400
    quadrant_size = 400
    line_spacing = 10
    
    # Draw dividing lines to separate quadrants
    draw_dividing_lines(t, quadrant_size)
    
    # Draw lines in each quadrant
    # Quadrant 1: Top-right - Vertical lines (red)
    draw_vertical_lines(t, quadrant_size, line_spacing, color="red")
    
    # Quadrant 2: Top-left - Horizontal lines (blue)
    draw_horizontal_lines(t, quadrant_size, line_spacing, color="blue")
    
    # Quadrant 3: Bottom-left - Diagonal lines 45° left (gold)
    draw_diagonal_left_lines(t, quadrant_size, line_spacing, color="#FFD700")
    
    # Quadrant 4: Bottom-right - Diagonal lines 45° right (black)
    draw_diagonal_right_lines(t, quadrant_size, line_spacing, color="black")
    
    # Finish
    screen.update()
    turtle.done()


def draw_dividing_lines(t, quadrant_size):
    """Draw dividing lines to separate the four quadrants."""
    t.pensize(2)
    t.pencolor("black")
    
    # Draw horizontal dividing line
    t.penup()
    t.goto(-quadrant_size, 0)
    t.pendown()
    t.goto(quadrant_size, 0)
    
    # Draw vertical dividing line
    t.penup()
    t.goto(0, -quadrant_size)
    t.pendown()
    t.goto(0, quadrant_size)


def draw_vertical_lines(t, quadrant_size, spacing, color):
    """
    Draw vertical lines in quadrant 1 (top-right).
    
    Args:
        t: Turtle object
        quadrant_size: Size of each quadrant
        spacing: Distance between lines
        color: Color of the lines
    """
    t.pensize(1)
    t.pencolor(color)
    
    # Quadrant 1 boundaries: x from 0 to quadrant_size, y from 0 to quadrant_size
    for x in range(spacing, quadrant_size, spacing):
        t.penup()
        t.goto(x, 0)
        t.pendown()
        t.goto(x, quadrant_size)


def draw_horizontal_lines(t, quadrant_size, spacing, color):
    """
    Draw horizontal lines in quadrant 2 (top-left).
    
    Args:
        t: Turtle object
        quadrant_size: Size of each quadrant
        spacing: Distance between lines
        color: Color of the lines
    """
    t.pensize(1)
    t.pencolor(color)
    
    # Quadrant 2 boundaries: x from -quadrant_size to 0, y from 0 to quadrant_size
    for y in range(spacing, quadrant_size, spacing):
        t.penup()
        t.goto(-quadrant_size, y)
        t.pendown()
        t.goto(0, y)


def draw_diagonal_left_lines(t, quadrant_size, spacing, color):
    """
    Draw diagonal lines tilted 45° to the left in quadrant 3 (bottom-left).
    
    Args:
        t: Turtle object
        quadrant_size: Size of each quadrant
        spacing: Distance between lines
        color: Color of the lines
    """
    t.pensize(1)
    t.pencolor(color)
    
    # Quadrant 3 boundaries: x from -quadrant_size to 0, y from -quadrant_size to 0
    # For 45° left diagonal, draw lines with slope 1 (from lower-left to upper-right)
    
    # Calculate adjusted spacing for diagonal lines
    # Using spacing * sqrt(2) to maintain consistent visual density across all quadrants
    diagonal_spacing = round(spacing * SQRT_2)
    
    # Draw parallel diagonal lines
    # Strategy: Start from points along the bottom and left edges,
    # draw upward at 45° until hitting the top or right edge
    for offset in range(0, quadrant_size * 2, diagonal_spacing):
        t.penup()
        
        # Determine start and end points
        if offset < quadrant_size:
            # Start on bottom edge, move left to right
            start_x = -quadrant_size + offset
            start_y = -quadrant_size
            # Move up-right at 45° for distance = min(quadrant_size, remaining space)
            distance = min(quadrant_size, quadrant_size - offset)
            end_x = start_x + distance
            end_y = start_y + distance
        else:
            # Start on left edge, move bottom to top
            start_x = -quadrant_size
            start_y = -quadrant_size + (offset - quadrant_size)
            # Move up-right at 45° until hitting top or right edge
            distance = min(quadrant_size, quadrant_size - (offset - quadrant_size))
            end_x = start_x + distance
            end_y = start_y + distance
        
        # Draw the line
        t.goto(start_x, start_y)
        t.pendown()
        t.goto(end_x, end_y)


def draw_diagonal_right_lines(t, quadrant_size, spacing, color):
    """
    Draw diagonal lines tilted 45° to the right in quadrant 4 (bottom-right).
    
    Args:
        t: Turtle object
        quadrant_size: Size of each quadrant
        spacing: Distance between lines
        color: Color of the lines
    """
    t.pensize(1)
    t.pencolor(color)
    
    # Quadrant 4 boundaries: x from 0 to quadrant_size, y from -quadrant_size to 0
    # For 45° right diagonal, draw lines with slope -1 (from upper-left to lower-right)
    
    # Calculate adjusted spacing for diagonal lines
    # Using spacing * sqrt(2) to maintain consistent visual density across all quadrants
    diagonal_spacing = round(spacing * SQRT_2)
    
    # Draw parallel diagonal lines
    # Strategy: Start from points along the top and left edges,
    # draw downward at 45° until hitting the bottom or right edge
    for offset in range(0, quadrant_size * 2, diagonal_spacing):
        t.penup()
        
        # Determine start and end points
        if offset < quadrant_size:
            # Start on top edge, move left to right
            start_x = offset
            start_y = 0
            # Move down-right at 45° for distance = min(quadrant_size, remaining space)
            distance = min(quadrant_size, quadrant_size - offset)
            end_x = start_x + distance
            end_y = start_y - distance
        else:
            # Start on left edge, move top to bottom
            start_x = 0
            start_y = -(offset - quadrant_size)
            # Move down-right at 45° until hitting bottom or right edge
            distance = min(quadrant_size, quadrant_size - (offset - quadrant_size))
            end_x = start_x + distance
            end_y = start_y - distance
        
        # Draw the line
        t.goto(start_x, start_y)
        t.pendown()
        t.goto(end_x, end_y)


if __name__ == "__main__":
    try:
        draw_sol_lewitt()
    except turtle.Terminator:
        pass
    except Exception as e:
        # Handle case where window is closed during drawing (TclError)
        if "invalid command name" in str(e):
            pass
        else:
            raise

