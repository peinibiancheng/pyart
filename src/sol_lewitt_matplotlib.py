"""
Sol LeWitt-inspired geometric wall drawing using Matplotlib.
Inspired by Sol LeWitt's minimalist wall drawings with dense parallel lines.

Usage:
    python sol_lewitt_matplotlib.py

Requirements:
    - matplotlib>=3.10.0
    - numpy>=2.0.0

Features:
    - 2x2 grid layout
    - Quadrant 1 (top-left): Dense horizontal lines
    - Quadrant 2 (top-right): Dense vertical lines
    - Quadrant 3 (bottom-left): Dense diagonal lines (45° NE direction)
    - Quadrant 4 (bottom-right): Dense diagonal lines (45° SE direction)
    - Thin black lines with perfect spacing
    - High-precision plotting for shimmering minimalist effect
"""

import matplotlib.pyplot as plt
import numpy as np


def create_sol_lewitt_wall_drawing():
    """
    Create a Sol LeWitt-inspired wall drawing with 2x2 grid.
    
    Each quadrant contains dense, parallel lines in different directions:
    - Top-left: Horizontal lines
    - Top-right: Vertical lines
    - Bottom-left: Diagonal lines (45° northeast)
    - Bottom-right: Diagonal lines (45° southeast)
    """
    # Create figure with 2x2 subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Sol LeWitt-Inspired Wall Drawing', fontsize=16, fontweight='bold')
    
    # Set consistent parameters for all quadrants
    line_spacing = 0.05  # Distance between parallel lines (smaller = denser)
    line_width = 0.5     # Thin lines for minimalist effect
    line_color = 'black'
    
    # Quadrant 1 (top-left): Horizontal lines
    draw_horizontal_lines(axs[0, 0], line_spacing, line_width, line_color)
    axs[0, 0].set_title('Horizontal Lines', fontsize=12)
    
    # Quadrant 2 (top-right): Vertical lines
    draw_vertical_lines(axs[0, 1], line_spacing, line_width, line_color)
    axs[0, 1].set_title('Vertical Lines', fontsize=12)
    
    # Quadrant 3 (bottom-left): Diagonal lines (45° northeast)
    draw_diagonal_lines_ne(axs[1, 0], line_spacing, line_width, line_color)
    axs[1, 0].set_title('Diagonal Lines (45° NE)', fontsize=12)
    
    # Quadrant 4 (bottom-right): Diagonal lines (45° southeast)
    draw_diagonal_lines_se(axs[1, 1], line_spacing, line_width, line_color)
    axs[1, 1].set_title('Diagonal Lines (45° SE)', fontsize=12)
    
    # Remove axes and set equal aspect ratio for all quadrants
    for i in range(2):
        for j in range(2):
            axs[i, j].set_xlim(0, 1)
            axs[i, j].set_ylim(0, 1)
            axs[i, j].set_aspect('equal')
            axs[i, j].axis('off')
    
    plt.tight_layout()
    plt.savefig('sol_lewitt_matplotlib.png', dpi=300, bbox_inches='tight')
    plt.show()


def draw_horizontal_lines(ax, spacing, line_width, color):
    """
    Draw dense horizontal lines in a quadrant.
    
    Args:
        ax: Matplotlib axis object
        spacing: Distance between parallel lines
        line_width: Width of each line
        color: Color of the lines
    """
    y_positions = np.arange(0, 1 + spacing, spacing)
    
    for y in y_positions:
        ax.plot([0, 1], [y, y], color=color, linewidth=line_width)


def draw_vertical_lines(ax, spacing, line_width, color):
    """
    Draw dense vertical lines in a quadrant.
    
    Args:
        ax: Matplotlib axis object
        spacing: Distance between parallel lines
        line_width: Width of each line
        color: Color of the lines
    """
    x_positions = np.arange(0, 1 + spacing, spacing)
    
    for x in x_positions:
        ax.plot([x, x], [0, 1], color=color, linewidth=line_width)


def draw_diagonal_lines_ne(ax, spacing, line_width, color):
    """
    Draw dense diagonal lines (45° northeast direction) in a quadrant.
    Lines go from bottom-left to top-right.
    
    Args:
        ax: Matplotlib axis object
        spacing: Distance between parallel lines (adjusted for diagonal)
        line_width: Width of each line
        color: Color of the lines
    """
    # For 45° diagonals, we need to adjust spacing to maintain visual density
    # The perpendicular distance between diagonal lines should be spacing
    diagonal_spacing = spacing * np.sqrt(2)
    
    # Generate lines starting from the left edge and bottom edge
    # Lines are parameterized as y = x + offset
    # offset ranges from -1 to 1 to cover the entire square
    offsets = np.arange(-1, 1 + diagonal_spacing, diagonal_spacing)
    
    for offset in offsets:
        # Calculate intersection points with the square boundary
        # For line y = x + offset within square [0,1] x [0,1]
        
        if offset >= 0:
            # Line intersects bottom edge (y=0) and possibly right edge (x=1)
            x_start = 0
            y_start = offset
            x_end = min(1, 1 - offset)
            y_end = x_end + offset
        else:
            # Line intersects left edge (x=0) and possibly top edge (y=1)
            x_start = -offset
            y_start = 0
            x_end = min(1, 1 - offset)
            y_end = x_end + offset
        
        # Clip to [0, 1] boundaries
        if 0 <= y_start <= 1 and 0 <= y_end <= 1:
            ax.plot([x_start, x_end], [y_start, y_end], 
                   color=color, linewidth=line_width)


def draw_diagonal_lines_se(ax, spacing, line_width, color):
    """
    Draw dense diagonal lines (45° southeast direction) in a quadrant.
    Lines go from top-left to bottom-right.
    
    Args:
        ax: Matplotlib axis object
        spacing: Distance between parallel lines (adjusted for diagonal)
        line_width: Width of each line
        color: Color of the lines
    """
    # For 45° diagonals, adjust spacing to maintain visual density
    diagonal_spacing = spacing * np.sqrt(2)
    
    # Generate lines starting from the left edge and top edge
    # Lines are parameterized as y = -x + offset
    # offset ranges from 0 to 2 to cover the entire square
    offsets = np.arange(0, 2 + diagonal_spacing, diagonal_spacing)
    
    for offset in offsets:
        # Calculate intersection points with the square boundary
        # For line y = -x + offset within square [0,1] x [0,1]
        
        if offset <= 1:
            # Line intersects left edge (x=0) and possibly bottom edge (y=0)
            x_start = 0
            y_start = offset
            x_end = min(offset, 1)
            y_end = offset - x_end
        else:
            # Line intersects top edge (y=1) and right edge (x=1)
            x_start = offset - 1
            y_start = 1
            x_end = min(1, offset)
            y_end = offset - x_end
        
        # Clip to [0, 1] boundaries
        if 0 <= x_start <= 1 and 0 <= x_end <= 1:
            if 0 <= y_start <= 1 and 0 <= y_end <= 1:
                ax.plot([x_start, x_end], [y_start, y_end], 
                       color=color, linewidth=line_width)


if __name__ == "__main__":
    create_sol_lewitt_wall_drawing()
