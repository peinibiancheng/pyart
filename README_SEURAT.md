# 乔治·修拉风格点彩画 / Georges Seurat-Style Pointillist Painting

## 作品说明 / Description

这是一个使用Python Matplotlib库创建的点彩画程序，灵感来源于乔治·修拉（Georges Seurat）的名作《大碗岛的星期日下午》（A Sunday Afternoon on the Island of La Grande Jatte）。程序完全遵循点彩派的核心技法，使用密集排列的小色点来构建画面，并通过光学混色原理实现色彩效果。

This is a pointillist painting program created using Python's Matplotlib library, inspired by Georges Seurat's masterpiece "A Sunday Afternoon on the Island of La Grande Jatte". The program fully adheres to the core techniques of pointillism, using densely arranged small color dots to build the image and achieving color effects through optical mixing.

## 技术特点 / Technical Features

### 1. 点彩技法 / Pointillist Technique
- **色点数量**：超过220,000个彩色点 / **Dot Count**: Over 220,000 colored dots
- **色点尺寸**：1-5像素随机变化 / **Dot Size**: Randomly varying between 1-5 pixels
- **绘制方法**：使用`ax.scatter()`方法 / **Drawing Method**: Using `ax.scatter()` method
- **高DPI输出**：150 DPI高质量图像 / **High DPI**: 150 DPI high-quality image output
- **透明度设置**：使用alpha值创造绘画质感 / **Alpha Values**: Using alpha for painterly texture

### 2. 场景元素 / Scene Elements
- **天空**：浅蓝色 + 白色点 (~80,000点) / **Sky**: Light blue + white dots (~80,000 dots)
  - 高光区域使用更多白色点
  - More white dots in highlighted areas
  
- **草地**：黄色 + 蓝色点光学混色创造绿色效果 (~100,000点) / **Grass**: Yellow + blue dots optically mixed to create green (~100,000 dots)
  - **核心特色**：使用黄色和蓝色点并置，从远处观看形成绿色视觉效果
  - **Key Feature**: Yellow and blue dots juxtaposed to create green visual effect from distance
  - 近景使用较亮的颜色和较大的点
  - Foreground uses brighter colors and larger dots
  - 添加棕色点作为阴影
  - Brown dots added for shadows
  
- **水面**：蓝色 + 青色 + 白色点 (~40,000点) / **Water**: Blue + cyan + white dots (~40,000 dots)
  - 白色点模拟水面反光
  - White dots simulate water reflections
  
- **树木**：3棵树，使用深浅绿色、黄色、蓝色点簇 / **Trees**: 3 trees using dark/light green, yellow, blue dot clusters
  - 每棵树约3,300点
  - Approximately 3,300 dots per tree
  - 棕色树干点簇
  - Brown trunk dot clusters
  
- **人物剪影**：两个简化人物 / **Figure Silhouettes**: Two simplified figures
  - 人物1：蓝色服饰（深蓝、天蓝、白色点）
  - Figure 1: Blue clothing (navy, sky blue, white dots)
  - 人物2：红色服饰（深红、粉红、白色点）
  - Figure 2: Red clothing (dark red, pink, white dots)

### 3. 色彩原理 / Color Principles
遵循点彩派色彩并置原理：
Following pointillist color juxtaposition principles:

- **光学混合**：黄色 + 蓝色点并置创造绿色效果 / **Optical Mixing**: Yellow + blue dots juxtaposed create green effect
- **高光区域**：白色 + 浅色点叠加 / **Highlights**: White + light color dots overlay
- **阴影区域**：深色点密集排列 / **Shadows**: Dense dark color dots
- **禁止混合色**：所有颜色都是纯色点 / **No Mixed Colors**: All colors are pure dots
- **视觉混合**：颜色在观者眼中混合 / **Visual Mixing**: Colors blend in viewer's eye

