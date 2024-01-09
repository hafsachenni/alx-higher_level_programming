#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let i = 0; i <= list.length; i++) {
    /* checks if current element is equal to the element */
    /* we are searching for */
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
