function animateCounter(el, target) {
    let duration = 2000;
    let start = 0;
    let startTime = null;

    function update(timestamp) {
        if (!startTime) startTime = timestamp;

        let progress = (timestamp - startTime) / duration;
        progress = Math.min(progress, 1);

        // calcule la valeur à afficher en fonction du temps
        let value = Math.floor(progress * target);

        el.textContent = value;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            el.textContent = target;
        }
    }

    requestAnimationFrame(update);
}

document.addEventListener("DOMContentLoaded", () => {
    const attraper = document.querySelector(".attraper p");
    const restant = document.querySelector(".restant p");

    animateCounter(attraper, 42);
    animateCounter(restant, 1580);
});
