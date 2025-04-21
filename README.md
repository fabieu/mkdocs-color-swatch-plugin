# 🎨 Color Swatch Plugin for [MkDocs](https://www.mkdocs.org/)

> A lightweight plugin that lets you insert inline color swatches into your Markdown docs using a simple, readable
> syntax.

[![PyPI](https://img.shields.io/pypi/v/mkdocs-color-swatch-plugin)](https://pypi.org/project/mkdocs-color-swatch-plugin/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-color-swatch-plugin)](https://pypi.org/project/mkdocs-color-swatch-plugin/)
[![GitHub pipeline status](https://img.shields.io/github/actions/workflow/status/fabieu/mkdocs-color-swatch-plugin/build.yml)](https://github.com/fabieu/mkdocs-color-swatch-plugin/actions)
[![GitHub issues](https://img.shields.io/github/issues-raw/fabieu/mkdocs-color-swatch-plugin)](https://github.com/fabieu/mkdocs-color-swatch-plugin/issues)
[![GitHub merge requests](https://img.shields.io/github/issues-pr/fabieu/mkdocs-color-swatch-plugin)](https://github.com/fabieu/mkdocs-color-swatch-plugin/pulls)
[![GitHub](https://img.shields.io/github/license/fabieu/mkdocs-color-swatch-plugin)](https://github.com/fabieu/mkdocs-color-swatch-plugin/blob/main/LICENSE)

## ⭐ Features

- Styled swatches with smooth hover animations and tooltips
- Responsive swatches for all screen sizes
- Supports various color formats:
  - Hex colors - `#ff0000`/`#f00`
  - RGB colors - `rgb(255, 0, 0)`
  - RGBA colors - `rgba(255, 0, 0, 0.5)`
- No CSS setup required — styles are embedded automatically

**Visit demo:** https://fabieu.github.io/mkdocs-color-swatch-plugin/

---

## 🚀 Installation

### Prerequisites

- [MkDocs](https://www.mkdocs.org/) >= 1.4.X
- [Python](https://www.python.org/) >= 3.10

Install the plugin from [PyPI](https://pypi.org/project/mkdocs-color-swatch-plugin/) using `pip`:

```bash
pip install mkdocs-color-swatch-plugin
```

Then enable it in your `mkdocs.yml`:

```yaml
plugins:
  - color-swatch
```

Make sure you have `mkdocs` installed:

```bash
pip install mkdocs
```

---

## ✍️ Syntax & Usage

To add swatches to your Markdown, use the simple, custom inline format:

```markdown
:color[#e74c3c]: -> Red
:color[rgb(52, 152, 219)]: -> Green
:color[rgba(46, 204, 113, 0.6)]: -> Blue
```

Each tag will render as:

- A visual color preview
- Dynamically generated **tooltips** showing the color value and label
- A smooth **hover animation** for swatch elements

---

## 🧠 Why Use This Plugin?

Instead of manually writing HTML for every color sample like:

```html
<span style="background-color: #e74c3c; width: 30px; height: 30px; ..."></span>
```

You can just write:

```markdown
:color[#e74c3c]:  
```

It's faster, cleaner, and scales dynamically with your content.

---

## 💡 Features & Benefits

- 🎨 Works with all valid `hex`, `rgb()`, and `rgba()` color values
- 🎯 Simple syntax for embedding colors directly in your Markdown files
- 🛠 Automatically injected CSS for responsive and visually appealing swatches
- 🔄 Perfectly safe to use with other Markdown extensions
- 🔍 Live color preview in rendered HTML files, complete with tooltips

---

## 🛠 Development & Contribution

### 👨‍💻 Repository Setup:

Clone the project repository and configure the environment with Poetry:

```bash
git clone https://github.com/yourusername/mkdocs-color-swatch-plugin.git
cd mkdocs-color-swatch-plugin
poetry install
```

### Editable Install (for local use):

```bash
poetry install
pip install -e .
```

This allows you to test your changes directly when running MkDocs locally.

---

## 📄 License

MIT © [Fabian Eulitz](https://github.com/fabieu)

---

## 📎 Resources

- [mkdocs-color-swatch-plugin on PyPI](https://pypi.org/project/mkdocs-color-swatch-plugin/)
- [mkdocs-color-swatch-plugin on GitHub](https://github.com/fabieu/mkdocs-color-swatch-plugin)
- [MkDocs Documentation](https://www.mkdocs.org/)

