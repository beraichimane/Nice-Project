(function($){
		
    // Platinum Partner Slides
    $('.platinum-partner-slides').owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        margin: 30,
        autoplayHoverPause: true,
        autoplay: true,
        navText: [
            "<i class='icofont-rounded-left'></i>",
            "<i class='icofont-rounded-right'></i>"
        ],
        responsive: {
            0: {
                items:2,
            },
            768: {
                items:3,
            },
            1200: {
                items:5,
            }
        }
    });
    
}(jQuery));