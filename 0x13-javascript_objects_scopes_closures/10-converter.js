#!/usr/bin/node
exports.converter = function (base) {
  function inner (mynum) {
    return mynum.toString(base);
  }

  return inner;
};
