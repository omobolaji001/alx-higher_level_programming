#!/usr/bin/node

const value = process.argv[2];

if (typeof value === 'undefined') {
  console.log('No argument');
} else {
  console.log(value);
}
