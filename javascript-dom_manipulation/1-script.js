// Select the element with id red_header
const redHeader = document.querySelector('#red_header');

// Select the header element
const header = document.querySelector('header');

// Add click event listener
redHeader.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
