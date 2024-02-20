#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const url = process.argv[2];
const request = require('request');
const fs = require('fs');
const pathTofile = process.argv[3];
request.get(url).pipe(fs.createWriteStream(pathTofile));
