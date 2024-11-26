let count = 0;

document.getElementById('radio1').checked = true;

function nextImage(){
    count++;
    if(count > 5){
        count = 1;
    }
}
setInterval(() => {
    nextImage();
    document.getElementById('radio' + count).checked = true;

}, 4000);

const swiper = new Swiper('.favorite__swiper', {
    loop: true,
    grabCursor: true,
    slidesPerView: 'auto',
    centeredSlides: 'auto'
});
document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('click', () => {
        item.classList.toggle('active');
    });
});
