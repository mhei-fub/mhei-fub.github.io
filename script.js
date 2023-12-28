const menu = `<div class="navbar"><button class="arrow" id="Btn"><div class="arrow-bar arrow-bar1"></div><div class="arrow-bar arrow-bar2"></div></button></div><div class="menu" id="menu"><a href="/">Home</a><a href="test3.html">Alto Paraná Atlantic forests</a><a href="test2.html">Alto Paraná Atlantic forests</a><a href="apaf.html">Alto Paraná Atlantic forests</a><a href="test1.html">Alto Paraná Atlantic forests</a><a href="test4.html">Alto Paraná Atlantic forests</a></div>`;
class NavbarComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = menu;
        }
    }
customElements.define('custom-navbar', NavbarComponent);

document.getElementById("Btn").addEventListener("click", function() {
    let menu = document.getElementById("menu");
    let arrow = document.getElementById("Btn");
    
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "flex";
        arrow.classList.add("active");
    } else {
        menu.style.display = "none";
        arrow.classList.remove("active");
    }
});