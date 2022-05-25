var swiper;
var nuberOfCardsPerSlide;

var viewport_width = document.documentElement.clientWidth;
if (viewport_width < 400) {
  nuberOfCardsPerSlide = 1;
} else if (viewport_width < 800) {
  nuberOfCardsPerSlide = 2;
} else {
  nuberOfCardsPerSlide = 3;
}
swiper = new Swiper(".mySwiper", {
  slidesPerView: nuberOfCardsPerSlide,
  spaceBetween: 30,

  loop: false,
  autoplay: {
    delay: 2500,
  },
  loopFillGroupWithBlank: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 2,
      spaceBetween: 10,
      slidesPerGroup: 1,
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 3,
      spaceBetween: 20,
      slidesPerGroup: 2,
    },
    // when window width is >= 640px
    640: {
      slidesPerView: 4,
      spaceBetween: 30,
      slidesPerGroup: 3,
    },
  },
});
