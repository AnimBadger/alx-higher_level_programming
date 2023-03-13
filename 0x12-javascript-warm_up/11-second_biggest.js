#!/usr/bin/env node

const passed = process.argv.slice(2);
if (isNaN(passed[0]) || passed.length === 1) {
  console.log('0');
} else {
  const listedIntegers = passed.map(Number);
  const sorted = listedIntegers.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
