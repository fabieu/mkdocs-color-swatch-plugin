const COLOR_SWATCH_SELECTOR = '.color-swatch';

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll(COLOR_SWATCH_SELECTOR).forEach(colorSwatch => {
        colorSwatch.addEventListener('click', () => {
            const tooltipText = colorSwatch.getAttribute('data-tooltip')?.trim();
            if (tooltipText) {
                copyToClipboard(tooltipText);
            }
        });
    });
});

const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
};