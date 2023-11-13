#!/usr/bin/node

const a = parseInt(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    let result = 1;
    let i = a;
    while (i > 1) {
      result *= i;
      i--;
    }
    return result;
  }
}

console.log(factorial(a));
