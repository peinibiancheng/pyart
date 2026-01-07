"""
Sol LeWitt-inspired geometric line drawing using Python's turtle module.
Homage to Sol LeWitt's 'Wall Drawing' series focusing on line arrangement, 
overlap, and direction.

Usage:
    python sol_lewitt.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle)

Features:
    - Canvas divided into four quadrants
    - Quadrant 1 (top-right): Vertical lines
    - Quadrant 2 (top-left): Horizontal lines
    - Quadrant 3 (bottom-left): Diagonal lines (45° left tilt)
    - Quadrant 4 (bottom-right): Diagonal lines (45° right tilt)
    - Lines maintain strict equal spacing (10 pixels)
    - Simple color palette: black and primary colors
    - Precise mathematical calculation for line placement
"""

import turtle


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
    t.speed(0)  # Fastest drawing speed
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
    
    # Quadrant 3: Bottom-left - Diagonal lines 45° left (yellow)
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
    # For 45° left diagonal, we need lines from bottom-left to top-right within the quadrant
    # The lines run from lower-left to upper-right (slope = 1)
    
    # Calculate adjusted spacing for diagonal lines
    # For 45° diagonals, perpendicular spacing = spacing * sqrt(2) / 2, but we'll use direct spacing
    diagonal_spacing = int(spacing * 1.414)  # Adjust spacing for visual consistency
    
    # Draw diagonals starting from the left edge
    for offset in range(-quadrant_size, quadrant_size, diagonal_spacing):
        t.penup()
        # Start point on left edge or bottom edge
        if offset < -quadrant_size:
            start_x = -quadrant_size
            start_y = offset + quadrant_size
        else:
            start_x = offset - quadrant_size
            start_y = -quadrant_size
        
        # End point on top edge or right edge (x=0)
        if offset < 0:
            end_x = offset
            end_y = 0
        else:
            end_x = 0
            end_y = offset - quadrant_size
        
        # Only draw if line is within quadrant 3
        if start_x >= -quadrant_size and start_y >= -quadrant_size:
            t.goto(start_x, start_y)
            t.pendown()
            # Draw to the endpoint, clipping at quadrant boundaries
            if end_x <= 0 and end_y <= 0:
                t.goto(end_x, end_y)
            elif end_x > 0:
                # Clip at x=0
                clip_y = start_y + (0 - start_x)
                t.goto(0, clip_y)
            elif end_y > 0:
                # Clip at y=0
                clip_x = start_x + (0 - start_y)
                t.goto(clip_x, 0)


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
    # For 45° right diagonal, we need lines from top-left to bottom-right within the quadrant
    # The lines run from upper-left to lower-right (slope = -1)
    
    # Calculate adjusted spacing for diagonal lines
    diagonal_spacing = int(spacing * 1.414)  # Adjust spacing for visual consistency
    
    # Draw diagonals starting from various positions
    for offset in range(-quadrant_size, quadrant_size, diagonal_spacing):
        t.penup()
        # Start point on left edge (x=0) or top edge (y=0)
        if offset < 0:
            start_x = 0
            start_y = -offset
        else:
            start_x = offset
            start_y = 0
        
        # End point on bottom edge or right edge
        if offset < 0:
            end_x = -offset
            end_y = -quadrant_size
        else:
            end_x = quadrant_size
            end_y = -(quadrant_size - offset)
        
        # Only draw if line is within quadrant 4
        if start_x <= quadrant_size and start_y >= -quadrant_size:
            t.goto(start_x, start_y)
            t.pendown()
            # Draw to the endpoint, clipping at quadrant boundaries
            if end_x <= quadrant_size and end_y >= -quadrant_size:
                t.goto(end_x, end_y)
            elif end_x > quadrant_size:
                # Clip at x=quadrant_size
                clip_y = start_y - (quadrant_size - start_x)
                t.goto(quadrant_size, clip_y)
            elif end_y < -quadrant_size:
                # Clip at y=-quadrant_size
                clip_x = start_x + (start_y + quadrant_size)
                t.goto(clip_x, -quadrant_size)


if __name__ == "__main__":
    draw_sol_lewitt()
