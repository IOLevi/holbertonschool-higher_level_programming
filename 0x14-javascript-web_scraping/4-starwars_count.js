#!/usr/bin/node

let url = process.argv[2];
let request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let films = JSON.parse(body)['results'];
    let counter = 0;
    for (let film of films) {
      for (let guy of film['characters']) {
        if (guy === 'https://swapi.co/api/people/18/') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
