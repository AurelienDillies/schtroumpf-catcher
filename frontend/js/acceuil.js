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

let capture = 0;
let restant = 0;

function fetchJSONData() {
    fetch('./items/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            data.forEach(schtroumpf => {
                if (schtroumpf.capture === false) {
                    restant++;
                } else {
                    capture++;
                }
            });

            
            const attraper = document.querySelector(".attraper p");
            const restanter = document.querySelector(".restant p");

            animateCounter(attraper, capture);
            animateCounter(restanter, restant);
        })
        .catch(error => console.error('Failed to fetch data:', error));
}

document.addEventListener("DOMContentLoaded", () => {
    fetchJSONData();
});
