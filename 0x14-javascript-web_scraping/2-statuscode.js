#!/usr/bin/node
// script that displays the status code of a GET request
const request = require('request');
const url = process.argv[2];
request.get(url).on('response', function (response) {
  // response event represents the HTTP res obj returned by the server
  console.log('Code:', response.statusCode);
});
