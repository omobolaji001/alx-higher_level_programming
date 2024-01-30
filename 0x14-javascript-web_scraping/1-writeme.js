#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
const filePath = process.argv[2];
const fileEncoding = 'utf8';

fs.writeFile(filePath, data, fileEncoding, (error) => {
  if (error) throw error;
});
