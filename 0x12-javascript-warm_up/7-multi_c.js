#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!isNaN(x) && x > 0) {
  let count = 0;

  while (count < x) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
