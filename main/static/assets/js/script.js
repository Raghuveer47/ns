'use strict';

/**
 * navbar toggle
 */

const overlay = document.querySelector("[data-overlay]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

const navToggleEvent = function (elem) {
  for (let i = 0; i < elem.length; i++) {
    elem[i].addEventListener("click", function () {
      navbar.classList.toggle("active");
      overlay.classList.toggle("active");
    });
  }
}

navToggleEvent(navElemArr);
navToggleEvent(navLinks);



/**
 * header sticky & go to top
 */

const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {

  if (window.scrollY >= 200) {
    header.classList.add("active");
    goTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    goTopBtn.classList.remove("active");
  }

});


$(document).ready(function() {
		$('#myModal').modal({
			backdrop: 'static', // Disable closing by clicking outside
			keyboard: false // Disable closing with keyboard
		});

		function adjustImageForMobile() {
			if ($(window).width() < 768) {
				$('#promoSection').css('background-image', 'url(https://res.cloudinary.com/dy9zlgjh6/image/upload/v1721236123/100_ip9pnw.webp)'); // Replace with your mobile image URL
			} else {
				$('#promoSection').css('background-image', 'url("https://res.cloudinary.com/dy9zlgjh6/image/upload/v1721236123/100_ip9pnw.webp")'); // Replace with your desktop image URL
			}
		}

		// Adjust image on document ready
		adjustImageForMobile();

		// Adjust image on window resize
		$(window).resize(function() {
			adjustImageForMobile();
		});

		// Form validation
		$('#offerForm').on('submit', function(event) {
			event.preventDefault(); // Prevent form submission
			let isValid = true;
			$('#offerForm input').each(function() {
				if (!$(this).val()) {
					isValid = false;
					$(this).addClass('is-invalid');
				} else {
					$(this).removeClass('is-invalid');
				}
			});
			if (isValid) {
				$('#myModal').modal('hide'); // Close modal if form is valid
			}
		});

		$('.btn').on('click', function(event) {
			if ($('#offerForm')[0].checkValidity() === false) {
				event.preventDefault();
				event.stopPropagation();
				$('#offerForm').addClass('was-validated');
			}
		});
	});


  document.querySelectorAll('[id^="book-now"]').forEach(button => {
    button.addEventListener('click', function() {
      document.getElementById('tour-search').scrollIntoView({ behavior: 'smooth' });
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
var whatsappButtons = document.getElementsByClassName("js-whatsapp");
var phoneNumber = "+919182063344"; // Your WhatsApp Business phone number with country code
var message = "Hello, I would like to know more about your services."; // Initial message sent to user

Array.prototype.forEach.call(whatsappButtons, function (button) {
  button.addEventListener("click", function (e) {
    e.preventDefault;
    var whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(
      message
    )}`;
    window.open(whatsappUrl, "_blank");
  });
});
});


$(document).ready(function() {
  $('#myModal').modal({
    backdrop: 'static', // Disable closing by clicking outside
    keyboard: false // Disable closing with keyboard
  });

  function adjustImageForMobile() {
    if ($(window).width() < 768) {
      $('#promoSection').css('background-image', 'url(https://res.cloudinary.com/dy9zlgjh6/image/upload/v1721236123/100_ip9pnw.webp)'); // Replace with your mobile image URL
    } else {
      $('#promoSection').css('background-image', 'url("https://res.cloudinary.com/dy9zlgjh6/image/upload/v1721236123/100_ip9pnw.webp")'); // Replace with your desktop image URL
    }
  }

  // Adjust image on document ready
  adjustImageForMobile();

  // Adjust image on window resize
  $(window).resize(function() {
    adjustImageForMobile();
  });

  // Form validation
  $('#offerForm').on('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    let isValid = true;
    $('#offerForm input').each(function() {
      if (!$(this).val()) {
        isValid = false;
        $(this).addClass('is-invalid');
      } else {
        $(this).removeClass('is-invalid');
      }
    });
    if (isValid) {
      $('#myModal').modal('hide'); // Close modal if form is valid
    }
  });

  $('.btn').on('click', function(event) {
    if ($('#offerForm')[0].checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
      $('#offerForm').addClass('was-validated');
    }
  });
});