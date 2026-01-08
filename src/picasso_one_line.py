#!/usr/bin/env python3
"""
Picasso-Style One-Line Drawing
Creates minimalist one-line drawings inspired by Picasso's famous continuous line works
like his 'Penguin', 'Dog', and 'Camel' drawings.

Usage:
    python picasso_one_line.py

Requirements:
    - matplotlib>=3.10.0
    - numpy>=2.0.0

Features:
    - Single continuous black stroke using Bézier curves
    - Textured paper-colored background
    - Fluid movement and abstract simplicity
    - Elegant minimalist aesthetic
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
import numpy as np


def create_textured_background(ax, fig):
    """
    Create a textured paper-colored background.
    
    Args:
        ax: Matplotlib axes object
        fig: Matplotlib figure object
    """
    # Paper color - warm beige/cream tone
    paper_color = '#f5f0e8'
    ax.set_facecolor(paper_color)
    fig.patch.set_facecolor(paper_color)
    
    # Add subtle texture with random dots to simulate paper grain
    np.random.seed(42)  # For reproducibility
    num_dots = 3000
    x_dots = np.random.uniform(-1, 11, num_dots)
    y_dots = np.random.uniform(-1, 11, num_dots)
    
    # Very subtle texture dots in varying shades
    for i in range(num_dots):
        alpha = np.random.uniform(0.01, 0.03)
        size = np.random.uniform(0.5, 2)
        color_variation = np.random.uniform(0.92, 0.98)
        ax.plot(x_dots[i], y_dots[i], 'o', 
                color=(color_variation, color_variation, color_variation), 
                alpha=alpha, markersize=size)


def create_dog_path():
    """
    Create a continuous one-line path for a minimalist dog drawing
    inspired by Picasso's one-line animal drawings.
    
    Returns:
        Path: A matplotlib Path object representing the continuous stroke
    """
    # Define the vertices for the continuous line
    # Starting from the tail, going through body, head, and back
    vertices = [
        # Tail start
        (1.5, 3.0),
        
        # Tail curve (using Bézier control points)
        (1.0, 3.5),
        (1.0, 4.0),
        (1.5, 4.5),
        
        # Lower back
        (2.0, 4.2),
        (3.0, 4.0),
        
        # Back leg (going down)
        (3.2, 3.8),
        (3.3, 2.5),
        (3.2, 1.5),
        
        # Paw and turn
        (3.3, 1.0),
        (3.5, 1.2),
        
        # Back leg up
        (3.6, 2.0),
        (3.7, 3.0),
        (3.8, 3.5),
        
        # Belly
        (4.5, 3.3),
        (5.5, 3.1),
        (6.5, 3.0),
        
        # Front leg down
        (6.7, 2.8),
        (6.8, 2.0),
        (6.7, 1.0),
        
        # Front paw turn
        (6.8, 0.8),
        (7.0, 1.0),
        
        # Front leg up
        (7.1, 2.0),
        (7.2, 3.0),
        
        # Chest
        (7.5, 3.5),
        (8.0, 4.0),
        
        # Neck going up
        (8.2, 4.5),
        (8.3, 5.5),
        
        # Head/snout forward
        (8.5, 6.0),
        (9.0, 6.5),
        (9.5, 6.7),
        
        # Nose tip
        (10.0, 6.8),
        
        # Snout top coming back
        (9.8, 7.0),
        (9.3, 7.2),
        
        # Forehead
        (8.8, 7.3),
        (8.3, 7.5),
        
        # Ear going up
        (8.0, 7.8),
        (7.8, 8.3),
        
        # Ear tip
        (7.7, 8.8),
        
        # Ear coming down
        (7.5, 8.5),
        (7.4, 8.0),
        
        # Back of head
        (7.2, 7.5),
        (6.8, 7.0),
        
        # Neck/back going down
        (6.0, 6.5),
        (5.0, 6.0),
        (4.0, 5.5),
        (3.0, 5.0),
        (2.0, 4.7),
        
        # Back to tail
        (1.5, 4.6),
        (1.3, 4.3),
        (1.4, 3.8),
        (1.5, 3.0),  # Close the loop at tail
    ]
    
    # Create path codes for smooth Bézier curves
    codes = [Path.MOVETO]  # Start point
    
    # Use CURVE4 (cubic Bézier) for smooth flowing lines
    for i in range(1, len(vertices)):
        codes.append(Path.CURVE4)
    
    # Adjust codes to ensure we have the right number
    while len(codes) < len(vertices):
        codes.append(Path.LINETO)
    
    codes = codes[:len(vertices)]
    
    # Create the path
    path = Path(vertices, codes)
    return path


def create_penguin_path():
    """
    Create an alternative continuous one-line path for a minimalist penguin
    inspired by Picasso's famous penguin drawing.
    
    Returns:
        Path: A matplotlib Path object representing the continuous stroke
    """
    vertices = [
        # Starting at bottom left flipper
        (3.0, 2.0),
        (2.5, 2.5),
        (2.3, 3.0),
        
        # Left side going up
        (2.5, 4.0),
        (3.0, 5.0),
        (3.5, 6.0),
        
        # Head left side
        (4.0, 7.0),
        (4.5, 7.8),
        
        # Top of head
        (5.0, 8.5),
        (5.5, 8.8),
        (6.0, 8.8),
        
        # Beak
        (6.5, 8.5),
        (7.0, 8.0),
        
        # Right side of head going down
        (7.0, 7.5),
        (6.8, 7.0),
        (6.5, 6.0),
        
        # Right body
        (6.3, 5.0),
        (6.0, 4.0),
        (5.8, 3.0),
        
        # Right flipper
        (6.0, 2.5),
        (6.5, 2.3),
        (7.0, 2.5),
        
        # Flipper tip
        (7.2, 2.8),
        
        # Coming back
        (7.0, 3.0),
        (6.5, 3.2),
        
        # Bottom
        (5.5, 2.5),
        (4.5, 2.2),
        (3.5, 2.0),
        (3.0, 2.0),  # Close at start
    ]
    
    codes = [Path.MOVETO]
    for i in range(1, len(vertices)):
        codes.append(Path.CURVE4)
    
    while len(codes) < len(vertices):
        codes.append(Path.LINETO)
    codes = codes[:len(vertices)]
    
    path = Path(vertices, codes)
    return path


def draw_picasso_oneline(style='dog'):
    """
    Create a Picasso-style one-line drawing.
    
    Args:
        style: Either 'dog' or 'penguin' to select the drawing style
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10), dpi=100)
    
    # Create textured background
    create_textured_background(ax, fig)
    
    # Choose the path based on style
    if style == 'penguin':
        path = create_penguin_path()
    else:
        path = create_dog_path()
    
    # Create the patch with the continuous stroke
    patch = mpatches.PathPatch(
        path,
        facecolor='none',
        edgecolor='black',
        linewidth=3.5,
        capstyle='round',
        joinstyle='round',
        antialiased=True
    )
    
    # Add the patch to the axes
    ax.add_patch(patch)
    
    # Set equal aspect ratio and clean appearance
    ax.set_aspect('equal')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    
    # Remove axes for clean minimalist look
    ax.axis('off')
    
    # Add subtle signature in Picasso style (bottom right)
    ax.text(9.5, 0.5, 'P.', 
            fontsize=14, 
            fontstyle='italic',
            color='#333333',
            alpha=0.6,
            ha='right')
    
    # Set tight layout
    plt.tight_layout()
    
    # Save the figure
    output_filename = f'picasso_oneline_{style}.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', 
                facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"✓ Artwork saved as: {output_filename}")
    
    # Display the figure
    plt.show()


def main():
    """
    Main function to generate Picasso-style one-line drawings.
    Creates both dog and penguin variations.
    """
    print("=" * 60)
    print("Picasso-Style One-Line Drawing Generator")
    print("=" * 60)
    print("\nCreating minimalist one-line drawings inspired by Picasso...")
    print("Features:")
    print("  • Single continuous stroke using Bézier curves")
    print("  • Textured paper-colored background")
    print("  • Fluid movement and abstract simplicity")
    print("  • Elegant black line on warm paper tone")
    print()
    
    # Generate dog drawing
    print("Creating 'Dog' drawing...")
    draw_picasso_oneline(style='dog')
    
    # Generate penguin drawing
    print("\nCreating 'Penguin' drawing...")
    draw_picasso_oneline(style='penguin')
    
    print("\n" + "=" * 60)
    print("✓ All drawings completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
