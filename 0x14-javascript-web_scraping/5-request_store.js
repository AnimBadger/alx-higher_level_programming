#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(path, body, 'utf-8');
  }
}
);
