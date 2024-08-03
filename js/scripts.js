let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        slide.style.opacity = '0';
    });
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.opacity = '1';
    setTimeout(showSlides, 30000); // Change slide every 30 seconds
}

function plusSlides(n) {
    slideIndex += n;
    const slides = document.querySelectorAll('.slide');
    if (slideIndex > slides.length) { slideIndex = 1 }
    if (slideIndex < 1) { slideIndex = slides.length }
    slides.forEach((slide, index) => {
        slide.style.opacity = '0';
    });
    slides[slideIndex - 1].style.opacity = '1';
}

document.addEventListener('DOMContentLoaded', () => {
    showSlides();
});

