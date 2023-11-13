#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
