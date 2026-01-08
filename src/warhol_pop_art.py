#!/usr/bin/env python3
"""
Andy Warhol-inspired Pop Art Generator
Creates a 2x2 grid of the same abstract portrait with different high-contrast colormaps.
Simulates the "silkscreen" look with bold outlines and flat, saturated color fills.

Usage:
    python warhol_pop_art.py

Requirements:
    - matplotlib>=3.10.0
    - numpy>=2.0.0

Features:
    - 2x2 grid with same abstract shape/portrait in each quadrant
    - Four different high-contrast colormaps: Magma, Viridis, Cividis, and custom neon
    - Bold outlines for silkscreen effect
    - Flat, saturated color fills
    - Pop art aesthetic inspired by Andy Warhol
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


def create_abstract_portrait():
    """
    Create an abstract portrait/face shape as a 2D numpy array.
    
    Returns:
        np.ndarray: 2D array representing an abstract portrait with values 0-1
    """
    # Set seed for reproducible artwork
    np.random.seed(42)
    
    # Create a 200x200 grid
    size = 200
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)
    
    # Create face outline (circle/oval)
    face = np.exp(-((X**2) / 0.6 + (Y**2) / 0.8) * 3)
    
    # Add eyes (two circles)
    eye_left = np.exp(-((X + 0.25)**2 + (Y - 0.25)**2) * 50)
    eye_right = np.exp(-((X - 0.25)**2 + (Y - 0.25)**2) * 50)
    
    # Add nose (triangle-like shape)
    nose = np.exp(-((X**2) / 0.02 + ((Y + 0.1)**2) / 0.1) * 20)
    
    # Add mouth (curved shape)
    mouth = np.exp(-(X**2 / 0.15 + (Y + 0.5)**2 / 0.03) * 15)
    
    # Add hair/top feature
    hair = np.exp(-((X**2) / 0.5 + ((Y - 0.6)**2) / 0.2) * 5)
    
    # Combine all features
    portrait = face + eye_left * 2 + eye_right * 2 + nose * 1.5 + mouth * 1.2 + hair * 0.8
    
    # Normalize to 0-1 range
    portrait = (portrait - portrait.min()) / (portrait.max() - portrait.min())
    
    # Add some noise for texture
    noise = np.random.rand(size, size) * 0.1
    portrait = portrait + noise
    portrait = np.clip(portrait, 0, 1)
    
    return portrait


def create_neon_colormap():
    """
    Create a custom neon colormap with vibrant, saturated colors.
    
    Returns:
        matplotlib.colors.LinearSegmentedColormap: Custom neon colormap
    """
    # Neon colors: Electric blue, hot pink, lime green, orange, purple
    neon_colors = [
        '#0D00FF',  # Electric Blue
        '#FF00FF',  # Magenta/Hot Pink
        '#00FF00',  # Lime Green
        '#FFFF00',  # Neon Yellow
        '#FF00AA',  # Hot Pink
        '#00FFFF',  # Cyan
    ]
    
    n_bins = 256
    cmap = mcolors.LinearSegmentedColormap.from_list('neon', neon_colors, N=n_bins)
    return cmap


def add_silkscreen_outline(ax, data, color='black', linewidth=2.5):
    """
    Add bold outlines to simulate silkscreen printing effect.
    
    Args:
        ax: Matplotlib axis object
        data: 2D numpy array of the image data
        color: Color of the outline
        linewidth: Width of the outline
    """
    # Create contour lines at specific levels to create bold outlines
    contour_levels = [0.3, 0.5, 0.7]
    ax.contour(data, levels=contour_levels, colors=color, linewidths=linewidth, 
               linestyles='solid', alpha=0.9)


def create_warhol_pop_art():
    """
    Create Andy Warhol-inspired Pop Art with 2x2 grid of the same portrait
    using different high-contrast colormaps.
    """
    # Create the abstract portrait once
    portrait = create_abstract_portrait()
    
    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Andy Warhol Pop Art - 2x2 Grid', fontsize=24, fontweight='bold', 
                 color='#2C3E50', y=0.98)
    
    # Define colormaps for each quadrant
    colormaps = [
        ('magma', 'MAGMA'),
        ('viridis', 'VIRIDIS'),
        ('cividis', 'CIVIDIS'),
        (create_neon_colormap(), 'NEON')
    ]
    
    # Flatten axes array for easier iteration
    axes_flat = axes.flatten()
    
    # Create each quadrant with different colormap
    for idx, (ax, (cmap, label)) in enumerate(zip(axes_flat, colormaps)):
        # Display portrait with high contrast and saturation
        im = ax.imshow(portrait, cmap=cmap, interpolation='bilinear', 
                      vmin=0.2, vmax=0.9)  # Adjust contrast
        
        # Add silkscreen-style bold outlines
        add_silkscreen_outline(ax, portrait, color='black', linewidth=2.5)
        
        # Add subtle title for each quadrant
        ax.set_title(label, fontsize=16, fontweight='bold', pad=10, 
                    color='white', bbox=dict(boxstyle='round,pad=0.5', 
                    facecolor='black', alpha=0.7))
        
        # Remove axes for clean look
        ax.axis('off')
    
    # Adjust layout to minimize white space
    plt.tight_layout()
    
    # Save the artwork
    output_file = 'warhol_pop_art.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"✨ Pop Art saved as: {output_file}")
    
    # Display the artwork
    plt.show()
    
    return output_file


if __name__ == "__main__":
    print("🎨 Creating Andy Warhol-inspired Pop Art...")
    print("📐 Generating 2x2 grid with different colormaps...")
    output_file = create_warhol_pop_art()
    print(f"✅ Done! Your Pop Art masterpiece is ready!")
