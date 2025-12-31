/* ================= IMAGE MODAL ================= */
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".gallery-card").forEach(card => {
        card.addEventListener("click", () => {
            const img = card.querySelector(".gallery-img");
            const isAuth = img.dataset.auth === "1";

            if (!isAuth) {
                window.location.href = "/login/";
                return;
            }

            openImage(img.dataset.full);
        });
    });
});



function openImage(src) {
    const modal = document.getElementById("imageModal");
    const img = document.getElementById("modalImg");
    if (!modal || !img) return;

    img.src = src;
    modal.style.display = "flex";
}

function closeImage(e) {
    if (e.target.id === "imageModal" || e.target.id === "modalImg") {
        document.getElementById("imageModal").style.display = "none";
    }
}

/* ================= HERO SLIDER ================= */
document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide");
    if (!slides.length) return;

    let index = 0;
    slides[index].classList.add("active");

    setInterval(() => {
        slides[index].classList.remove("active");
        index = (index + 1) % slides.length;
        slides[index].classList.add("active");
    }, 5000);
});

/* ================= MOBILE MENU ================= */
function toggleMenu() {
    const menu = document.getElementById("mobileMenu");
    if (menu) menu.classList.toggle("active");
}

/* ================= RESERVATION TIME BUTTONS ================= */




