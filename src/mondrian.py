"""
Piet Mondrian-inspired composition using Python's matplotlib module.
Generates a grid-like composition with primary colors and black borders.

Usage:
    python mondrian.py

Requirements:
    - matplotlib>=3.10.0
    - numpy>=2.0.0

Features:
    - Recursive space division creating rectangles of varying sizes
    - Mondrian's signature color palette: Red, Blue, Yellow, and White
    - Thick black borders (linewidth > 5) between all rectangles
    - Composition reminiscent of "Composition with Red Blue and Yellow"
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


def should_divide(width, height, depth, max_depth=4):
    """
    Determine whether a rectangle should be divided further.
    
    Args:
        width: Width of the rectangle
        height: Height of the rectangle
        depth: Current recursion depth
        max_depth: Maximum recursion depth
        
    Returns:
        bool: True if the rectangle should be divided, False otherwise
    """
    if depth >= max_depth:
        return False
    
    # Larger rectangles are more likely to be divided
    # Minimum size check to avoid creating too tiny rectangles
    if width < 0.15 or height < 0.15:
        return False
    
    # Probabilistic decision with bias towards division for larger rectangles
    area = width * height
    if area > 0.3:
        return random.random() < 0.9
    elif area > 0.15:
        return random.random() < 0.7
    else:
        return random.random() < 0.4


def divide_rectangle(ax, x, y, width, height, depth=0, max_depth=4):
    """
    Recursively divide a rectangle and fill with Mondrian colors.
    
    Args:
        ax: Matplotlib axes object
        x: X-coordinate of bottom-left corner
        y: Y-coordinate of bottom-left corner
        width: Width of the rectangle
        height: Height of the rectangle
        depth: Current recursion depth
        max_depth: Maximum recursion depth
    """
    # Mondrian's signature color palette
    colors = [
        '#FFFFFF',  # White (most common)
        '#FFFFFF',  # White (increase probability)
        '#FFFFFF',  # White (increase probability)
        '#DC143C',  # Red (Crimson)
        '#0047AB',  # Blue (Cobalt Blue)
        '#FFD700',  # Yellow (Gold)
    ]
    
    if not should_divide(width, height, depth, max_depth):
        # Draw the filled rectangle with a random Mondrian color
        color = random.choice(colors)
        rect = patches.Rectangle(
            (x, y), width, height,
            linewidth=6,  # Thick black border
            edgecolor='black',
            facecolor=color
        )
        ax.add_patch(rect)
        return
    
    # Decide whether to divide horizontally or vertically
    # Prefer dividing along the longer dimension for better proportions
    if width > height:
        divide_vertically = random.random() < 0.7
    elif height > width:
        divide_vertically = random.random() < 0.3
    else:
        divide_vertically = random.random() < 0.5
    
    if divide_vertically:
        # Choose a division point (avoid dividing too close to the edges)
        min_ratio = 0.3
        max_ratio = 0.7
        split_ratio = random.uniform(min_ratio, max_ratio)
        split_x = x + width * split_ratio
        
        # Recursively divide left and right parts
        divide_rectangle(ax, x, y, width * split_ratio, height, depth + 1, max_depth)
        divide_rectangle(ax, split_x, y, width * (1 - split_ratio), height, depth + 1, max_depth)
    else:
        # Divide horizontally
        min_ratio = 0.3
        max_ratio = 0.7
        split_ratio = random.uniform(min_ratio, max_ratio)
        split_y = y + height * split_ratio
        
        # Recursively divide bottom and top parts
        divide_rectangle(ax, x, y, width, height * split_ratio, depth + 1, max_depth)
        divide_rectangle(ax, x, split_y, width, height * (1 - split_ratio), depth + 1, max_depth)


def create_mondrian_composition():
    """
    Generate a Piet Mondrian-style composition.
    
    Creates a composition with:
    - Rectangular divisions of varying sizes
    - Mondrian's signature colors: Red, Blue, Yellow, and White
    - Thick black borders between all rectangles
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Set the limits and aspect ratio
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    
    # Remove axes for clean aesthetic
    ax.axis('off')
    
    # Set white background
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    # Start recursive division from the entire canvas
    divide_rectangle(ax, 0, 0, 1, 1, depth=0, max_depth=4)
    
    # Set title
    plt.title("Composition with Red Blue and Yellow (Mondrian-Inspired)", 
              fontsize=14, fontweight='bold', pad=20)
    
    # Adjust layout to remove extra whitespace
    plt.tight_layout()
    
    # Save the composition to a file (for headless environments)
    plt.savefig('mondrian_composition.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Mondrian composition saved to 'mondrian_composition.png'")
    
    # Display the composition
    plt.show()


if __name__ == "__main__":
    create_mondrian_composition()
