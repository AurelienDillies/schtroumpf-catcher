function animateCounter(el, target) {
    let duration = 2000;
    let start = 0;
    let startTime = null;

    function update(timestamp) {
        if (!startTime) startTime = timestamp;

        let progress = (timestamp - startTime) / duration;
        progress = Math.min(progress, 1);

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

function fetchDataCounters() {
    // toujours repartir de zéro
    let capture = 0;
    let restant = 0;

    fetch(window.location.origin + "/items/")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            data.forEach(schtroumpf => {
                if (schtroumpf.capture) {
                    capture++;
                } else {
                    restant++;
                }
            });

            const captureEl = document.querySelector(".attraper p");
            const restantEl = document.querySelector(".restant p");

            if (captureEl) animateCounter(captureEl, capture);
            if (restantEl) animateCounter(restantEl, restant);
        })
        .catch(error => console.error("Failed to fetch data:", error));
}

// lancer au chargement
document.addEventListener("DOMContentLoaded", fetchDataCounters);


// secret
  document.querySelector(".secret").addEventListener("click", function () {
    // Ajoute la classe sur <body>
    document.body.classList.add("smurf-cursor");
  });