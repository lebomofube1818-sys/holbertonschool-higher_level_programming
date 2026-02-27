// Select the element with id update_header
const updateHeader = document.querySelector('#update_header');

// Select the header element
const header = document.querySelector('header');

// Add click event listener
updateHeader.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
