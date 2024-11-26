const profileIcon = document.getElementById('profileIcon');
const profileMenu = document.getElementById('profileMenu');

profileIcon.addEventListener('click', () => {
    profileMenu.style.display = profileMenu.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', (e) => {
    if (!profileMenu.contains(e.target) && e.target !== profileIcon) {
        profileMenu.style.display = 'none';
    }
});
document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        alert.classList.add('alert-show');
        
        // Fechar a notificação após 5 segundos
        setTimeout(() => {
            alert.classList.remove('alert-show');
            alert.classList.add('slideOut');
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const slidePrev = document.querySelector('.slide-prev');
    const slideNext = document.querySelector('.slide-next');
    const produtosRecentes = document.querySelector('.produtos-recentes');
    const produtoWidth = 250;
    const produtosPorSlide = 1;
    const totalSlides = Math.ceil(15 / produtosPorSlide);
    let currentSlide = 0;

    function updateSlidePosition() {
        const offset = -currentSlide * produtosPorSlide * produtoWidth;
        produtosRecentes.style.transform = `translateX(${offset}px)`;
    }

    slideNext.addEventListener('click', function(){
        if (currentSlide < totalSlides - 1) {
            currentSlide++;
            updateSlidePosition();
        }
    });

    slidePrev.addEventListener('click', function(){
        if (currentSlide > 0){
            currentSlide--;
            updateSlidePosition();
        }
    });
    updateSlidePosition();
});

const navbarToggle = document.querySelector('.navbar-toggle');
const navbarLinks = document.querySelector('.navbar-links');

navbarToggle.addEventListener('click', () => {
  navbarLinks.classList.toggle('active');
});