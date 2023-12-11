#!/usr/bin/node

const value = Math.floor(Number(process.argv[2]));
console.log(isNaN(value) ? 'Not a number' : `My number: ${value}`);
