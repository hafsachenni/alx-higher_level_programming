#!/usr/bin/node
// reading from a file that will be provided as cmd line arg
const fs = require('fs');
const file_path = process.argv[2];
fs.readFile(file_path, 'utf8', function (error, data) {
  console.log(error || data);
});
