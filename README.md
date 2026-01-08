# pyart
Where code meets canvas. A collection of generative art, algorithmic drawings, and digital recreations — all crafted with Python. From Van Gogh-inspired swirls to data-driven visualizations, this repo explores the intersection of programming, mathematics, and visual expression. ✨ One script. Infinite artworks.

## Artworks

### 🎨 Andy Warhol Pop Art
**File:** `warhol_pop_art.py`

An Andy Warhol-inspired Pop Art masterpiece using Matplotlib. Features:
- 2x2 grid displaying the same abstract portrait in each quadrant
- Four different high-contrast colormaps: Magma, Viridis, Cividis, and custom Neon
- Bold outlines simulating the iconic silkscreen printing effect
- Flat, saturated color fills with vibrant pop art aesthetics
- Mathematically generated abstract portrait with facial features
- High-resolution output (300 DPI) suitable for printing

**Run it:**
```bash
python warhol_pop_art.py
```

### 🎨 Picasso One-Line Drawing
**File:** `picasso_one_line.py`

Minimalist one-line drawings inspired by Picasso's famous continuous line works like his 'Penguin', 'Dog', and 'Camel'. Features:
- Single continuous elegant black stroke using Bézier curves
- Textured paper-colored background (warm beige/cream tone)
- Fluid movement and abstract simplicity
- Two variations: Dog and Penguin drawings
- Pure matplotlib implementation using `matplotlib.path.Path`
- Elegant minimalist aesthetic with rounded line caps and joins

**Run it:**
```bash
python picasso_one_line.py
```

### 🎨 Piet Mondrian Composition
**File:** `mondrian.py`

A Python recreation of Piet Mondrian's iconic geometric abstract art style using matplotlib. Features:
- Recursive space division creating rectangles of varying sizes
- Mondrian's signature color palette: Red (#DC143C), Blue (#0047AB), Yellow (#FFD700), and White
- Thick black borders (linewidth 6) between all rectangles
- Composition reminiscent of "Composition with Red Blue and Yellow"
- Mathematical approach to art with random variations in each generation

**Run it:**
```bash
python mondrian.py
```
```

### 🐴 Galloping Horse 2026
**File:** `galloping_horse_2026.py`

A dynamic horse artwork celebrating the Year 2026 with the Chinese idiom **马到成功** (immediate success). Features:
- Stylized galloping horse with flowing mane and tail
- Motion lines showing speed and energy
- Festive color palette: red, gold, and blue
- 2026 banner and success message
- Perfect for Lunar New Year celebrations

**Run it:**
```bash
python galloping_horse_2026.py
```

### 🌸 Geometric Mandala
**File:** `geometric_mandala.py`

An intricate circular pattern combining mathematical precision with artistic beauty. Features:
- 12-fold radial symmetry
- Multiple concentric layers with geometric designs
- Star patterns, flower petals, and decorative rings
- Vibrant color palette: purple, red, green, blue, and gold
- Mesmerizing symmetry and harmony

**Run it:**
```bash
python geometric_mandala.py
```

### Sol LeWitt Wall Drawing (Matplotlib)
**File:** `sol_lewitt_matplotlib.py`

A minimalist homage to Sol LeWitt's "Wall Drawing" series using Matplotlib for high-precision rendering. Features:
- 2x2 grid layout with dense, parallel lines in each quadrant
- Top-left: Horizontal lines
- Top-right: Vertical lines
- Bottom-left: Diagonal lines (45° northeast)
- Bottom-right: Diagonal lines (45° southeast)
- Thin black lines (0.5pt width) with perfect spacing (0.05 units)
- High-precision ax.plot() for crisp, professional output
- Shimmering minimalist effect true to LeWitt's conceptual art philosophy
- Saves high-resolution PNG (300 DPI)

**Run it:**
```bash
python sol_lewitt_matplotlib.py
```

### Sol LeWitt Wall Drawing (Turtle - Geometric Lines)
**File:** `sol_lewitt.py`

A homage to Sol LeWitt's "Wall Drawing" series using Python's turtle graphics module. Features:
- Canvas divided into four quadrants with distinct line orientations
- Quadrant 1 (top-right): Vertical lines in red
- Quadrant 2 (top-left): Horizontal lines in blue
- Quadrant 3 (bottom-left): Diagonal lines tilted 45° left in gold
- Quadrant 4 (bottom-right): Diagonal lines tilted 45° right in black
- Strict equal spacing of 10 pixels between lines
- Precise mathematical calculations using for loops and coordinate geometry
- Lines fill each quadrant completely without exceeding boundaries

**Run it:**
```bash
python sol_lewitt.py
```

### Spot Painting (Damien Hirst Inspired)
**File:** `spot_painting.py`

A Python recreation of Damien Hirst's iconic "Spot Paintings" using the turtle graphics module. Features:
- 10x10 grid of perfectly aligned colored circles
- High-saturation pop art color palette with random color selection
- Mathematical grid layout with consistent spacing and centering
- Clean, minimal aesthetic with solid fills and no borders
- Algorithmic composition inspired by Hirst's systematic approach to art

**Run it:**
```bash
python spot_painting.py
```

### Starry Night (Van Gogh Inspired)
**File:** `starry_night.py`

A Python recreation of Van Gogh's iconic "Starry Night" using the turtle graphics module. Features:
- Swirling sky patterns created with sine/cosine waves mimicking Van Gogh's distinctive brushstrokes
- Stylized flame-like cypress trees in the foreground
- Glowing moon with layered halos
- Strict color palette: `#1a5fb4` (blue), `#f7931a` (orange/yellow), and black

**Run it:**
```bash
python starry_night.py
```

### Sol LeWitt Geometric (Conceptual Art Inspired)
**File:** `sol_lewitt_geometric.py`

A Python simulation of Sol LeWitt's colorful geometric artworks using the turtle graphics module. Features:
- Multiple overlapping geometric shapes (squares, triangles, circles) with outline strokes
- Hatch line filling technique - shapes filled with parallel fine lines instead of solid colors
- Sol LeWitt's vibrant color palette: high-saturation red, yellow, blue, and black
- Dynamic randomization: each run generates unique stacking orders and line densities
- Optimized rendering with `tracer(0)` for instant display of complex linear textures

**Run it:**
```bash
python sol_lewitt_geometric.py
```

### Pointillism Art (Georges Seurat Inspired)
**File:** `seurat_pointillism.py`

A Python recreation of Georges Seurat's Pointillism technique using the turtle graphics module. Features:
- Thousands of small dots of pure color applied in patterns to form an image
- Optical color mixing: colors are mixed in the eye of the viewer rather than on the palette
- Thematic focus on light, shadow, and color theory
- High-density dot rendering using mathematical distributions
- Read more: [README_SEURAT.md](README_SEURAT.md)

**Run it:**
```bash
python seurat_pointillism.py
```

### 🎨 Chinese Calligraphy - 2026 马到成功
**File:** `calligraphy_2026.py`  
**Output:** High-quality PNG with gradient effects and Chinese characters  
**Read more:** [README_CALLIGRAPHY.md](README_CALLIGRAPHY.md)

**Run it:**
```bash
python calligraphy_2026.py
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt
```

For systems without Chinese fonts, install them first:
```bash
# Ubuntu/Debian
sudo apt-get install fonts-wqy-zenhei fonts-noto-cjk
```
