"""
Georges Seurat-style Pointillism using Matplotlib
乔治·修拉风格点彩画 - 使用Matplotlib实现

Simulates Pointillism by plotting hundreds of thousands of tiny, colorful dots
using ax.scatter(). Uses clusters of slightly different colored dots to create
optical color mixing effects (e.g., mixing yellow and blue dots to create a
"green" area from a distance).

使用Matplotlib的ax.scatter()方法绘制成千上万个微小的彩色点来模拟点彩画。
通过将稍有不同颜色的点簇聚在一起，创造光学混色效果（例如，混合黄色和蓝色的点，
从远处看形成"绿色"区域）。
"""

import numpy as np
import matplotlib.pyplot as plt


def create_dot_cluster(x_center, y_center, num_dots, colors, size_range=(1, 3), spread=0.5):
    """
    Create a cluster of dots with slightly different colors for optical mixing.
    
    Args:
        x_center: X coordinate of cluster center
        y_center: Y coordinate of cluster center
        num_dots: Number of dots in the cluster
        colors: List of colors to randomly choose from
        size_range: Tuple of (min_size, max_size) for dot sizes
        spread: How spread out the dots should be
    
    Returns:
        Tuple of (x_coords, y_coords, colors_array, sizes_array)
    """
    # Generate random positions around center with normal distribution
    x_coords = np.random.normal(x_center, spread, num_dots)
    y_coords = np.random.normal(y_center, spread, num_dots)
    
    # Randomly select colors from the palette
    colors_array = np.random.choice(colors, num_dots)
    
    # Generate random sizes
    sizes_array = np.random.uniform(size_range[0], size_range[1], num_dots)
    
    return x_coords, y_coords, colors_array, sizes_array


def draw_sky(ax, width, height, num_dots=80000):
    """
    Draw sky using blue and white dots for optical mixing.
    
    The upper part has more white dots (highlights), while the middle
    has a mix of blues and whites creating a luminous sky effect.
    """
    # Sky color palette - various blues and whites
    sky_colors_top = ['#FFFFFF', '#F0F8FF', '#E6F3FF', '#D4E9FF']  # More white at top
    sky_colors_mid = ['#87CEEB', '#ADD8E6', '#B0E0E6', '#E0F6FF', '#FFFFFF']
    sky_colors_bottom = ['#5DADE2', '#87CEEB', '#6CA6CD', '#ADD8E6']
    
    x_all, y_all, c_all, s_all = [], [], [], []
    
    # Divide sky into three bands for gradual color transition
    for _ in range(num_dots):
        x = np.random.uniform(0, width)
        y = np.random.uniform(height * 0.5, height)  # Upper half
        
        # Choose color palette based on y position
        if y > height * 0.85:
            color = np.random.choice(sky_colors_top)
        elif y > height * 0.65:
            color = np.random.choice(sky_colors_mid)
        else:
            color = np.random.choice(sky_colors_bottom)
        
        size = np.random.uniform(1, 4)
        
        x_all.append(x)
        y_all.append(y)
        c_all.append(color)
        s_all.append(size)
    
    ax.scatter(x_all, y_all, c=c_all, s=s_all, alpha=0.7, linewidths=0)


