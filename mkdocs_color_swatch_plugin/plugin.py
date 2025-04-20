from pathlib import Path

from bs4 import BeautifulSoup
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

from mkdocs_color_swatch_plugin.color_swatch import ColorSwatchExtension


class ColorSwatchPlugin(BasePlugin):
    ASSET_DIR = Path(__file__).parent / "assets"
    CSS_PATH = ASSET_DIR / "color-swatch.css"
    JAVASCRIPT_PATH = ASSET_DIR / "color-swatch.js"

    def __init__(self) -> None:
        self.css_content = self._read_content(self.CSS_PATH)
        self.javascript_content = self._read_content(self.JAVASCRIPT_PATH)

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
        config['markdown_extensions'].append(ColorSwatchExtension())
        return config

    def on_post_page(self, html_output: str, /, *, page: Page, config: MkDocsConfig) -> str | None:
        soup_content = BeautifulSoup(html_output, 'html.parser')

        self._inject_css(soup_content)
        self._inject_js(soup_content)

        return str(soup_content)

    def _read_content(self, path: Path) -> str:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        return path.read_text(encoding="utf-8")

    def _inject_css(self, soup: BeautifulSoup) -> None:
        if self.css_content and soup.head:
            style_tag = soup.new_tag("style")
            style_tag.string = self.css_content
            soup.head.append(style_tag)

    def _inject_js(self, soup_content: BeautifulSoup) -> None:
        if self.javascript_content and soup_content.body:
            script_tag = soup_content.new_tag("script")
            script_tag.string = self.javascript_content
            soup_content.body.append(script_tag)
