#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) throw error;
    });
  } else {
    console.error('Unexpected response status code:', response.statusCode);
  }
});
