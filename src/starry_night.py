"""
Van Gogh 'Starry Night'-inspired artwork using Python's turtle module.
Generates swirling sky patterns, cypress trees, and a glowing moon.

Usage:
    python starry_night.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, math, random)

Features:
    - Swirling sky patterns using sine/cosine waves (mimicking brushstrokes)
    - Stylized black cypress trees (flame-like) in foreground
    - Glowing yellow moon with soft halos
    - Color palette: #1a5fb4 (blue), #f7931a (orange/yellow), and black
"""

import turtle
import math
import random


def draw_starry_night():
    """
    Generate a Van Gogh 'Starry Night'-inspired artwork.
    
    Creates:
    - Swirling sky patterns using sine/cosine waves (mimicking brushstrokes)
    - Stylized black cypress trees (flame-like) in foreground
    - Glowing yellow moon with soft halos
    - Color palette: #1a5fb4 (blue), #f7931a (orange/yellow), and black
    """
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")  # Black night sky background from palette
    screen.title("Starry Night - Van Gogh Inspired")
    screen.tracer(2)  # Update screen every 10th drawing action for moderate speed


    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()
    
    # Draw sky with swirling patterns
    draw_swirling_sky(t)
    
    # Draw moon with halos
    draw_moon_with_halos(t)
    
    # Draw stars
    draw_stars(t)
    
    # Draw cypress trees in foreground
    draw_cypress_trees(t)
    
    # Finish
    screen.update()
    turtle.done()


def draw_swirling_sky(t):
    """Draw swirling sky patterns using sine/cosine waves."""
    t.pensize(2)
    
    # Create multiple swirling patterns across the sky
    for row in range(-250, 150, 30):
        for start_x in range(-400, 400, 100):
            draw_swirl_line(t, start_x, row)


def draw_swirl_line(t, start_x, start_y):
    """Draw a single swirling line using sine wave."""
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    
    # Use blue color for sky swirls (visible against black background)
    t.pencolor("#1a5fb4")
    
    # Draw sinusoidal swirl
    for i in range(100):
        x = start_x + i
        # Use sine wave for vertical displacement
        y = start_y + 15 * math.sin(i * 0.2) + 5 * math.cos(i * 0.3)
        t.goto(x, y)


def draw_moon_with_halos(t):
    """Draw a glowing yellow moon with soft halos."""
    moon_x, moon_y = 200, 150
    
    # Draw halos (multiple circles of same color for glow effect)
    halo_sizes = [60, 50, 40, 30]
    
    for size in halo_sizes:
        t.penup()
        t.goto(moon_x, moon_y - size)
        t.pendown()
        t.pencolor("#f7931a")
        t.fillcolor("#f7931a")
        t.begin_fill()
        t.circle(size)
        t.end_fill()
    
    # Draw bright moon center (using same yellow/orange color)
    t.penup()
    t.goto(moon_x, moon_y - 20)
    t.pendown()
    t.pencolor("#f7931a")
    t.fillcolor("#f7931a")
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def draw_stars(t):
    """Draw small stars scattered across the sky."""
    random.seed(42)  # For reproducibility
    
    t.pensize(1)
    
    # Draw stars at various positions (ensure exactly 30 stars)
    star_positions = []
    while len(star_positions) < 30:
        x = random.randint(-380, 380)
        y = random.randint(-200, 250)
        # Avoid moon area
        if not (180 < x < 220 and 120 < y < 180):
            star_positions.append((x, y))
    
    for x, y in star_positions:
        draw_star(t, x, y)


def draw_star(t, x, y):
    """Draw a single star with radiating lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("#f7931a")
    
    # Draw star as radiating lines
    for angle in range(0, 360, 45):
        t.setheading(angle)
        t.forward(5)
        t.backward(5)


def draw_cypress_trees(t):
    """Draw stylized flame-like cypress trees in the foreground."""
    # Left cypress tree
    draw_cypress_tree(t, -350, -300, 200)
    
    # Right cypress tree (smaller)
    draw_cypress_tree(t, -250, -300, 150)


def draw_cypress_tree(t, x, y, height):
    """Draw a single flame-like cypress tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    
    # Draw flame-like shape using curved path
    t.setheading(90)  # Point upward
    
    # Left side of tree (with curves)
    for i in range(20):
        angle = math.sin(i * 0.3) * 10
        t.setheading(90 + angle)
        t.forward(height / 20)
    
    # Top point
    t.setheading(90)
    t.forward(height * 0.15)
    
    # Right side of tree (with curves, mirrored)
    t.setheading(-90)
    t.forward(height * 0.15)
    
    for i in range(20):
        angle = math.sin((19 - i) * 0.3) * 10
        t.setheading(-90 - angle)
        t.forward(height / 20)
    
    # Close the shape
    t.goto(x, y)
    t.end_fill()
    
    # Add some texture lines to the tree
    draw_tree_texture(t, x, y, height)


def draw_tree_texture(t, x, y, height):
    """Add texture lines to cypress tree to enhance flame-like appearance."""
    t.pencolor("black")
    t.pensize(2)
    
    # Draw wavy lines inside the tree
    for offset in [-5, 0, 5]:
        t.penup()
        t.goto(x + offset, y + height * 0.2)
        t.pendown()
        
        for i in range(int(height * 0.06)):
            curve = math.sin(i * 0.5) * 3
            t.goto(x + offset + curve, y + height * 0.2 + i * 10)


if __name__ == "__main__":
    try:
        draw_starry_night()
    except turtle.Terminator:
        pass
    except Exception as e:
        if "invalid command name" in str(e):
            pass
        else:
            raise
