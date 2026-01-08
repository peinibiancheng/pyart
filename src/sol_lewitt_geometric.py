"""
Sol LeWitt-inspired geometric artwork using Python's turtle module.
Generates overlapping geometric shapes filled with parallel hatch lines.

Usage:
    python sol_lewitt_geometric.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, random)

Features:
    - Multiple overlapping geometric shapes (squares, triangles, circles)
    - Hatch line filling instead of solid colors
    - Sol LeWitt's color palette: red, yellow, blue, black (high saturation)
    - Randomized stacking order and line density for each run
    - Fast rendering with tracer(0)
"""

import turtle
import random


def draw_sol_lewitt_art():
    """
    Generate a Sol LeWitt-inspired geometric artwork.
    
    Creates:
    - Overlapping geometric shapes with hatch line fills
    - Random stacking order and line density
    - Color palette: vibrant red, yellow, blue, and black
    """
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Sol LeWitt - Geometric Hatch Lines")
    screen.tracer(2)  # Update screen every 2nd drawing action

    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Sol LeWitt color palette (high saturation)
    colors = [
        "#FF0000",  # Vibrant red
        "#FFFF00",  # Vibrant yellow
        "#0000FF",  # Vibrant blue
        "#000000"   # Black
    ]
    
    # Generate random shapes with random parameters
    num_shapes = random.randint(6, 10)
    shapes = []
    
    for _ in range(num_shapes):
        shape_type = random.choice(['square', 'triangle', 'circle'])
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(80, 200)
        color = random.choice(colors)
        line_density = random.randint(3, 8)  # Random line spacing
        angle = random.randint(0, 3) * 45  # Hatch line angle (0, 45, 90, 135)
        
        shapes.append({
            'type': shape_type,
            'x': x,
            'y': y,
            'size': size,
            'color': color,
            'density': line_density,
            'angle': angle
        })
    
    # Randomize stacking order
    random.shuffle(shapes)
    
    # Draw all shapes
    for shape in shapes:
        draw_shape_with_hatching(t, shape)
    
    # Finish
    screen.update()
    turtle.done()


def draw_shape_with_hatching(t, shape):
    """
    Draw a geometric shape filled with parallel hatch lines.
    
    Args:
        t: Turtle object
        shape: Dictionary with shape parameters
    """
    if shape['type'] == 'square':
        draw_square_hatched(t, shape['x'], shape['y'], shape['size'], 
                           shape['color'], shape['density'], shape['angle'])
    elif shape['type'] == 'triangle':
        draw_triangle_hatched(t, shape['x'], shape['y'], shape['size'], 
                             shape['color'], shape['density'], shape['angle'])
    elif shape['type'] == 'circle':
        draw_circle_hatched(t, shape['x'], shape['y'], shape['size'], 
                           shape['color'], shape['density'], shape['angle'])


def draw_square_hatched(t, x, y, size, color, density, angle):
    """Draw a square outline filled with parallel hatch lines."""
    # Draw outline
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.pensize(3)
    
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    # Draw hatch lines
    draw_hatch_in_square(t, x, y, size, color, density, angle)


def draw_triangle_hatched(t, x, y, size, color, density, angle):
    """Draw an equilateral triangle outline filled with parallel hatch lines."""
    # Draw outline
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.pensize(3)
    
    for _ in range(3):
        t.forward(size)
        t.left(120)
    
    # Draw hatch lines
    draw_hatch_in_triangle(t, x, y, size, color, density, angle)


def draw_circle_hatched(t, x, y, size, color, density, angle):
    """Draw a circle outline filled with parallel hatch lines."""
    radius = size / 2
    
    # Circle will be centered at (x + radius, y + radius)
    # turtle.circle() draws from the bottom of the circle when heading is 90
    center_x = x + radius
    center_y = y + radius
    
    # Draw outline
    t.penup()
    t.goto(center_x, center_y - radius)
    t.pendown()
    t.pencolor(color)
    t.pensize(3)
    t.setheading(90)
    t.circle(radius)
    
    # Draw hatch lines
    draw_hatch_in_circle(t, center_x, center_y, radius, color, density, angle)


