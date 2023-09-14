#!/usr/bin/node
const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

// Read the contents of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }

  // Read the contents of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

    // Concatenate the contents of both source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log(`Concatenated files ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
    });
  });
});

