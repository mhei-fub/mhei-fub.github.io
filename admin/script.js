const menu = `<div class="menu"><div class="accordion"><div class="contentBox"><div class="label"><a href="index.html">Research</a></div><div class="content"></div></div><div class="contentBox"><div class="label"><a href="people.html">People</a></div><div class="content"></div></div><div class="contentBox"><div class="label">Alto parana atlantic forest</div><div class="content"><a href="field-trip-2023.html">Field Trip 2023</a></div></div><div class="contentBox"><div class="label">Mexico</div><div class="content"><a href="evaluating-socio-environmental-justice.html">Evaluating Socio-Environmental justice</a></div></div></div><button class="button" id="Btn"><i class="bx bx-menu bx-burst" style="color: #54d82d"></i></button>`;

class NavbarComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = menu;
        this.setupToggle();
        this.setupAccordion();
    }

    setupToggle() {
        const button = this.querySelector("#Btn");
        const icon = button.querySelector("i");
        button.addEventListener("click", () => {
            const accordion = this.querySelector(".accordion");
            const isVisible = accordion.style.display === "block";

            accordion.style.display = isVisible ? "none" : "block";
            const isActive = button.classList.toggle("active", !isVisible);

            button.style.position = isActive ? "relative" : "absolute";

            if (icon.classList.contains('bx-menu')) {
                icon.classList.remove('bx-menu', 'bx-burst');
                icon.classList.add('bx-x', 'bx-burst');
            } else {
                icon.classList.remove('bx-x', 'bx-burst');
                icon.classList.add('bx-menu', 'bx-burst');
            }

            const iframes = document.querySelectorAll("iframe");
            iframes.forEach(iframe => {
                iframe.style.display = isVisible ? "block" : "none";
            });
        });
    }

    setupAccordion() {
        const accordion = this.querySelector(".accordion");
        accordion.addEventListener("click", (event) => {
            if (event.target.classList.contains("label")) {
                const contentBox = event.target.parentElement;
                const isActive = contentBox.classList.contains("active");
                accordion.querySelectorAll(".contentBox").forEach(box => {
                    box.classList.remove("active");
                    box.querySelector(".content").style.maxHeight = null;
                });
                if (!isActive) {
                    contentBox.classList.add("active");
                    const content = contentBox.querySelector(".content");
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            }
        });
    }
}

customElements.define('custom-navbar', NavbarComponent);