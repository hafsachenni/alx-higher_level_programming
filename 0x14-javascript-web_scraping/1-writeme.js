#!/usr/bin/node
// this is a script that writes a str to a file
const pathTofile = process.argv[2];
const stringTowrite = process.argv[3];
const fs = require('fs');
fs.writeFile(pathTofile, stringTowrite,'utf-8', function(error) {
    if (error) console.error(error);
});
