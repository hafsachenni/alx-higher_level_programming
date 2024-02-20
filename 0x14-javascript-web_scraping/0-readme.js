#!/usr/bin/node
// reading from a file usinfs module
const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf8', function (error, data) {
  console.log(error || data);
});
