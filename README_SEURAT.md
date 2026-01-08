# 乔治·修拉风格点彩画 / Georges Seurat-Style Pointillist Painting

## 作品说明 / Description

这是一个使用Python Turtle库创建的点彩画程序，灵感来源于乔治·修拉（Georges Seurat）的名作《大碗岛的星期日下午》（A Sunday Afternoon on the Island of La Grande Jatte）。程序完全遵循点彩派的核心技法，使用密集排列的小色点来构建画面。

This is a pointillist painting program created using Python's Turtle library, inspired by Georges Seurat's masterpiece "A Sunday Afternoon on the Island of La Grande Jatte". The program fully adheres to the core techniques of pointillism, using densely arranged small color dots to build the image.

## 技术特点 / Technical Features

### 1. 点彩技法 / Pointillist Technique
- **色点尺寸**：统一使用3像素的点 / **Dot Size**: Uniform 3-pixel dots
- **点间距**：相邻色点间距1像素 / **Spacing**: 1 pixel between adjacent dots
- **绘制方法**：全程使用`turtle.dot(size, color)`方法 / **Drawing Method**: Exclusively using `turtle.dot(size, color)`
- **禁用技法**：完全摒弃线条和填充 / **Prohibited**: No lines or fills used

### 2. 场景元素 / Scene Elements
- **天空**：浅蓝色 + 白色点 / **Sky**: Light blue + white dots
  - 高光区域使用更多白色点
  - More white dots in highlighted areas
  
- **草地**：草绿 + 黄绿 + 土黄色点 / **Grass**: Green + yellow-green + tan dots
  - 近景使用较亮的黄绿色
  - Foreground uses brighter yellow-green
  - 阴影区域添加土黄色点
  - Tan dots added for shadow areas
  
- **河岸边缘**：棕色 + 黑色点 / **Riverbank**: Brown + black dots
  - 底部使用更多黑色表现阴影
  - More black at bottom for shadows
  
- **人物剪影**：两个简化人物 / **Figure Silhouettes**: Two simplified figures
  - 人物1：蓝色服饰（深蓝、天蓝、白色点）
  - Figure 1: Blue clothing (navy, sky blue, white dots)
  - 人物2：红色服饰（深红、粉红、白色点）
  - Figure 2: Red clothing (dark red, pink, white dots)

### 3. 色彩原理 / Color Principles
遵循点彩派色彩并置原理：
Following pointillist color juxtaposition principles:

- **高光区域**：白色 + 浅色点叠加 / **Highlights**: White + light color dots overlay
- **阴影区域**：深色点密集排列 / **Shadows**: Dense dark color dots
- **禁止混合色**：所有颜色都是纯色点 / **No Mixed Colors**: All colors are pure dots
- **视觉混合**：颜色在观者眼中混合 / **Optical Mixing**: Colors blend in viewer's eye

### 4. 性能优化 / Performance Optimization
- `turtle.speed(0)` - 最快绘图速度 / Fastest drawing speed
- `turtle.tracer(0)` - 关闭动画以提升效率 / Disable animation for efficiency
- `turtle.update()` - 绘制完成后一次性更新 / Update once after drawing
- `turtle.hideturtle()` - 隐藏海龟光标 / Hide turtle cursor

## 运行方法 / How to Run

### 环境要求 / Requirements
- Python 3.x
- tkinter库（通常随Python自带）/ tkinter library (usually comes with Python)

### 运行命令 / Run Command
```bash
python seurat_pointillism.py
```

或 / Or:
```bash
python3 seurat_pointillism.py
```

## 代码结构 / Code Structure

```
seurat_pointillism.py
│
├── setup_canvas()      # 初始化画布 / Initialize canvas
├── draw_sky()          # 绘制天空 / Draw sky
├── draw_grass()        # 绘制草地 / Draw grass
├── draw_riverbank()    # 绘制河岸 / Draw riverbank
├── draw_figures()      # 绘制人物 / Draw figures
└── main()              # 主函数 / Main function
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

1. **画布大小** / **Canvas Size**: 修改`screen.setup(width=800, height=600)`
2. **色点大小** / **Dot Size**: 修改`dot_size = 3`
3. **点间距** / **Spacing**: 修改`spacing = 1`
4. **颜色方案** / **Color Scheme**: 修改各函数中的颜色列表
5. **人物位置** / **Figure Position**: 修改`draw_figures()`中的坐标

## 参考资料 / References

- Georges Seurat: "A Sunday Afternoon on the Island of La Grande Jatte" (1884-1886)
- Neo-Impressionism and Pointillism techniques
- Color theory and optical mixing

## 作者 / Author

Created as part of the PyArt project - where code meets canvas.

## 许可证 / License

See LICENSE file in the repository root.
