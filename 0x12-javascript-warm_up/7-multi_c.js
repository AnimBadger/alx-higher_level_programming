#!/usr/bin/env node

const passed = process.argv.slice(2);

let firstPass = passed[0];

if (isNaN(firstPass)) {
  console.log('Missing number of occurrences');
} else {
  firstPass = parseInt(firstPass);
  for (let i = 0; i < firstPass; i++) {
    console.log('C is fun');
  }
}
