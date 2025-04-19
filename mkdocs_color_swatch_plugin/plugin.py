from mkdocs.plugins import BasePlugin

from mkdocs_color_swatch_plugin.color_swatch import ColorSwatchExtension

EMBEDDED_CSS = """
<style>
.color-swatch {
  display: inline-block;
  width: 2em;
  height: 2em;
  margin: 0.2em 0.4em 0.2em 0;
  border: 0.1em solid #ccc;
  vertical-align: middle;
  position: relative;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.color-swatch:hover {
  transform: scale(1.1);
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
}
.color-swatch::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 120%;
  left: 50%;
  transform: translateX(-50%);
  background: #333;
  color: #fff;
  padding: 5px 8px;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  font-size: 0.75em;
  transition: opacity 0.3s ease;
  z-index: 10;
}
.color-swatch:hover::after {
  opacity: 1;
}

/* Toast-style copied notice */
.copied-toast {
  position: fixed;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  background: #2ecc71; /* fallback */
  color: white;
  padding: 0.5em 1em;
  border-radius: 0.5em;
  font-size: 1em;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
  z-index: 9999;
}
.copied-toast.show {
  opacity: 1;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.color-swatch').forEach(function (swatch) {
    swatch.addEventListener('click', function () {
      const tooltip = swatch.getAttribute('data-tooltip');
      if (!tooltip) return;
      const colorValue = tooltip.split('–')[0].trim();
      navigator.clipboard.writeText(colorValue).then(function () {
        showCopiedToast(colorValue);
      });
    });
  });

  function showCopiedToast(color) {
    let toast = document.querySelector('.copied-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'copied-toast';
      document.body.appendChild(toast);
    }
    toast.innerText = 'Color copied to clipboard!';
    toast.style.backgroundColor = color;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2000);
  }
});
</script>
"""


class ColorSwatchPlugin(BasePlugin):
    config_scheme = ()

    def on_config(self, config, **kwargs):
        config['markdown_extensions'].append(ColorSwatchExtension())
        return config

    def on_page_content(self, html, **kwargs):
        if 'class="color-swatch"' in html:
            html = EMBEDDED_CSS + '\n' + html
        return html
