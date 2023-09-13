#!/usr/bin/node

function addMeMaybe(number, theFunction) {
  const result = number + 1;
  theFunction(result);
}

module.exports = {
  addMeMaybe: addMeMaybe
};

