document.addEventListener("DOMContentLoaded", function() {
    const revealButtons = document.querySelectorAll(".reveal-code");
    revealButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        this.classList.toggle("clicked");
      });
    });
  });
  