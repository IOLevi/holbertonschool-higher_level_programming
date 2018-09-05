#!/usr/bin/node

let ep = process.argv[2];
let url = `http://swapi.co/api/films/${ep}`;
let request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body)['title']);
});
