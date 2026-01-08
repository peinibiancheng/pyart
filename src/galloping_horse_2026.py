"""
Galloping Horse artwork for 2026 - symbolizing "马到成功" (immediate success).
Creates a dynamic horse in motion using Python's turtle module.

Usage:
    python galloping_horse_2026.py

Requirements:
    - Python 3.x with tkinter support
    - Standard library only (turtle, math)

Features:
    - Stylized galloping horse with flowing mane and tail
    - Dynamic motion lines to show speed
    - 2026 text banner
    - Color palette: #c01c28 (red), #f6d32d (gold), #1c71d8 (blue), black
    - Represents the Chinese idiom 马到成功 (success comes swiftly)
"""

import turtle
import math


def draw_galloping_horse():
    """
    Generate a galloping horse artwork for 2026.
    
    Creates:
    - Stylized horse in galloping pose
    - Flowing mane and tail showing motion
    - Motion lines and dust clouds
    - 2026 banner with festive colors
    - Color palette: red (#c01c28), gold (#f6d32d), blue (#1c71d8), black
    """
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("#f6f5f4")  # Light background
    screen.title("Galloping Horse 2026 - 马到成功")
    screen.tracer(2)  # Commented out to enable smooth animation for t.speed(1)

    t = turtle.Turtle()
    t.speed(1)  # Fastest drawing speed

    t.hideturtle()
    
    # Draw motion lines in background
    draw_motion_lines(t)
    
    # Draw the horse
    draw_horse(t)
    
    # Draw flowing mane
    draw_mane(t)
    
    # Draw flowing tail
    draw_tail(t)
    
    # Draw 2026 banner
    draw_2026_banner(t)
    
    # Add success symbol (马到成功)
    draw_success_text(t)
    
    # Finish
    screen.update()
    turtle.done()


def draw_motion_lines(t):
    """Draw motion lines in the background to show speed."""
    t.pensize(2)
    
    # Draw horizontal speed lines
    for y in range(-200, 250, 40):
        # Vary the line length for dynamic effect
        start_x = -380
        end_x = start_x + 100 + (y % 80)
        
        t.penup()
        t.goto(start_x, y)
        t.pendown()
        t.pencolor("#1c71d8")
        
        # Draw wavy line
        for x in range(int(end_x - start_x)):
            new_x = start_x + x
            new_y = y + 3 * math.sin(x * 0.2)
            t.goto(new_x, new_y)


def draw_horse(t):
    """Draw the main horse body."""
    # Horse body (torso)
    draw_horse_body(t, 0, -50)
    
    # Horse head
    draw_horse_head(t, 150, 50)
    
    # Horse neck
    draw_horse_neck(t, 100, 0)
    
    # Legs (galloping position)
    draw_front_legs(t)
    draw_back_legs(t)


def draw_horse_body(t, x, y):
    """Draw the horse's torso."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("#c01c28")
    t.begin_fill()
    
    # Draw elliptical body
    t.setheading(0)
    for i in range(180):
        t.forward(1.5)
        t.left(1)
    
    # Bottom of body
    t.setheading(180)
    for i in range(180):
        t.forward(1.2)
        t.left(1)
    
    t.end_fill()


def draw_horse_head(t, x, y):
    """Draw the horse's head."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("#c01c28")
    t.begin_fill()
    
    # Head shape
    t.setheading(45)
    t.forward(40)
    t.setheading(90)
    t.forward(30)
    t.setheading(180)
    t.forward(25)
    
    # Snout
    t.setheading(270)
    t.forward(20)
    t.setheading(0)
    t.forward(15)
    t.setheading(270)
    t.forward(10)
    
    t.goto(x, y)
    t.end_fill()
    
    # Eye
    t.penup()
    t.goto(x + 15, y + 25)
    t.pendown()
    t.dot(8, "black")
    
    # Ear
    draw_ear(t, x + 10, y + 45)


