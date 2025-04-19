import xml.etree.ElementTree as ElementTree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

SWATCH_CLASS = 'color-swatch'

# Support hex, rgb(), rgba()
COLOR_RE = r'\[\[color:\s*(#[0-9a-fA-F]{3,6}|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+(?:\s*,\s*(?:\d+|\d*\.\d+))?\s*\))\s*\|\s*([^\]]+)\]\]'


class ColorSwatchExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(ColorSwatchInlineProcessor(COLOR_RE, md), 'color_swatch', 175)


class ColorSwatchInlineProcessor(InlineProcessor):
    def handleMatch(self, matcher, data):
        color_code = matcher.group(1)
        label = matcher.group(2)

        swatch = ElementTree.Element('span')
        swatch.set('class', SWATCH_CLASS)
        swatch.set('style', f'background-color: {color_code};')
        swatch.set('data-tooltip', f'{color_code} – {label}')

        wrapper = ElementTree.Element('div')
        wrapper.append(swatch)

        return wrapper, matcher.start(0), matcher.end(0)