### 4. 性能优化 / Performance Optimization
- `figsize=(12, 9)` - 大尺寸画布 / Large canvas size
- `dpi=150` - 高分辨率输出 / High resolution output
- `alpha` values - 透明度创造层次感 / Alpha for depth and texture
- `linewidths=0` - 移除点的边框 / Remove dot borders for cleaner look
- `ax.axis('off')` - 隐藏坐标轴 / Hide axes for art display

## 运行方法 / How to Run

### 环境要求 / Requirements
- Python 3.x
- matplotlib>=3.10.0
- numpy>=2.0.0

### 安装依赖 / Install Dependencies
```bash
pip install -r requirements.txt
```

### 运行命令 / Run Command
```bash
python seurat_pointillism.py
```

或 / Or:
```bash
python3 seurat_pointillism.py
```

脚本将生成一个名为 `seurat_pointillism_matplotlib.png` 的高分辨率图像文件。
The script will generate a high-resolution image file named `seurat_pointillism_matplotlib.png`.

## 代码结构 / Code Structure

```
seurat_pointillism.py
│
├── create_dot_cluster()   # 创建点簇 / Create dot clusters
├── draw_sky()             # 绘制天空 / Draw sky
├── draw_grass()           # 绘制草地（光学混色）/ Draw grass (optical mixing)
├── draw_water()           # 绘制水面 / Draw water
├── draw_trees()           # 绘制树木 / Draw trees
├── draw_figures()         # 绘制人物 / Draw figures
└── main()                 # 主函数 / Main function
```

## 艺术背景 / Artistic Background

点彩画（Pointillism）是19世纪末新印象派的核心技法，由乔治·修拉和保罗·西涅克发展而来。这种技法的核心是：

Pointillism is a core technique of Neo-Impressionism from the late 19th century, developed by Georges Seurat and Paul Signac. The core of this technique is:

1. **光学混合**：使用纯色小点，让颜色在观者眼中混合
   **Optical Mixing**: Using pure color dots that blend in the viewer's eye

2. **科学色彩理论**：基于当时的色彩学研究
   **Scientific Color Theory**: Based on color science research of the time

3. **系统化创作**：精确控制色点的位置和颜色
   **Systematic Creation**: Precise control of dot position and color

## 自定义修改 / Customization

如果想修改画面效果，可以调整以下参数：
To modify the visual effect, you can adjust the following parameters:

1. **画布大小** / **Canvas Size**: 修改`figsize=(12, 9)` / Modify `figsize=(12, 9)`
2. **分辨率** / **Resolution**: 修改`dpi=150` / Modify `dpi=150`
3. **色点数量** / **Dot Count**: 修改各函数中的`num_dots`参数 / Modify `num_dots` in each function
4. **色点大小** / **Dot Size**: 修改`size_range`参数 / Modify `size_range` parameter
5. **透明度** / **Alpha**: 修改`alpha`值（0-1之间）/ Modify `alpha` value (between 0-1)
6. **颜色方案** / **Color Scheme**: 修改各函数中的颜色列表 / Modify color palettes in functions
7. **树木数量** / **Number of Trees**: 修改`num_trees`参数 / Modify `num_trees` parameter

## 输出示例 / Output Example

运行脚本后会生成一幅点彩画，展示：
After running the script, it generates a pointillist painting showing:

- 清晰的光学混色效果（草地中的黄色和蓝色点）
- Clear optical color mixing effect (yellow and blue dots in grass)
- 从远处观看时颜色自然融合
- Colors naturally blend when viewed from a distance
- 高分辨率输出适合打印和展示
- High-resolution output suitable for printing and display

## 参考资料 / References

- Georges Seurat: "A Sunday Afternoon on the Island of La Grande Jatte" (1884-1886)
- Neo-Impressionism and Pointillism techniques
- Color theory and optical mixing

## 作者 / Author

Created as part of the PyArt project - where code meets canvas.

## 许可证 / License

See LICENSE file in the repository root.
