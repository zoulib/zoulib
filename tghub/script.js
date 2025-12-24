// MENU
const burger = document.getElementById("burger");
const closeBtn = document.getElementById("close");
const menu = document.getElementById("menu");
const overlay = document.getElementById("overlay");

let open = false;
function openMenu() {
    open = true;
    menu.classList.add("show");
    overlay.classList.remove("hidden");
    burger.textContent = "✕";
}
function closeMenu() {
    open = false;
    menu.classList.remove("show");
    overlay.classList.add("hidden");
    burger.textContent = "☰";
}
burger.onclick = () => open ? closeMenu() : openMenu();
closeBtn.onclick = closeMenu;
overlay.onclick = closeMenu;

const cursor = document.getElementById("cursor");
if (window.innerWidth >= 768) {
    let pos = {x: window.innerWidth/2, y: window.innerHeight/2};
    let mouse = {x: pos.x, y: pos.y};

    document.addEventListener("mousemove", e => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    function animate() {
        pos.x += (mouse.x - pos.x) * 0.15;
        pos.y += (mouse.y - pos.y) * 0.15;

        let dx = mouse.x - pos.x;
        let dy = mouse.y - pos.y;
        let dist = Math.sqrt(dx*dx + dy*dy);
        let scale = Math.min(Math.max(dist/100, 1), 1.8);

        cursor.style.transform = `translate(${pos.x}px, ${pos.y}px) translate(-50%, -50%) scaleX(${scale}) scaleY(${2-scale})`;

        requestAnimationFrame(animate);
    }
    animate();
} else {
    cursor.style.display = "none";
}

