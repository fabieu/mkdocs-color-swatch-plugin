import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

SWATCH_CLASS = 'color-swatch'

# Regex pattern for :color[#hex]:, :color[rgb(...)]:, :color[rgba(...)]: with no label support
COLOR_PATTERN = (
    r":color\[\s*"
    r"(#[0-9a-fA-F]{3,8}"
    r"|rgb\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*\)"
    r"|rgba\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*(?:\d*\.\d+|\d+)\s*\))"
    r"\s*]:"
)


class ColorSwatchExtension(Extension):
    """
    Provides functionality to extend Markdown with custom inline color swatches.

    This class integrates with the Markdown library to add support for processing
    and rendering color swatch patterns. It is intended to simplify working with
    inline color definitions and incorporate them seamlessly into Markdown content.

    :ivar config: Configuration options for the extension.
    :type config: dict
    """
    def extendMarkdown(self, md):
        """
        Extends the given Markdown instance by registering a custom inline processor for color swatch patterns.
        """
        md.inlinePatterns.register(ColorSwatchInlineProcessor(COLOR_PATTERN, md), 'color_swatch', 175)


class ColorSwatchInlineProcessor(InlineProcessor):
    """
    Processes inline color swatch markdown elements.

    This class extends the functionality of the Markdown InlineProcessor
    to identify and process inline color swatch elements. It parses color
    codes within inline markdown elements and replaces them with styled
    HTML elements that visually represent the color. This can be used for
    rendering markdown documents where color indicators are needed.

    :ivar pattern: Regex pattern used to match color swatch inline elements.
    :type pattern: str
    """

    def handleMatch(self, m: re.Match[str], data: str) -> tuple[etree.Element | str | None, int | None, int | None]:
        color_code = m.group(1)

        swatch = etree.Element('span')
        swatch.set('class', SWATCH_CLASS)
        swatch.set('style', f'background-color: {color_code};')
        swatch.set('data-tooltip', f'{color_code}')

        return swatch, m.start(0), m.end(0)
