document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".sidebar li");

  items.forEach(item => {
    item.addEventListener("click", () => {
      const target = item.getAttribute("data-target");
      if (!target) return;

      // Update active class
      items.forEach(i => i.classList.remove("active"));
      item.classList.add("active");

      // Navigate to target page
      window.location.href = target;
    });
  });
});