def draw_grass(ax, width, height, num_dots=100000):
    """
    Draw grass using yellow and blue dots mixed to create optical green.
    
    This demonstrates the core principle of Pointillism - mixing yellow and
    blue dots creates the illusion of green when viewed from a distance.
    """
    # Grass area: lower-middle portion
    # Using yellow and blue dots to create optical green mixing
    yellow_palette = ['#FFD700', '#FFF44F', '#FFEB3B', '#F4D03F']
    blue_palette = ['#0066CC', '#1E90FF', '#4169E1', '#5B9BD5']
    green_palette = ['#228B22', '#32CD32', '#90EE90', '#9ACD32']  # Some true greens
    brown_palette = ['#8B4513', '#A0522D', '#CD853F', '#DEB887']  # For shadows/earth
    
    x_all, y_all, c_all, s_all = [], [], [], []
    
    for _ in range(num_dots):
        x = np.random.uniform(0, width)
        y = np.random.uniform(0, height * 0.5)  # Lower half
        
        # Foreground (bottom) - more varied colors and larger dots
        if y < height * 0.15:
            # Mix of yellow, blue, and green for rich grass texture
            color_choice = np.random.random()
            if color_choice < 0.3:
                color = np.random.choice(yellow_palette)
            elif color_choice < 0.5:
                color = np.random.choice(blue_palette)
            elif color_choice < 0.85:
                color = np.random.choice(green_palette)
            else:
                color = np.random.choice(brown_palette)  # Shadows
            size = np.random.uniform(2, 5)
        # Middle ground
        elif y < height * 0.35:
            color_choice = np.random.random()
            if color_choice < 0.25:
                color = np.random.choice(yellow_palette)
            elif color_choice < 0.45:
                color = np.random.choice(blue_palette)
            else:
                color = np.random.choice(green_palette)
            size = np.random.uniform(1.5, 4)
        # Background (upper grass, near horizon)
        else:
            color_choice = np.random.random()
            if color_choice < 0.2:
                color = np.random.choice(yellow_palette)
            elif color_choice < 0.35:
                color = np.random.choice(blue_palette)
            else:
                color = np.random.choice(green_palette)
            size = np.random.uniform(1, 3)
        
        x_all.append(x)
        y_all.append(y)
        c_all.append(color)
        s_all.append(size)
    
    ax.scatter(x_all, y_all, c=c_all, s=s_all, alpha=0.65, linewidths=0)


def draw_trees(ax, width, height, num_trees=3):
    """
    Draw trees using clusters of dots in various greens, blues, and yellows.
    """
    tree_dark = ['#0B6623', '#004225', '#355E3B', '#2C5F2D']
    tree_light = ['#90EE90', '#98FB98', '#87D68D', '#8FBC8F']
    tree_yellow = ['#9ACD32', '#BDB76B', '#F0E68C']
    tree_blue = ['#4682B4', '#5F9EA0', '#6495ED']
    trunk_colors = ['#3B2F2F', '#4B3621', '#654321', '#5C4033']
    
    for i in range(num_trees):
        # Position trees at different locations
        tree_x = width * (0.2 + i * 0.3)
        tree_base_y = height * 0.25
        tree_top_y = height * 0.55
        
        # Draw trunk with brown dots
        for _ in range(300):
            x = np.random.normal(tree_x, 2)
            y = np.random.uniform(tree_base_y, tree_base_y + (tree_top_y - tree_base_y) * 0.4)
            color = np.random.choice(trunk_colors)
            size = np.random.uniform(2, 4)
            ax.scatter(x, y, c=color, s=size, alpha=0.8, linewidths=0)
        
        # Draw foliage with mixed color dots
        foliage_dots = 3000
        for _ in range(foliage_dots):
            # Create roughly circular crown
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0, 15)
            x = tree_x + radius * np.cos(angle)
            y = tree_top_y + radius * np.sin(angle) * 1.2  # Slightly taller than wide
            
            # Mix colors for optical blending
            color_choice = np.random.random()
            if color_choice < 0.4:
                color = np.random.choice(tree_dark)
            elif color_choice < 0.65:
                color = np.random.choice(tree_light)
            elif color_choice < 0.85:
                color = np.random.choice(tree_yellow)
            else:
                color = np.random.choice(tree_blue)
            
            size = np.random.uniform(1.5, 4)
            ax.scatter(x, y, c=color, s=size, alpha=0.7, linewidths=0)


def draw_water(ax, width, height, num_dots=40000):
    """
    Draw a water area using blue, cyan, and white dots for reflective effect.
    """
    water_blue = ['#1E90FF', '#4682B4', '#5F9EA0', '#6495ED']
    water_cyan = ['#00CED1', '#48D1CC', '#40E0D0', '#AFEEEE']
    water_white = ['#E0FFFF', '#F0FFFF', '#FFFFFF']
    
    x_all, y_all, c_all, s_all = [], [], [], []
    
    # Water strip in lower portion
    for _ in range(num_dots):
        x = np.random.uniform(0, width)
        y = np.random.uniform(0, height * 0.2)
        
        # Add sparkles (white dots) randomly
        color_choice = np.random.random()
        if color_choice < 0.5:
            color = np.random.choice(water_blue)
        elif color_choice < 0.85:
            color = np.random.choice(water_cyan)
        else:
            color = np.random.choice(water_white)  # Sparkles
        
        size = np.random.uniform(1, 3.5)
        
        x_all.append(x)
        y_all.append(y)
        c_all.append(color)
        s_all.append(size)
    
    ax.scatter(x_all, y_all, c=c_all, s=s_all, alpha=0.6, linewidths=0)


