# EncreMagique

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

EncreMagique is a powerful Python library that allows you to create stunning video effects in a magical way. By combining text, images, and animations, EncreMagique transforms your creativity into visual art.

## Name Origin

"EncreMagique" means "magic ink" in French.
We chose this name because it represents the core features of this library: through EncreMagique, you can turn ordinary materials and ideas into magical video effects. The name carries the essence of creativity and enchanting effects, just like the powerful functionalities offered by the library.

## Key Features

- **Magic Ink Effects**: EncreMagique provides a range of astonishing magic ink effects that can bring a touch of magic and enchantment to your videos.
- **Text Transformations**: With EncreMagique, you can transform text into dynamic effects, giving your videos a unique visual charm.
- **Image Transitions**: Converting images into video effects is another remarkable feature of EncreMagique, helping you turn static images into vivid and captivating visual stories.
- **Easy to Use**: EncreMagique offers a simple and intuitive API that allows users of all levels, from beginners to professional video creators, to easily harness its powerful capabilities.

## Installation

You can install EncreMagique using the following command:

```bash
pip install EncreMagique
```

Make sure you have Python 3.8 or above.

## Quick Start

Here's a simple example demonstrating how to use EncreMagique to create a video with magic ink effects and dynamic text:

```python
import EncreMagique as em

# Create a video object
video = em.Video(width=640, height=480)

# Add magic ink effect
video.add_effect(em.MagicInkEffect())

# Add dynamic text
text = em.Text("Hello, EncreMagique!", font_color=(255, 255, 255), font_size=24)
video.add_element(text, position=(320, 240))

# Render the video
video.render("my_video.mp4")
```

## Contribution

If you are interested in EncreMagique and would like to contribute code or improve its functionalities, feel free to submit an issue or create a pull request.

## License

EncreMagique is released under the MIT License. See the [LICENSE](https://github.com/yourusername/EncreMagique/blob/main/LICENSE) file for more details.