// Select the element with id character
const character = document.querySelector('#character');

// Fetch the character data
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    character.textContent = data.name;
  });
