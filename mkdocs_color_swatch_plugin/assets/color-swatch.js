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
        // Create or find toast container
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        // Create individual toast
        const toast = document.createElement('div');
        toast.className = 'copied-toast';
        toast.style.backgroundColor = '#2ecc71';
        toast.innerHTML = `
        <div>
            <span>Copied <strong>${color}</strong> to clipboard!<span>
            <span class="close-toast" title="Dismiss">×</span>
        </div>
    `;

        // Close manually
        toast.querySelector('.close-toast').addEventListener('click', () => {
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        });

        // Auto-remove after 2 seconds
        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        }, 2000);

        container.appendChild(toast);
    }
});