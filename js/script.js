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