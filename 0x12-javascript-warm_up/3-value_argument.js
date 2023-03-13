#!/usr/bin/node

const passed = process.argv.slice(2);
if (passed[0] === undefined) {
  console.log('No argument');
} else {
  console.log(passed[0]);
}
