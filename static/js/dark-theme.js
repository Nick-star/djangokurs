var darkThemeButton = document.getElementById("dark-theme");
document.getElementById("dark-theme").addEventListener("click", function() {
    document.body.classList.toggle("dark-theme");

    var svg = document.getElementById("theme-icon");
    if (document.body.classList.contains("dark-theme")) {
        svg.src = window.location.origin + "/static/icons/sun.svg";
    } else {
        svg.src = window.location.origin + "/static/icons/dark.svg";
    }
});
