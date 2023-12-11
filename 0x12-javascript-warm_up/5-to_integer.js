#!/usr/bin/node

const value = Number(process.argv[2]);
if (value) {
  console.log('My Number:', Math.floor(value));
} else {
  console.log('Not a number');
}
