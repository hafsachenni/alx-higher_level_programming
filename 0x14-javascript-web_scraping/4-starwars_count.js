#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present
const apiUrl = process.argv[2];
const charId = 18;

const request = require('request');
request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const res = JSON.parse(body).results;

    let count = 0;
    for (const result of res) {
      const filmschars = result.characters;

      for (const film of filmschars) {
        if (film.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
