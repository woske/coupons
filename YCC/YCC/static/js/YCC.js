document.addEventListener("DOMContentLoaded", function() {
    const revealButtons = document.querySelectorAll(".reveal-code");
    revealButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        this.classList.toggle("clicked");
      });
    });
  });
  

  // Get the current date
  const currentDate = new Date();

  // Define an array of month names
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

  // Get the current month and year
  const currentMonth = monthNames[currentDate.getMonth()];
  const currentYear = currentDate.getFullYear();

  // Inject the current month and year into the placeholders
  document.getElementById("current-month").textContent = currentMonth;
  document.getElementById("current-year").textContent = currentYear;