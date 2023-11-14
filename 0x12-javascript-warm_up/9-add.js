#!/usr/bin/node

function add(a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);

  if (isNaN(numA) || isNaN(numB)) {
    console.log('NaN');
  } else {
    console.log(numA + numB);
  }
}

add(process.argv[2], process.argv[3]);
