#!/usr/bin/node

const first = Number(process.argv[2]);
const second = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(first, second);
