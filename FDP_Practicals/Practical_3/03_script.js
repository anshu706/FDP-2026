// Update footer year
document.getElementById("year").textContent = new Date().getFullYear();

// Fake contact form handler
document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Thanks for your message! This is a demo form.");
  this.reset();
});