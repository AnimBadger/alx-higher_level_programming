#!/usr/bin/env node

const passed = process.argv.slice(2)
const firstPass = passed[0]
const secondPass = passed[1]

function add (a, b) {
  return a + b
}

console.log(add(Number(firstPass), Number(secondPass)))
