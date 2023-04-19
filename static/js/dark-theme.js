document.getElementById("dark-theme").addEventListener("click", function() {
  document.body.classList.toggle("dark-theme");
  if (document.body.classList.contains("dark-theme")) {
    document.getElementById("theme-icon").src = "{% static 'icons/sun.svg' %}";
  } else {
    document.getElementById("theme-icon").src = "{% static 'icons/dark.svg' %}";
  }
});
