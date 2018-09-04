exports.logMe = function (item) {
  if (this.x === undefined)
  {
    this.x = 0;
  }
  else {
    this.x += 1;
  }

  console.log(`${this.x}: ${item}`);

}
