#!/usr/bin/node
const numArguments = process.argv[2];// extract cmd line args //
if (!numArguments) {
  console.log('No argument');
} else {
  console.log(numArguments);
}
