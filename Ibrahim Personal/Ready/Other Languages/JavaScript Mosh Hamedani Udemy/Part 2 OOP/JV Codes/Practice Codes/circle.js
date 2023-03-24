const _radius = new WeakMap();

class Circle {
  constructor(radius) {
    _radius.set(this, radius);
  }


  draw() {
    console.log('Circle with radius ' + _radius.get(this));
  }
}

// This is how you export multiple object
//module.exports.Circle = Circle;// modules here refers to the current module, exports is a property. module.exports refers to an object and we can add one or more properties to this object
//module.exports.Square = Square; // here .exports.Square is a name of the properties and we set it to the Square class as shown

// This is how you export single object
// As discussed before module.exports is an object
// If we have only single object then instead of adding a circle property to the modules.export object we can just reset this object to circle
// Hence when we import the module we get circle class

module.exports = Circle; // module.exports refers to the object that is exported from this module. 