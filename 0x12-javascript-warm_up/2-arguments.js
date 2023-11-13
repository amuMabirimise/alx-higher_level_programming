#!/usr/bin/node

const MyArgument = process.argv.length - 2;

if (MyArgument === 0) {
  console.log('No argument');
} else if (MyArgument === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
