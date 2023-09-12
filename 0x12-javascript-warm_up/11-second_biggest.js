#!/usr/bin/node
function secondBiggest (args) {
  if (args.length <= 2) {
    return 0;
  } else {
    // Sort the arguments in ascending order and convert them to integers
    const sortedArgs = args.map(Number).sort((a, b) => a - b);

    // Get the second-to-last element (second biggest)
    return sortedArgs[sortedArgs.length - 2];
  }
}

const args = process.argv.slice(2); // Remove the first two elements (script name and node command)
const result = secondBiggest(args);
console.log(result);
