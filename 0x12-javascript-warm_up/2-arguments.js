#!/usr/bin/node

const count = process.argv.length;
if (count < 3) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
