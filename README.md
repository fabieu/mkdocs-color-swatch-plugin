# 🎨 MkDocs Color Swatch Plugin

A lightweight [MkDocs](https://www.mkdocs.org/) plugin that lets you insert inline color swatches into your Markdown docs using a simple, readable syntax.

Supports:
- ✅ Hex colors (`#ff0000`, `#f00`)
- ✅ RGB and RGBA (`rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`)
- ✅ Tooltip with color value + label
- ✅ Rounded swatches with smooth hover animations
- ✅ No CSS setup required — styles are embedded automatically

---

## 🚀 Installation

Install via [PyPI](https://pypi.org/):

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

## ✍️ Usage

In your Markdown, use the custom swatch syntax:

```markdown
[[color: #e74c3c | Red]]
[[color: rgb(52, 152, 219) | Blue]]
[[color: rgba(46, 204, 113, 0.6) | Transparent Green]]
```

Each tag will render as:

- A **rounded swatch** showing the color
- A **tooltip** with the color value + label
- A **hover effect** that scales and highlights the swatch

---

## 🧠 Why Use This Plugin?

Instead of manually writing HTML for every color sample like:

```html
<span style="background-color: #e74c3c; width: 30px; height: 30px; ..."></span>
```

You can just write:

```markdown
[[color: #e74c3c | Red]]
```

It's faster, cleaner, and works right out of the box.

---

## 🛠 Features

- 🔹 Works with any valid `hex`, `rgb()`, or `rgba()` color
- 🔹 Tooltip automatically shows `#hex – Label`
- 🔹 Embedded CSS — no setup needed
- 🔹 Safe to use alongside other Markdown extensions
- 🔹 Lightweight and dependency-free

---

## 📦 Development & Contribution

### Clone and Install:

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

---

## 🧪 Testing

Basic tests coming soon!

---

## 📄 License

MIT © [Fabian Eulitz](https://github.com/fabieu)

---

Made with ❤️
