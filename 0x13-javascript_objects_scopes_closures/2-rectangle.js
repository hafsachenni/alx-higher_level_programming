#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else if (w && h < 0) {
      Object.create(null);
    } else if (w && h === 0) {
      Object.create(null);
    }
  }
};
