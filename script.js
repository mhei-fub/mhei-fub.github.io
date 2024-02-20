const menu = `<div class="navbar"><button class="arrow" id="Btn"><div class="arrow-bar arrow-bar1"></div><div class="arrow-bar arrow-bar2"></div></button></div><div class="menu-background"><div class="menu-content" id="menu"><a href="/">Home</a><a href="apaf.html">Alto Paraná Atlantic forests</a><a href="test.html">No title</a></div></div>`;
class NavbarComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = menu;
        }
    }
customElements.define('custom-navbar', NavbarComponent);

document.getElementById("Btn").addEventListener("click", function() {
    let menuContent = document.getElementById("menu"); // This is your menu content
    let menuBackground = document.querySelector(".menu-background"); // This is your menu background
    let arrow = document.getElementById("Btn");
    
    // Toggle for menu content
    if (menuContent.style.display === "none" || menuContent.style.display === "") {
        menuContent.style.display = "flex"; // Show menu content
        menuBackground.style.display = "block"; // Show menu background
        arrow.classList.add("active");
    } else {
        menuContent.style.display = "none"; // Hide menu content
        menuBackground.style.display = "none"; // Hide menu background
        arrow.classList.remove("active");
    }
});
