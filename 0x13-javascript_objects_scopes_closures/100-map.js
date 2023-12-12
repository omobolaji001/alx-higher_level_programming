#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (n, index) {
  return n * index;
});

console.log(list);
console.log(newList);
