#!/usr/bin/node
const firstArg = process.argv[2];
const argNum = parseInt(firstArg);
if (!isNaN(argNum)) {
  console.log(`My number: ${argNum}`);
} else {
  console.log('Not a number');
}
