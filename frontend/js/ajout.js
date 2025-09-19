// Activer l’animation dès le rendu
document.addEventListener("DOMContentLoaded", () => {
    const markerEl = document.querySelector(".point-blanc"); 
    if (markerEl) {
        markerEl.classList.add("pulse");

        // Arrêter définitivement au clic
        markerEl.addEventListener("click", () => {
            markerEl.classList.remove("pulse");
        }, { once: true }); // "once" = le listener ne s’exécute qu’une seule fois
    }
});
    