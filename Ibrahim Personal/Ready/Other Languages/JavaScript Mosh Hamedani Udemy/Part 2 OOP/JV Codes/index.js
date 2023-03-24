function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};

  // this.getDefaultLocation = function() {
  //   return defaultLocation;
  // }
  
  // this.draw =  function() {
  //   console.log('draw');
  // };


  // Notice that the Object has method called defineProperty and defineProperties (if you want to define multiple properties in one go)
  Object.defineProperty(this, 'defaultLocation', {
    get: function() {
      return defaultLocation;
    },
    set: function(value) {
      if (!value.x || !value.y) // checking if the value passed is not a falsy
        throw new Error ('Invalid Location');

      defaultLocation = value;
    }

  });
}

const circle = new Circle(10);
circle.defaultLocation = {x:1, y:1};