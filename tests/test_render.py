import markdown
import pytest

from mkdocs_color_swatch_plugin.color_swatch import ColorSwatchExtension

# Global Markdown instance that can be reused
md = markdown.Markdown(extensions=[ColorSwatchExtension()])


@pytest.mark.parametrize("input_md,expected_style", [
    (":color[#3498db]:", "background-color: #3498db;"),
    (":color[#fff]:", "background-color: #fff;"),
    (":color[rgb(255,0,0)]:", "background-color: rgb(255,0,0);"),
    (":color[rgba(10,20,30,0.5)]:", "background-color: rgba(10,20,30,0.5);"),
])
def test_color_swatch_renders_correctly(input_md, expected_style):
    # Use global Markdown instance, but reset between tests
    md.reset()
    html = md.convert(input_md)

    assert 'class="color-swatch"' in html
    assert expected_style in html

    # Tooltip should show the color code
    code_start = input_md.find('[') + 1
    code_end = input_md.find(']')
    color_code = input_md[code_start:code_end].strip()

    assert f'data-tooltip="{color_code}"' in html


@pytest.mark.parametrize("invalid_md", [
    ":color[#12g]:",  # Invalid hex
    ":color[rgb(100,200)]:",  # Missing channel
    ":color[rgba(10,20,30)]:",  # Missing alpha
    ":color[rgba(10,20,30,foo)]:",  # Invalid alpha
    ":color[#fff|]:",  # Pipe with nothing
    ":color[red]:",  # Named color not supported
])
def test_color_swatch_does_not_render_on_invalid(invalid_md):
    md.reset()
    html = md.convert(invalid_md)
    assert 'class="color-swatch"' not in html
