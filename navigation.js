function toggleNavMenu(event) {
  const dropdown = event.currentTarget.closest(".nav-dropdown");
  const isOpen = dropdown.classList.toggle("open");
  event.currentTarget.setAttribute("aria-expanded", isOpen ? "true" : "false");
}

document.addEventListener("click", function(event) {
  document.querySelectorAll(".nav-dropdown.open").forEach(function(dropdown) {
    if (!dropdown.contains(event.target)) {
      dropdown.classList.remove("open");
      const trigger = dropdown.querySelector(".nav-trigger");
      if (trigger) {
        trigger.setAttribute("aria-expanded", "false");
      }
    }
  });
});
