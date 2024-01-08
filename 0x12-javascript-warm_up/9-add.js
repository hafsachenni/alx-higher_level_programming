#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const addFirst = parseInt(process.argv[2]);
const addSecond = parseInt(process.argv[3]);

if (isNaN(addFirst) || isNaN(addSecond)) {
  console.log('NaN');
} else {
  console.log(add(addFirst, addSecond));
}
