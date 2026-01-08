#!/usr/bin/env python3
"""
Chinese Calligraphy Art Generator
Generates beautiful, colorful calligraphy of "2026 马到成功"
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib import patheffects
import os


def create_colorful_calligraphy():
    """Create a colorful calligraphy artwork of '2026 马到成功'"""
    
    # Create figure with high DPI for better quality
    fig, ax = plt.subplots(figsize=(16, 10), dpi=150)
    
    # Set background with gradient effect
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack((gradient, gradient))
    
    # Create a beautiful gradient background
    extent = [0, 10, 0, 10]
    ax.imshow(gradient, extent=extent, aspect='auto', cmap='RdYlBu_r', alpha=0.3)
    
    # Text to display
    text = "2026  马到成功"
    
    # Find Chinese font
    # Try to find a Chinese font, fallback to default
    chinese_fonts = [
        'WenQuanYi Zen Hei',  # Linux - installed
        'Noto Sans CJK SC',  # Noto Sans - installed
        'Noto Serif CJK SC',  # Noto Serif - installed
        'SimHei',  # Windows
        'STHeiti',  # Mac
        'DejaVu Sans',  # Fallback
        'Arial Unicode MS',
        'Source Han Sans CN',
    ]
    
    font_prop = None
    available_fonts = set([f.name for f in fm.fontManager.ttflist])
    
    for font_name in chinese_fonts:
        if font_name in available_fonts:
            font_prop = fm.FontProperties(family=font_name, size=80, weight='bold')
            print(f"✓ Using font: {font_name}")
            break
    
    if font_prop is None:
        # Try to directly load the font file
        font_files = [
            '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
        ]
        for font_file in font_files:
            if os.path.exists(font_file):
                font_prop = fm.FontProperties(fname=font_file, size=80)
                print(f"✓ Using font file: {font_file}")
                break
    
    if font_prop is None:
        print("⚠ Warning: No Chinese font found, using default")
        font_prop = fm.FontProperties(size=80, weight='bold')
    
    # Create multiple colored text layers for a vibrant effect
    colors = [
        '#FF1744',  # Red
        '#F50057',  # Pink
        '#D500F9',  # Purple
        '#651FFF',  # Deep Purple
        '#2979FF',  # Blue
        '#00E5FF',  # Cyan
        '#1DE9B6',  # Teal
        '#76FF03',  # Light Green
        '#FFEA00',  # Yellow
        '#FF9100',  # Orange
    ]
    
    # Main text position
    x_pos = 5
    y_pos = 5
    
    # Create rainbow effect by offsetting colored text slightly
    for i, color in enumerate(colors):
        offset = i * 0.015
        text_obj = ax.text(
            x_pos - offset, 
            y_pos + offset, 
            text,
            fontproperties=font_prop,
            fontsize=80,
            color=color,
            ha='center',
            va='center',
            alpha=0.7,
            rotation=0
        )
        
        # Add glow effect
        text_obj.set_path_effects([
            patheffects.withStroke(linewidth=3, foreground=color, alpha=0.5)
        ])
    
    # Add a main bold text on top with gradient-like color
    main_text = ax.text(
        x_pos, 
        y_pos, 
        text,
        fontproperties=font_prop,
        fontsize=80,
        color='#FFD700',  # Gold
        ha='center',
        va='center',
        weight='bold',
        alpha=0.9
    )
    
    # Add strong shadow/outline effect
    main_text.set_path_effects([
        patheffects.withStroke(linewidth=8, foreground='#8B0000', alpha=0.8),
        patheffects.Normal()
    ])
    
    # Add decorative elements
    # Add some artistic flourishes around the text
    circle_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    # Top decorative circles
    for i, color in enumerate(circle_colors):
        angle = i * (2 * np.pi / len(circle_colors))
        x = 5 + 3.5 * np.cos(angle)
        y = 5 + 2.5 * np.sin(angle)
        circle = plt.Circle((x, y), 0.3, color=color, alpha=0.4)
        ax.add_patch(circle)
    
    # Remove axes
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Add title
    fig.suptitle('Chinese Calligraphy Art', fontsize=20, color='#2C3E50', 
                 fontweight='bold', y=0.98)
    
    # Tight layout
    plt.tight_layout()
    
    # Save the image
    output_file = 'calligraphy_2026_马到成功.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', 
                facecolor='#FFF8DC', edgecolor='none')
    print(f"✨ Calligraphy artwork saved as: {output_file}")
    
    # Display the image
    plt.show()
    
    return output_file


if __name__ == "__main__":
    print("🎨 Creating beautiful Chinese calligraphy artwork...")
    print("📝 Text: '2026  马到成功' (2026 - Immediate Success)")
    output_file = create_colorful_calligraphy()
    print(f"✅ Done! Your colorful calligraphy is ready!")