def draw_hatch_in_square(t, x, y, size, color, density, angle):
    """Fill a square with parallel hatch lines."""
    t.pensize(1)
    t.pencolor(color)
    
    # Determine line spacing based on density
    spacing = density
    
    # Calculate the diagonal length for proper coverage when rotated
    # Using 1.5 * size ensures diagonal lines extend beyond square boundaries
    # (actual diagonal is sqrt(2) * size ≈ 1.414, but 1.5 provides margin)
    diagonal = size * 1.5
    
    # Save original position
    t.penup()
    
    # Draw lines at specified angle
    if angle == 0:  # Horizontal lines
        y_pos = y
        while y_pos <= y + size:
            t.goto(x, y_pos)
            t.pendown()
            t.goto(x + size, y_pos)
            t.penup()
            y_pos += spacing
    elif angle == 90:  # Vertical lines
        x_pos = x
        while x_pos <= x + size:
            t.goto(x_pos, y)
            t.pendown()
            t.goto(x_pos, y + size)
            t.penup()
            x_pos += spacing
    elif angle == 45:  # Diagonal lines (bottom-left to top-right)
        # Draw lines parallel to diagonal from bottom-left to top-right
        for offset in range(-size, size + 1, spacing):
            points = []
            
            # Check intersection with bottom edge (y = y)
            if 0 <= offset <= size:
                points.append((x + offset, y))
            
            # Check intersection with left edge (x = x)
            if 0 <= -offset <= size:
                points.append((x, y - offset))
            
            # Check intersection with top edge (y = y + size)
            if 0 <= offset - size <= size:
                points.append((x + offset - size, y + size))
            
            # Check intersection with right edge (x = x + size)
            if 0 <= size - offset <= size:
                points.append((x + size, y + size - offset))
            
            # Draw line between valid intersection points (should be exactly 2)
            if len(points) >= 2:
                t.goto(points[0][0], points[0][1])
                t.pendown()
                t.goto(points[-1][0], points[-1][1])
                t.penup()
    elif angle == 135:  # Diagonal lines (top-left to bottom-right)
        # Draw lines parallel to diagonal from top-left to bottom-right
        # For lines with slope -1, we parameterize as: x - y = offset
        for offset in range(-size, size + 1, spacing):
            points = []
            
            # Check intersection with left edge (x = x_origin)
            # When x = x_origin, y = x_origin - offset
            y_left = x - offset
            if y <= y_left <= y + size:
                points.append((x, y_left))
            
            # Check intersection with top edge (y = y_origin + size)
            # When y = y_origin + size, x = y_origin + size + offset
            x_top = y + size + offset
            if x <= x_top <= x + size:
                points.append((x_top, y + size))
            
            # Check intersection with right edge (x = x_origin + size)
            # When x = x_origin + size, y = x_origin + size - offset
            y_right = x + size - offset
            if y <= y_right <= y + size:
                points.append((x + size, y_right))
            
            # Check intersection with bottom edge (y = y_origin)
            # When y = y_origin, x = y_origin + offset
            x_bottom = y + offset
            if x <= x_bottom <= x + size:
                points.append((x_bottom, y))
            
            # Draw line between valid intersection points (should be exactly 2)
            if len(points) >= 2:
                t.goto(points[0][0], points[0][1])
                t.pendown()
                t.goto(points[-1][0], points[-1][1])
                t.penup()


def draw_hatch_in_triangle(t, x, y, size, color, density, angle):
    """Fill an equilateral triangle with parallel hatch lines."""
    t.pensize(1)
    t.pencolor(color)
    
    spacing = density
    
    # Calculate triangle vertices
    # Starting from (x, y), going counterclockwise
    v1 = (x, y)
    v2 = (x + size, y)
    v3 = (x + size/2, y + size * 0.866)  # height of equilateral triangle
    
    t.penup()
    
    # Horizontal hatching for triangles (angle parameter ignored for simplicity)
    # All angles simplified to horizontal lines for cleaner visual result with triangular shapes
    # This is an intentional design choice to maintain visual clarity
    y_pos = y
    while y_pos <= v3[1]:
        # Calculate line intersections with triangle edges
        # Left edge: from v1 to v3
        # Right edge: from v2 to v3
        
        progress = (y_pos - y) / (v3[1] - y) if (v3[1] - y) != 0 else 0
        progress = max(0, min(1, progress))
        
        x_left = v1[0] + (v3[0] - v1[0]) * progress
        x_right = v2[0] + (v3[0] - v2[0]) * progress
        
        if x_left <= x_right:
            t.goto(x_left, y_pos)
            t.pendown()
            t.goto(x_right, y_pos)
            t.penup()
        
        y_pos += spacing


def draw_hatch_in_circle(t, cx, cy, radius, color, density, angle):
    """Fill a circle with parallel hatch lines.
    
    Args:
        cx, cy: Circle center coordinates
        radius: Circle radius
    """
    t.pensize(1)
    t.pencolor(color)
    
    spacing = density
    
    t.penup()
    
    # Draw horizontal or vertical lines depending on angle
    # For circles, we simplify diagonal angles to horizontal/vertical for cleaner appearance
    if angle == 0 or angle == 45:  # Horizontal lines (0° and simplified 45°)
        y_pos = cy - radius
        while y_pos <= cy + radius:
            # Calculate x intersections with circle: (x-cx)^2 + (y-cy)^2 = r^2
            dy = y_pos - cy
            if abs(dy) <= radius:
                dx = (radius**2 - dy**2) ** 0.5
                x_left = cx - dx
                x_right = cx + dx
                
                t.goto(x_left, y_pos)
                t.pendown()
                t.goto(x_right, y_pos)
                t.penup()
            
            y_pos += spacing
    else:  # Vertical lines (90° and simplified 135°)
        x_pos = cx - radius
        while x_pos <= cx + radius:
            # Calculate y intersections with circle
            dx = x_pos - cx
            if abs(dx) <= radius:
                dy = (radius**2 - dx**2) ** 0.5
                y_bottom = cy - dy
                y_top = cy + dy
                
                t.goto(x_pos, y_bottom)
                t.pendown()
                t.goto(x_pos, y_top)
                t.penup()
            
            x_pos += spacing


if __name__ == "__main__":
    try:
        draw_sol_lewitt_art()
    except turtle.Terminator:
        pass
    except Exception as e:
        if "invalid command name" in str(e):
            pass
        else:
            raise
