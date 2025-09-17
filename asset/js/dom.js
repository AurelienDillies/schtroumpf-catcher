function animateCounter(element, target, speed = 20) {
  let count = 0;
  let step = Math.ceil(target / 100);

  let interval = setInterval(() => {
    count += step;
    if (count >= target) {
      count = target;
      clearInterval(interval);
    }
    element.textContent = count;
  }, speed);
}

document.addEventListener("DOMContentLoaded", () => {
  animateCounter(document.querySelector(".attraper p"), 42);
  animateCounter(document.querySelector(".restant p"), 158);
});
