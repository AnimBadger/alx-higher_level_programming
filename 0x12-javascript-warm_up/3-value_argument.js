#!/usr/bin/env node

const passed = process.argv.slice(2);
if (passed[0] === undefined) {
  console.log('No argument');
} else {
  passed.forEach(element => {
    console.log(element);
  });
}
