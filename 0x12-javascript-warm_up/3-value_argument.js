#!/usr/bin/node
const numArguments = process.argv.slice(2);// slices used to extract cmd line ars //
if (!numArguments) {
  console.log('No argument');
} else {
  console.log(numArguments[0]);
}
