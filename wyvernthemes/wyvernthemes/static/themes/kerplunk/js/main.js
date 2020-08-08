$(document).ready(function(){
    "use strict";
});

/* Nav Fade */
$(window).scroll(function(){
    $(".navbar.header").css("opacity", 1 - $(window).scrollTop() / 250);
});
/* End Nav Fade */

/* Pre Loader */
/* $(window).on("load", function() {
    // Animate loader off screen
    $(".se-pre-con").fadeOut("slow");;
}); */
/* Pre Loader */