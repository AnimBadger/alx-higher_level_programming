#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const index in films) {
      const filmchars = films[index].characters;
      for (const char in filmchars) {
        if (filmchars[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