def draw_figures(ax, width, height):
    """
    Draw simplified human figures using colorful dot clusters.
    """
    # Figure 1: Person in blue clothing
    figure1_x = width * 0.3
    figure1_y = height * 0.3
    
    # Head (skin tones)
    head_colors = ['#FFE4C4', '#F5DEB3', '#DEB887', '#D2B48C']
    for _ in range(200):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0, 3)
        x = figure1_x + radius * np.cos(angle)
        y = figure1_y + 10 + radius * np.sin(angle)
        color = np.random.choice(head_colors)
        size = np.random.uniform(2, 4)
        ax.scatter(x, y, c=color, s=size, alpha=0.8, linewidths=0)
    
    # Body (blue with white highlights)
    body_colors = ['#000080', '#0000CD', '#4169E1', '#1E90FF', '#FFFFFF']
    for _ in range(500):
        x = np.random.uniform(figure1_x - 5, figure1_x + 5)
        y = np.random.uniform(figure1_y - 10, figure1_y + 8)
        color = np.random.choice(body_colors)
        size = np.random.uniform(2, 4)
        ax.scatter(x, y, c=color, s=size, alpha=0.75, linewidths=0)
    
    # Figure 2: Person in red clothing
    figure2_x = width * 0.7
    figure2_y = height * 0.28
    
    # Head
    for _ in range(180):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0, 2.8)
        x = figure2_x + radius * np.cos(angle)
        y = figure2_y + 9 + radius * np.sin(angle)
        color = np.random.choice(head_colors)
        size = np.random.uniform(2, 4)
        ax.scatter(x, y, c=color, s=size, alpha=0.8, linewidths=0)
    
    # Body (red with pink/white highlights)
    body_colors = ['#8B0000', '#DC143C', '#CD5C5C', '#FFB6C1', '#FFFFFF']
    for _ in range(450):
        x = np.random.uniform(figure2_x - 4, figure2_x + 4)
        y = np.random.uniform(figure2_y - 9, figure2_y + 7)
        color = np.random.choice(body_colors)
        size = np.random.uniform(2, 4)
        ax.scatter(x, y, c=color, s=size, alpha=0.75, linewidths=0)


def main():
    """
    Main function to create the Pointillist painting.
    """
    print("Creating Georges Seurat-style Pointillist painting using Matplotlib...")
    print("正在创建乔治·修拉风格点彩画...")
    
    # Set up high DPI figure for better quality
    fig, ax = plt.subplots(figsize=(12, 9), dpi=150)
    
    # Set canvas dimensions
    width, height = 100, 75
    
    # Set white background
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    print("Drawing sky... / 绘制天空...")
    draw_sky(ax, width, height)
    
    print("Drawing grass with optical color mixing... / 绘制草地（光学混色）...")
    draw_grass(ax, width, height)
    
    print("Drawing water... / 绘制水面...")
    draw_water(ax, width, height)
    
    print("Drawing trees... / 绘制树木...")
    draw_trees(ax, width, height)
    
    print("Drawing figures... / 绘制人物...")
    draw_figures(ax, width, height)
    
    # Remove axes for cleaner look
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    print("Complete! / 完成！")
    
    # Save the figure
    output_file = 'seurat_pointillism_matplotlib.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"Saved to {output_file}")
    
    print("\nNote: The painting uses optical color mixing - notice how yellow and blue")
    print("dots create the illusion of green in the grass when viewed from a distance!")
    
    # Close the figure to free memory
    plt.close(fig)


if __name__ == "__main__":
    main()
