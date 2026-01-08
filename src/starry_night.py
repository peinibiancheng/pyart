"""
Van Gogh 'Starry Night'-inspired artwork using Matplotlib.
Uses vector fields to define swirling, flow-like patterns and thousands
of short, thick strokes to create an energetic, moving sky.

Usage:
    python starry_night.py

Requirements:
    - matplotlib>=3.10.0
    - numpy>=2.0.0

Features:
    - Vector fields (streamplot) defining swirling flow patterns
    - Thousands of short, thick strokes along flow lines
    - Post-Impressionist color palette (blues and yellows)
    - Energetic, moving sky with dashed brushstrokes
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.collections import LineCollection


def create_vector_field(X, Y):
    """
    Create a swirling vector field for Van Gogh-style flow patterns.
    
    Parameters:
    -----------
    X, Y : numpy arrays
        Meshgrid coordinates
        
    Returns:
    --------
    U, V : numpy arrays
        Vector field components
    """
    # Create multiple swirl centers
    centers = [
        (0.3, 0.7, 1.5, 0.3),   # (x, y, strength, rotation)
        (0.7, 0.6, 1.2, -0.5),
        (0.5, 0.8, 0.8, 0.7),
    ]
    
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    
    # Add swirling patterns from each center
    for cx, cy, strength, rotation in centers:
        dx = X - cx
        dy = Y - cy
        r = np.sqrt(dx**2 + dy**2) + 0.1
        
        # Circular flow with radial component
        U += strength * (-dy / r + rotation * dx)
        V += strength * (dx / r + rotation * dy)
    
    # Add general horizontal flow
    U += 0.5
    
    return U, V


def create_brushstrokes(X, Y, U, V, num_strokes=5000, random_seed=42):
    """
    Create thousands of short, thick brushstrokes along flow lines.
    
    Parameters:
    -----------
    X, Y : numpy arrays
        Meshgrid coordinates
    U, V : numpy arrays
        Vector field components
    num_strokes : int
        Number of brushstrokes to create
    random_seed : int, optional
        Random seed for reproducibility
        
    Returns:
    --------
    segments : list
        List of line segments
    colors : list
        List of colors for each segment
    linewidths : list
        List of linewidths for each segment
    """
    rng = np.random.RandomState(random_seed)
    
    segments = []
    colors = []
    linewidths = []
    
    # Post-Impressionist color palette
    blues = [
        '#1a5fb4', '#0d3a6b', '#2563eb', '#1e40af', '#1e3a8a',
        '#0f4c81', '#3b82f6', '#2563eb', '#1d4ed8', '#4169e1'
    ]
    yellows = [
        '#f7931a', '#fbbf24', '#f59e0b', '#d97706', '#fcd34d',
        '#fde047', '#facc15', '#eab308', '#ca8a04', '#ffa500'
    ]
    
    for i in range(num_strokes):
        # Random starting position
        x_start = rng.uniform(0, 1)
        y_start = rng.uniform(0, 1)
        
        # Find vector field direction at this point
        x_idx = int(x_start * (X.shape[1] - 1))
        y_idx = int(y_start * (X.shape[0] - 1))
        
        u = U[y_idx, x_idx]
        v = V[y_idx, x_idx]
        
        # Normalize and scale stroke length
        magnitude = np.sqrt(u**2 + v**2)
        if magnitude > 0:
            u_norm = u / magnitude
            v_norm = v / magnitude
        else:
            u_norm, v_norm = 1, 0
        
        # Create short stroke
        stroke_length = rng.uniform(0.01, 0.03)
        x_end = x_start + u_norm * stroke_length
        y_end = y_start + v_norm * stroke_length
        
        segments.append([(x_start, y_start), (x_end, y_end)])
        
        # Choose color based on position (blues in upper areas, yellows in stars/moon)
        if y_start > 0.7 or (0.6 < x_start < 0.8 and 0.5 < y_start < 0.7):
            # Star/moon areas - yellows
            color = rng.choice(yellows)
        elif rng.random() < 0.1:
            # Occasional yellow strokes in sky for variety
            color = rng.choice(yellows)
        else:
            # Sky areas - blues
            color = rng.choice(blues)
        
        colors.append(color)
        
        # Varying thickness for brushstroke effect
        linewidth = rng.uniform(1.5, 4.0)
        linewidths.append(linewidth)
    
    return segments, colors, linewidths


def draw_starry_night(random_seed=42):
    """
    Generate a Van Gogh 'Starry Night'-inspired artwork using Matplotlib.
    
    Parameters:
    -----------
    random_seed : int, optional
        Random seed for reproducibility
    
    Creates:
    - Swirling vector field defining flow patterns
    - Thousands of short, thick brushstrokes
    - Post-Impressionist color palette (blues and yellows)
    - Energetic, moving sky effect
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0a0a0a')
    ax.set_facecolor('#0a0a0a')
    
    # Create meshgrid for vector field
    x = np.linspace(0, 1, 30)
    y = np.linspace(0, 1, 30)
    X, Y = np.meshgrid(x, y)
    
    # Generate vector field
    U, V = create_vector_field(X, Y)
    
    # Plot streamplot for flow visualization (subtle)
    stream = ax.streamplot(X, Y, U, V, color='#1a5fb4', linewidth=0.5, 
                           density=1.2, arrowsize=0)
    stream.lines.set_alpha(0.3)
    
    # Create and plot brushstrokes
    segments, colors, linewidths = create_brushstrokes(X, Y, U, V, num_strokes=5000, random_seed=random_seed)
    
    lc = LineCollection(segments, colors=colors, linewidths=linewidths,
                        alpha=0.7, capstyle='round')
    ax.add_collection(lc)
    
    # Add some bright stars
    rng = np.random.RandomState(random_seed)
    num_stars = 15
    for i in range(num_stars):
        star_x = rng.uniform(0.1, 0.9)
        star_y = rng.uniform(0.6, 0.95)
        
        # Create star with radiating strokes
        num_rays = 8
        ray_length = 0.02
        for angle in np.linspace(0, 2*np.pi, num_rays, endpoint=False):
            x_end = star_x + ray_length * np.cos(angle)
            y_end = star_y + ray_length * np.sin(angle)
            ax.plot([star_x, x_end], [star_y, y_end], 
                   color='#fbbf24', linewidth=2, alpha=0.9)
        
        # Star center
        ax.scatter(star_x, star_y, s=30, c='#fde047', alpha=1.0, zorder=10)
    
    # Add moon with glow
    moon_x, moon_y = 0.75, 0.65
    moon_radius = 0.08
    
    # Glow effect with multiple circles
    for r in np.linspace(moon_radius * 1.8, moon_radius, 5):
        circle = patches.Circle((moon_x, moon_y), r, 
                               color='#f7931a', alpha=0.15)
        ax.add_patch(circle)
    
    # Bright moon center
    circle = patches.Circle((moon_x, moon_y), moon_radius, 
                           color='#fde047', alpha=0.95)
    ax.add_patch(circle)
    
    # Set limits and remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    plt.title("Starry Night - Van Gogh Inspired", 
             fontsize=16, color='#fbbf24', pad=20, fontweight='bold')
    
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    fig = draw_starry_night()
    plt.savefig('starry_night.png', dpi=300, facecolor='#0a0a0a', 
                bbox_inches='tight')
    print("✓ Starry Night artwork saved as 'starry_night.png'")
    plt.show()
