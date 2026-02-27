// Select the element with id add_item
const addItem = document.querySelector('#add_item');

// Select the ul element with class my_list
const myList = document.querySelector('.my_list');

// Add click event listener
addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
