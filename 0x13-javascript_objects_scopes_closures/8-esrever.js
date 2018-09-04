exports.esrever = function (list) {
  let a = [];

  while (list.length > 0) {
    a.push(list.pop());
  }

  return a;
};
