from pathlib import Path

from bs4 import BeautifulSoup
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files, File
from mkdocs.structure.pages import Page

from mkdocs_color_swatch_plugin.color_swatch import ColorSwatchExtension


class ColorSwatchPlugin(BasePlugin):
    def __init__(self):
        self.plugin_src_dir = Path(__file__).parent / "assets"
        self.plugin_site_dir = None

    def on_config(self, config: MkDocsConfig, **kwargs):
        config.markdown_extensions.append(ColorSwatchExtension())

        self.plugin_site_dir = Path(config.site_dir) / "plugins" / "color-swatch"
        self.plugin_site_dir.mkdir(parents=True, exist_ok=True)

        return config

    def on_files(self, files: Files, config: MkDocsConfig, **kwargs) -> Files | None:
        for file in self.plugin_src_dir.iterdir():
            if file.is_file():
                files.append(
                    File(
                        path=str(file.relative_to(self.plugin_src_dir)),
                        src_dir=str(self.plugin_src_dir),
                        dest_dir=str(self.plugin_site_dir),
                        use_directory_urls=False,
                    )
                )

        return files

    def on_post_page(self, html_output: str, /, *, page: Page, config: MkDocsConfig, **kwargs) -> str | None:
        soup = BeautifulSoup(html_output, 'html.parser')

        # Only inject references if there are color swatches in the page
        if soup.find('span', class_='color-swatch'):
            self._inject_references(soup, config)

        return str(soup)

    def _inject_references(self, soup: BeautifulSoup, config: MkDocsConfig) -> None:
        for file in self.plugin_site_dir.iterdir():
            if not file.is_file():
                continue

            rel_path = file.relative_to(config.site_dir).as_posix()

            if file.suffix == '.css':
                link_tag = soup.new_tag("link", rel="stylesheet", href=rel_path)
                soup.head.append(link_tag)
            elif file.suffix in ('.js', '.javascript'):
                script_tag = soup.new_tag("script", src=rel_path)
                soup.body.append(script_tag)
