$(document).ready(function(){
    /* if ( $('.dateinput').prop('type') != 'date' ) $('.dateinput').datepicker(); */
});

/* Recaptcha */
function enableContact() {
  document.getElementById("contact-submit").disabled = false;
}

/* Back to Top Button */
backtopbutton = document.getElementById("back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    if(backtopbutton) {
        scrollFunction();
    }
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backtopbutton.style.display = "block";
  } else {
    backtopbutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
