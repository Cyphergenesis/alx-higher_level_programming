#!/usr/bin/node
function fac (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * fac(n - 1);
  }
}
const num = parseInt(process.argv[2]);
const result = fac(num);
console.log(result);
