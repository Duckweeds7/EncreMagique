# EncreMagique

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

[English](https://github.com/Duckweeds7/EncreMagique/blob/main/README_en.md)

EncreMagique 是一个强大的Python库，旨在让你以魔法般的方式创造令人惊叹的视频特效。通过结合文字、图片和动画，EncreMagique 可以将你的创意转化为视觉艺术作品。

## 名字由来

"EncreMagique" 是法语中魔法墨水的意思。
我们选择这个名字是因为它代表了这个库的核心特点：通过EncreMagique，你可以将平凡的素材和创意转变为魔法般的视频效果。这个名字蕴含着创造力和神奇效果，恰如库中所提供的强大功能。

## 特色功能

- **幻墨特效**：EncreMagique 提供了一系列令人惊叹的幻墨特效，可以让你的视频充满神奇和魔力。
- **文本转换**：利用 EncreMagique，你可以将文本转化为动态效果，为你的视频添加独特的视觉魅力。
- **图片转换**：将图片转化为视频特效是 EncreMagique 的又一绝技，帮助你将静态图片变成生动且有趣的视觉故事。
- **简单易用**：EncreMagique 提供了简洁、直观的API，让你能够轻松使用其中的功能，无论你是初学者还是专业视频创作者。

## 安装

你可以通过以下方式安装 EncreMagique：

```bash
pip install EncreMagique
```

确保你的Python版本在3.8或以上。

## 快速入门

下面是一个简单的示例，演示了如何使用 EncreMagique 创建一段具有幻墨特效和动态文本的视频：

```python
import EncreMagique as em

# 创建一个视频对象
video = em.Video(width=640, height=480)

# 添加幻墨特效
video.add_effect(em.MagicInkEffect())

# 添加动态文本
text = em.Text("Hello, EncreMagique!", font_color=(255, 255, 255), font_size=24)
video.add_element(text, position=(320, 240))

# 渲染视频
video.render("my_video.mp4")
```

## 贡献

如果你对 EncreMagique 感兴趣并想要贡献代码或改进功能，欢迎提交Issue或创建Pull Request。

## 许可证

EncreMagique 采用MIT许可证。详情请参阅 [LICENSE](https://github.com/yourusername/EncreMagique/blob/main/LICENSE) 文件。
