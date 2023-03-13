#!/usr/bin/node

const passed = process.argv.slice(2);
const firstPass = parseInt(passed[0]);

function factorial (a, memo = {}) {
  if (a in memo) {
    return memo[a];
  }
  if (isNaN(a) || a < 2) {
    return 1;
  } else {
    memo[a] = a * factorial(a - 1, memo);
    return memo[a];
  }
}

console.log(factorial(firstPass));
