#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const fileEncoding = 'utf8';

fs.readFile(filePath, fileEncoding, (error, data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(data);
});
