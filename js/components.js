class NavbarComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <div class="navbar">
                <button class="arrow" id="Btn">
                    <div class="arrow-bar arrow-bar1"></div>
                    <div class="arrow-bar arrow-bar2"></div>
                </button>
                
            </div>
            <div class="menu" id="menu">
                    <a href="/">Home</a>    
                    <a href="apaf.html">Alto Paraná Atlantic forests</a>
            </div>
            `;
        }
    }
customElements.define('custom-navbar', NavbarComponent);