def draw_ear(t, x, y):
    """Draw horse's ear."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("#c01c28")
    t.begin_fill()
    
    t.setheading(60)
    t.forward(15)
    t.setheading(180)
    t.forward(8)
    t.goto(x, y)
    
    t.end_fill()


def draw_horse_neck(t, x, y):
    """Draw the horse's neck connecting body and head."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("#c01c28")
    t.begin_fill()
    
    # Neck curve
    t.setheading(45)
    for i in range(30):
        t.forward(2)
        t.left(1)
    
    # Top of neck
    t.setheading(0)
    t.forward(20)
    
    # Back down
    t.setheading(225)
    for i in range(30):
        t.forward(2)
        t.right(1)
    
    t.goto(x, y)
    t.end_fill()


def draw_front_legs(t):
    """Draw front legs in galloping position."""
    # Front leg 1 (extended forward)
    draw_leg(t, 80, -50, 80, 30)
    
    # Front leg 2 (tucked)
    draw_leg(t, 60, -50, 60, -10)


def draw_back_legs(t):
    """Draw back legs in galloping position."""
    # Back leg 1 (pushing off)
    draw_leg(t, -60, -50, 100, -30)
    
    # Back leg 2 (extended back)
    draw_leg(t, -80, -50, 80, -40)


def draw_leg(t, x, y, length, angle):
    """Draw a single leg."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("black")
    t.fillcolor("#c01c28")
    t.pensize(8)
    
    t.setheading(270 + angle)
    t.forward(length)
    
    # Hoof
    t.pensize(10)
    t.forward(5)
    
    t.pensize(2)


def draw_mane(t):
    """Draw flowing mane showing motion."""
    t.pensize(3)
    
    # Multiple flowing strands
    mane_positions = [
        (110, 45), (120, 50), (115, 55), (125, 40), (105, 50)
    ]
    
    for x, y in mane_positions:
        draw_mane_strand(t, x, y)


def draw_mane_strand(t, x, y):
    """Draw a single strand of flowing mane."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("#f6d32d")
    t.pensize(4)
    
    # Draw wavy strand flowing backward
    t.setheading(180)
    for i in range(20):
        curve = math.sin(i * 0.3) * 5
        t.setheading(180 + curve)
        t.forward(3)


def draw_tail(t):
    """Draw flowing tail showing motion."""
    base_x, base_y = -135, 0
    
    t.pensize(3)
    
    # Multiple flowing tail strands
    for offset in range(-15, 20, 8):
        draw_tail_strand(t, base_x, base_y + offset)


def draw_tail_strand(t, x, y):
    """Draw a single strand of flowing tail."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("#f6d32d")
    t.pensize(5)
    
    # Draw sweeping curve backward
    t.setheading(200)
    for i in range(30):
        curve = math.sin(i * 0.2) * 8
        t.setheading(200 + curve)
        t.forward(2.5)


def draw_2026_banner(t):
    """Draw 2026 banner."""
    t.penup()
    t.goto(-350, 200)
    t.pendown()
    
    # Banner background
    t.pencolor("#1c71d8")
    t.fillcolor("#1c71d8")
    t.begin_fill()
    
    for _ in range(2):
        t.forward(150)
        t.right(90)
        t.forward(50)
        t.right(90)
    
    t.end_fill()
    
    # 2026 text
    t.penup()
    t.goto(-330, 180)
    t.pencolor("#f6d32d")
    
    style = ('Arial', 36, 'bold')
    t.write('2026', font=style, align='left')


def draw_success_text(t):
    """Draw success message (马到成功)."""
    t.penup()
    t.goto(-350, -250)
    t.pendown()
    
    t.pencolor("#c01c28")
    
    style = ('Arial', 24, 'bold')
    t.write('马到成功', font=style, align='left')
    
    # English translation
    t.penup()
    t.goto(-350, -280)
    t.pencolor("black")
    
    style_small = ('Arial', 14, 'normal')
    t.write('Immediate Success', font=style_small, align='left')


if __name__ == "__main__":
    draw_galloping_horse()
