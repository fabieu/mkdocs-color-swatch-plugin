from markdown import Markdown

from mkdocs_color_swatch_plugin.color_swatch import ColorSwatchExtension
from mkdocs_color_swatch_plugin.plugin import ColorSwatchPlugin, EMBEDDED_CSS

# Global instances to reuse across all tests
MARKDOWN_ENGINE = Markdown(extensions=[ColorSwatchExtension()])
PLUGIN = ColorSwatchPlugin()


def render_markdown(text, use_plugin=False):
    html = MARKDOWN_ENGINE.convert(text)
    if use_plugin:
        html = PLUGIN.on_page_content(html)
    return html


def test_swatch_renders_html():
    html = render_markdown('[[color: #e74c3c | Red]]')
    assert 'class="color-swatch"' in html
    assert 'data-tooltip="#e74c3c – Red"' in html


def test_plain_text_has_no_swatch():
    html = render_markdown('This is just plain text.')
    assert 'class="color-swatch"' not in html


def test_css_injected_when_needed():
    html = render_markdown('[[color: #3498db | Blue]]', use_plugin=True)
    assert EMBEDDED_CSS.strip() in html
    assert 'class="color-swatch"' in html


def test_css_not_injected_for_plain_text():
    html = render_markdown('Nothing to see here.', use_plugin=True)
    assert EMBEDDED_CSS.strip() not in html


def test_rgb_and_rgba_colors_render():
    html = render_markdown('[[color: rgb(255,0,0) | Red]]')
    assert 'rgb(255,0,0)' in html

    html = render_markdown('[[color: rgba(0,255,0,0.5) | Transparent Green]]')
    assert 'rgba(0,255,0,0.5)' in html
