#!/usr/bin/node
// reading from a file
const fs = require('fs');
file_path = process.argv[2];
fs.readFile(file_path, 'utf8', function (error, data) {
  console.log(error || data);
});
