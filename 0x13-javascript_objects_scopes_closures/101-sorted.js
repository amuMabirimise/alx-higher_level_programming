#!/usr/bin/node

const data = require('./101-data');

const newDict = {};

for (const userId in data.dict) {
  const occurrences = data.dict[userId];

  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

console.log(newDict);
