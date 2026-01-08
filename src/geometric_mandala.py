"""
Geometric Mandala artwork using Python's turtle module.
Creates intricate circular patterns with mathematical precision.

Usage:
    python geometric_mandala.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, math)

Features:
    - Circular mandala pattern with recursive geometry
    - Multiple layers of symmetric designs
    - Vibrant color gradients
    - Mathematical precision and symmetry
    - Color palette: #9141ac (purple), #e01b24 (red), #26a269 (green), #1c71d8 (blue)
"""

import turtle
import math


def draw_geometric_mandala():
    """
    Generate a geometric mandala artwork.
    
    Creates:
    - Multiple concentric layers of geometric patterns
    - Radial symmetry with 12-fold rotation
    - Flower-like petals and star shapes
    - Gradient-like color transitions
    - Color palette: purple (#9141ac), red (#e01b24), green (#26a269), blue (#1c71d8)
    """
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Geometric Mandala")
    screen.tracer(1)  # Use batch rendering for speed (draws 10 actions per frame)
    
    t = turtle.Turtle()
    t.speed(20)  # Fastest drawing speed

    t.hideturtle()
    
    # Center the drawing
    center_x, center_y = 0, 0
    
    # Draw multiple layers from outside to inside
    draw_outer_ring(t, center_x, center_y)
    draw_star_layer(t, center_x, center_y)
    draw_petal_layer(t, center_x, center_y)
    draw_inner_circles(t, center_x, center_y)
    draw_center_flower(t, center_x, center_y)
    
    # Finish
    screen.update()
    turtle.done()


def draw_outer_ring(t, cx, cy):
    """Draw the outermost ring with decorative elements."""
    radius = 280
    num_segments = 36
    
    t.pensize(3)
    
    for i in range(num_segments):
        angle = i * (360 / num_segments)
        
        # Calculate position
        x = cx + radius * math.cos(math.radians(angle))
        y = cy + radius * math.sin(math.radians(angle))
        
        # Draw small decorative circle
        t.penup()
        t.goto(x, y - 10)
        t.pendown()
        
        # Alternate colors
        if i % 3 == 0:
            color = "#9141ac"
        elif i % 3 == 1:
            color = "#e01b24"
        else:
            color = "#1c71d8"
        
        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        
        # Draw line to center
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(1)
        t.pencolor(color)
        
        inner_x = cx + (radius * 0.85) * math.cos(math.radians(angle))
        inner_y = cy + (radius * 0.85) * math.sin(math.radians(angle))
        t.goto(inner_x, inner_y)


def draw_star_layer(t, cx, cy):
    """Draw star-shaped layer."""
    radius = 220
    num_points = 12
    
    t.pensize(2)
    
    for i in range(num_points):
        angle = i * (360 / num_points)
        
        # Outer point
        outer_x = cx + radius * math.cos(math.radians(angle))
        outer_y = cy + radius * math.sin(math.radians(angle))
        
        # Inner point (between outer points)
        inner_angle = angle + (360 / num_points / 2)
        inner_radius = radius * 0.6
        inner_x = cx + inner_radius * math.cos(math.radians(inner_angle))
        inner_y = cy + inner_radius * math.sin(math.radians(inner_angle))
        
        # Draw triangle
        if i == 0:
            t.penup()
            t.goto(outer_x, outer_y)
            t.pendown()
        
        t.pencolor("#26a269")
        t.fillcolor("#26a269")
        
        if i == 0:
            t.begin_fill()
        
        # Create star point
        next_angle = (i + 1) * (360 / num_points)
        next_outer_x = cx + radius * math.cos(math.radians(next_angle))
        next_outer_y = cy + radius * math.sin(math.radians(next_angle))
        
        t.goto(inner_x, inner_y)
        t.goto(next_outer_x, next_outer_y)
        
        if i == num_points - 1:
            # Close the shape
            first_x = cx + radius * math.cos(math.radians(0))
            first_y = cy + radius * math.sin(math.radians(0))
            t.goto(first_x, first_y)
            t.end_fill()


def draw_petal_layer(t, cx, cy):
    """Draw flower petal layer."""
    radius = 150
    num_petals = 12
    petal_size = 60
    
    for i in range(num_petals):
        angle = i * (360 / num_petals)
        
        # Calculate petal center
        x = cx + radius * math.cos(math.radians(angle))
        y = cy + radius * math.sin(math.radians(angle))
        
        draw_petal(t, x, y, petal_size, angle)


def draw_petal(t, x, y, size, rotation):
    """Draw a single flower petal."""
    t.penup()
    t.goto(x, y)
    t.setheading(rotation)
    t.pendown()
    
    t.pencolor("#e01b24")
    t.fillcolor("#e01b24")
    t.begin_fill()
    
    # Draw petal using curves
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    
    t.end_fill()


def draw_inner_circles(t, cx, cy):
    """Draw concentric circles in the middle."""
    radii = [100, 80, 60]
    colors = ["#9141ac", "#1c71d8", "#26a269"]
    
    for radius, color in zip(radii, colors):
        t.penup()
        t.goto(cx, cy - radius)
        t.pendown()
        
        t.pencolor(color)
        t.fillcolor(color)
        t.pensize(3)
        
        t.begin_fill()
        t.circle(radius)
        t.end_fill()


def draw_center_flower(t, cx, cy):
    """Draw the central flower design."""
    num_petals = 8
    petal_radius = 40
    
    for i in range(num_petals):
        angle = i * (360 / num_petals)
        
        # Calculate position for petal center
        offset = 25
        x = cx + offset * math.cos(math.radians(angle))
        y = cy + offset * math.sin(math.radians(angle))
        
        # Draw small petal
        t.penup()
        t.goto(x, y - petal_radius / 2)
        t.pendown()
        
        t.pencolor("#f6d32d")
        t.fillcolor("#f6d32d")
        t.begin_fill()
        t.circle(petal_radius / 2)
        t.end_fill()
    
    # Draw center circle
    t.penup()
    t.goto(cx, cy - 15)
    t.pendown()
    
    t.pencolor("#e01b24")
    t.fillcolor("#e01b24")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    # Draw very center dot
    t.penup()
    t.goto(cx, cy - 5)
    t.pendown()
    
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(5)
    t.end_fill()


if __name__ == "__main__":
    try:
        draw_geometric_mandala()
    except turtle.Terminator:
        pass
    except Exception as e:
        if "invalid command name" in str(e):
            pass
        else:
            raise
