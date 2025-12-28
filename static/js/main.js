function openImage(src) {
    const modal = document.getElementById("imageModal");
    const img = document.getElementById("modalImg");
    img.src = src;
    modal.style.display = "flex";
}

function closeImage(e) {
    if (e.target.id === "imageModal") {
        document.getElementById("imageModal").style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide");
    let current = 0;

    setInterval(() => {
        slides[current].classList.remove("active");
        current = (current + 1) % slides.length;
        slides[current].classList.add("active");
    }, 5000);
});
function toggleMenu() {
    document.getElementById("mobileMenu").classList.toggle("active");
}

let slides = document.querySelectorAll('.slide');
let index = 0;

function showSlide(i) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[i].classList.add('active');
}

setInterval(() => {
    index = (index + 1) % slides.length;
    showSlide(index);
}, 5000); // هر 5 ثانیه

