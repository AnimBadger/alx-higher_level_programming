#!/usr/bin/node

const passed = process.argv.slice(2);
const firstPassed = passed[0];

if (isNaN(firstPassed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(firstPassed));
}
