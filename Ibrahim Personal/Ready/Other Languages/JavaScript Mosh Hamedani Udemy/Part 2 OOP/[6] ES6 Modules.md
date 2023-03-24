## [1] Modules

* Modules is nothing but having different functions/features of a program in a different code.

* Advantages of Modularity

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\47.PNG)

* To achieve the abstraction we can take the radius WeakMap and Circle class out of the file and put it in a separate file called Module and then only expose the Circle class outside. 
* Hence Now we can import the circle class, create the circle object but we will not have access to this radius object which is our weakmap. This is abstraction in action.
* In JS, there are various syntaxes called module formats. Some of the popular ones are:
* AMD - Asynchronous Module Definition
* UMD - Universal Module Definition

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\48.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\49.PNG)

## [2] CommonJS Modules

* Notice that everything defined in module is considered private unless explicitly exported.
* CommonJS format requires `module.exports` in the module and `require()` function in the main code.
* Circle.js Module

```javascript
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
```

* index.js

```javascript
const Circle = require('./circle') // ./ refers current directory. Also note that extension is not required like .js 

const c = new Circle(10);
c.draw();
```



* Note that in the circle module we are only exporting the circle class so this radius weakMap is not accessible in our other modules. This is part of implementation detail of circle module.
* What we are exporting which is our circle class, is what we call the public interface.
* So this is abstraction in practice where we are hiding the implementation details or complexity inside the module.
* If we change _radius with some other value like Symbol() then the entire code will not break.

