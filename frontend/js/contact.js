document.getElementById("boutonEnvoyer").addEventListener("click", function () {
    // Afficher le pop-up
    const popup = document.getElementById("popup-message");
    popup.style.display = "block";

    // Attendre 2 secondes puis recharger la page
    setTimeout(() => {
        location.reload();
    }, 2000);
});
