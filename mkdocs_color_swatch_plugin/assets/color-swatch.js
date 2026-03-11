const COLOR_SWATCH_SELECTOR = '.color-swatch';

function onCopy(colorSwatch) {
    colorSwatch.classList.add("clicked");
    setTimeout(() => colorSwatch.classList.remove("clicked"), 2000);
}

function onSwatchClick(colorSwatch) {
    const tooltipText = colorSwatch.dataset.tooltip?.trim();
    if (tooltipText) {
        navigator.clipboard.writeText(tooltipText).then(() => onCopy(colorSwatch));
    }
}

function initColorSwatches() {
    document.querySelectorAll(COLOR_SWATCH_SELECTOR).forEach(colorSwatch => {
        colorSwatch.addEventListener('click', () => onSwatchClick(colorSwatch));
    });
}

document.addEventListener('DOMContentLoaded', initColorSwatches);
