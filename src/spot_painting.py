"""
Damien Hirst 'Spot Paintings'-inspired artwork using Python's Matplotlib.
Generates a grid of colorful circles with pop art aesthetics.

Usage:
    python spot_painting.py

Requirements:
    - Python 3.x
    - matplotlib

Features:
    - 12x12 grid of perfectly aligned colored spots
    - Randomly assigned vibrant colors for each spot
    - Consistent spacing and centering
    - Clean, minimal aesthetic with no borders/outlines
    - Pure white background
"""

import matplotlib.pyplot as plt
import random


def draw_spot_painting():
    """
    Generate a Damien Hirst 'Spot Paintings'-inspired artwork.
    
    Creates a 12x12 grid of colorful circles with:
    - Randomly assigned vibrant colors for each spot
    - Perfect grid alignment with consistent spacing
    - Centered composition on a pure white canvas
    - No outlines on circles
    """
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
        "#FFA500",  # Orange
        "#8B008B",  # Dark Magenta
        "#7FFF00",  # Chartreuse
        "#DC143C",  # Crimson
        "#00FFFF",  # Cyan
        "#ADFF2F",  # Green Yellow
        "#DA70D6",  # Orchid
        "#98FB98",  # Pale Green
        "#DDA0DD",  # Plum
        "#FA8072",  # Salmon
        "#F0E68C",  # Khaki
        "#EE82EE",  # Violet
        "#FFFF54",  # Laser Lemon
        "#00FF7F",  # Spring Green
        "#40E0D0",  # Turquoise
        "#F5DEB3",  # Wheat
        "#9ACD32",  # Yellow Green
    ]
    
    # Grid configuration
    rows = 12  # Number of rows in the grid
    cols = 12  # Number of columns in the grid
    
    # Generate grid coordinates
    x_coords = []
    y_coords = []
    spot_colors = []
    
    # Create 12x12 grid centered at origin
    for row in range(rows):
        for col in range(cols):
            # Center the grid by offsetting from origin
            # Grid goes from -5.5 to 5.5 on both axes (12 spots, centered)
            x = col - (cols - 1) / 2
            y = (rows - 1) / 2 - row  # Flip y-axis to match conventional grid
            
            x_coords.append(x)
            y_coords.append(y)
            
            # Assign a randomly selected vibrant color to each spot
            spot_colors.append(random.choice(colors))
    
    # Create figure and axis with white background
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
    ax.set_facecolor('white')
    
    # Create scatter plot with no outlines
    ax.scatter(x_coords, y_coords, c=spot_colors, s=800, edgecolors='none')
    
    # Hide all axes
    ax.axis('off')
    
    # Set equal aspect ratio for perfect circles
    ax.set_aspect('equal')
    
    # Adjust layout to remove padding
    plt.tight_layout(pad=0)
    
    # Display the artwork
    plt.show()


if __name__ == "__main__":
    draw_spot_painting()
