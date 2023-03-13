#!/usr/bin/env node

const passed = process.argv.slice(2);

let firstPass = passed[0];

if (isNaN(firstPass)) {
  console.log('Missing size');
} else {
  firstPass = parseInt(firstPass);
  for (let i = 0; i < firstPass; i++) {
    let row = '';
    for (let j = 0; j < firstPass; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
