// Select the element with id toggle_header
const toggleHeader = document.querySelector('#toggle_header');

// Select the header element
const header = document.querySelector('header');

// Add click event listener
toggleHeader.addEventListener('click', function () {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
