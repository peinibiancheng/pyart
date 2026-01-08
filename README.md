# pyart
Where code meets canvas. A collection of generative art, algorithmic drawings, and digital recreations — all crafted with Python. From Van Gogh-inspired swirls to data-driven visualizations, this repo explores the intersection of programming, mathematics, and visual expression. ✨ One script. Infinite artworks.

## Artworks

### Sol LeWitt Wall Drawing (Geometric Lines)
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

**Requirements:** Python 3.x with tkinter support (standard library only)

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

**Requirements:** Python 3.x with tkinter support (standard library only)

### 🎨 Chinese Calligraphy - 2026 马到成功
Beautiful, colorful calligraphy celebrating the Year of the Horse with vibrant rainbow effects and artistic styling.

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
