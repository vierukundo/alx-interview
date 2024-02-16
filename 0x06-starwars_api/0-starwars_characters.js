#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const mainUrl = 'https://swapi-api.alx-tools.com/api/';
const url = `${mainUrl}films/${movieId}`;

function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        reject(new Error(`Error fetching character: ${error}`));
      }
    });
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const characters = JSON.parse(body).characters;

    // Use Promise.all to maintain the order of character names
    Promise.all(characters.map(characterUrl => fetchCharacter(characterUrl)))
      .then(names => {
        names.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error(error);
      });
  }
});
