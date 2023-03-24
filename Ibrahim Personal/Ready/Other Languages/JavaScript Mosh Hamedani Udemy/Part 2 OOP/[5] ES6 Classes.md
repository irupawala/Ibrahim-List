## [1] ES6 Classes

* In ES6/ ES2015, there is new way of creating objects in JS that is with the use of classes.
* Classes in JS is like Syntactic sugar over prototypical inheritance. It's not like classes in Java or C++.
* Study the code below.

```javascript
class Circle {
  constructor(radius) { // This is same as constructor function in ES5 and below
    this.radius = radius;
    this.move = function() {} // This will be inheritance method
  }

  draw() { // notice that function keyword is not present
    // This will be prototypical method
    console.log('draw'); 
  }
}

const c = new Circle(1);
```

* You can write this new code in Babelis.io and observe that code getting converted to ES5 format.
* Make  a check by typing this simple code on Babelis.io

```javascript
class Circle {
  constructor() { 
  }
}
```

## [2] Hoisting

* Hoisting is a concept which allows the use of the functions before the declaration by raising all the function declarations to the top of the code.
* Study the code

```javascript
console.log (number); // Cannot be done
console.log (sayHello); // Can be done because of hoisting which means that all the function declarations are raised to the top
console.log(sayGoodbye); // Cannot be done because it is identifier like a const


// Function Declaration
function sayHello() {} // No Semicolon

// Function Expression
const sayGoodbye = function() {}; // Notice the semicolon
const number = 1;
```

* Unlike functions Class declarations and functions are not hoisted

```javascript
const c = new Circle(); // Not allowed 

// Class Declaration
class Circle { // stick to Class Declaration as it is used more

}

// Class Expression
const Square = class {

};
```

## [3] Static Methods

* In classical OOP's there are two methods. Instance methods and static methods.
* Static Methods not available on Object instance but class itself to create utility functions not specific to given object.
* These are not tied to the object hence not available on circle object.
* With static method we are not working on circle object but circle class itself. Hence to call static method we don't have to create instance of the class.

```javascript
class Circle {
  constructor(radius) {
    this.radius = radius;
    }

    // Instance/ Prototype Method 
    draw() { // Available on instance of a Class which is Object

    }

    // Static Methods not available on Object instance but class itself to create utility functions not specific to given object.
    static parse (str) { // Not tied to the object hence not available on circle object 
      console.log("parse");
    }
  }

const circle = new Circle(1);
Circle.parse(); // parse method not present in object but accessible on reference.  With this method we are not working on circle object but circle class itself. Hence to call static method we don't have to create instance of the class
console.log(circle);
```

* 

```javascript
class Circle {
  constructor(radius) {
    this.radius = radius;
    }

    // Instance/ Prototype Method 
    draw() { // Available on instance of a Class which is Object

    }

    // Static Methods not available on Object instance but class itself to create utility functions not specific to given object.
    static parse (str) { // Not tied to the object hence not available on circle object 
      const radius = JSON.parse(str).radius; // Assume that JSON.parse(str) is a valid object and radius is one of its properties
      return new Circle(radius);
    }
  }

//const circle = new Circle(1);
const circle = Circle.parse('{"radius": 1 }')
//Circle.parse(); // parse method not present in object but accessible on reference.  With this method we are not working on circle object but circle class itself. Hence to call static method we don't have to create instance of the class
console.log(circle);
```

## [4] This Keyword

* Study the code below

```javascript
const Circle = function() {
  this.draw = function() {
    console.log(this);
  }
}

const c = new Circle(); // In this case, this in the function will point to c object
// The statement above will create a new empty object and will point this in the function to this new empty object.
// If we forgot the "new" operator then again same scenario will occur and this will point to global object.
// Method Call
c.draw();


const draw = c.draw; // When we call the method as a function by default this will point to the global object which is windows in the browser and global in the node
// Function Call
draw(); 
```

* Strict Mode
* When enabled JS engine will do more checking. If there are errors which are silently going to fail it will turn them into exceptions.
* Also it will change the behavior of ***this*** in the function.

```javascript
'use strict';

const Circle = function() {
  this.draw = function() {
    console.log(this);
  }
}

const c = new Circle(); // In this case, this in the function will point to c object
// The statement above will create a new empty object and will point this in the function to this new empty object.
// If we forgot the "new" operator then again same scenario will occur and this will point to global object.
// Method Call
c.draw();


const draw = c.draw; // When we call the method as a function by default this will point to the global object which is windows in the browser and global in the node
// Function Call
draw(); 
```

* If we use strict here then instead of global function we will get undefined, the reason being JS engine wants us to prevent making any unintentional changes to the windows object.
* Now consider the case when this is used within the class

```javascript
class Circle {
  draw() {
    console.log(this);
  }
 }

//const draw = Circle.draw;
//draw();

const c = new Circle();
const draw = c.draw;// getting reference of draw method
draw();
```

* In this case also the this will be undefined because the **body of the class by default gets executed in the strict mode.**

## [5] Private Members using Symbols

* In the example below let's make the radius as private using ES6 Symbols
* Symbol is nothing but unique Identifier hence every time we call it we get a new unique identifier. Check it by writing Symbol() === Symbol in the console.
* Also it's not constructor function hence we cannot use  new Symbol()
* We can use this unique value as a property name for an object

```javascript
const _radius = Symbol(); // _ is used by convention to indicate private property

class Circle {
  constructor (radius) {
   // this.radius = radius; // public by default
   // this['radius'] = radius;
   // We can also use the Symbol() name in the line above intead of a string 
      this[_radius] = radius;
  
  }
}

const c = new Circle(1);
```

* The output is as follows

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\38.PNG)

* Note here that internally the Symbol() will have unique value hence internally the name of the properties will have unique values each time if we create multiple properties using the symbols.
* Notice that now if we try to access the radius using `c.radius` or `c._radius` then we won't be able to access it because radius is private.
* To view this private property we can use `getOwnPropertySymbols`

```javascript
const _radius = Symbol(); // _ is used by convention to indicate private property

class Circle {
  constructor (radius) {
   // this.radius = radius; // public by default
   // this['radius'] = radius;
   // We can also use the Symbol() name in the line above intead of a string 
      this[_radius] = radius;
  
  }
}

const c = new Circle(1);
const key = Object.getOwnPropertySymbols(c)[0]; // [0] because getOwnPropertySymbols will return an array hence logging the first element
console.log(c[key]);
```

* Now we will get the value of the radius on the console.
* Now adding the private method using symbols

```javascript
const _radius = Symbol(); // _ is used by convention to indicate private property
const _draw = Symbol(); // to make draw method private

class Circle {
  constructor (radius) {
   // this.radius = radius; // public by default
   // this['radius'] = radius;
   // We can also use the Symbol() name in the line above intead of a string 
      this[_radius] = radius;
  
  }

  [_draw]() { // In ES6 we have this new feature which is called computed properties name. In [] brackets we add expressions and the name of the property/method will be computed based on the results evaluated from the expression
    // hence in this case as we have () after [_draw] we will get a unique identifier as the name of this method 

  }
}

const c = new Circle(1);
const key = Object.getOwnPropertySymbols(c)[0]; // [0] because getOwnPropertySymbols will return an array hence logging the first element
console.log(c[key]);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\39.PNG)



* Notice that Symbol() in the protoype represents the private draw method while Symbol() in the Circle object represents the private radius property

## [6] Private Members using WeakMaps

* Now we will look at how the radius which is public property is converted to private property using Weak Maps for the example below. Also we will see the declaration of method using the WeakMaps.

```javascript
class Circle {
  constructor(radius) {
    this.radius = radius;
  }

}

const c = new Circle(1);
```

* WeakMaps is nothing but dictionary in which the keys are objects while values can be anything.
* We call it weak because Keys are weak meaning if there are no references for the keys then they will be garbage collectors.

```javascript
const _radius = new WeakMap();

class Circle {
  constructor (radius) {
    //this.radius = radius;
    _radius.set(this, radius); // first argument (key) has to be object, here it is instance of Circle object and second will be radius element.
  }
}

const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\40.PNG)

* Observe that there is no radius anywhere in the object.

```javascript
const _radius = new WeakMap();

class Circle {
  constructor (radius) {
    //this.radius = radius;
    _radius.set(this, radius); // first argument (key) has to be object, here it is instance of Circle object and second will be radius element.
  }

   // Let's say we want to access the radius inside the class
   draw() {
   console.log(_radius.get(this)); // key here is an instance of circle object
  }

}

const c = new Circle(1);
```

* c.draw() here will return the value of radius.
* Now lets define a private method _move.

```javascript
const _radius = new WeakMap();
const _move = new WeakMap();

class Circle {
  constructor (radius) {
    //this.radius = radius;
    _radius.set(this, radius); 
  
    _move.set(this, function() {
      console.log("move", this);
    });
  
  
  }

   draw() {
   console.log(_radius.get(this)); 
   _move.get(this)(); // Notice that () is needed because get function returns a function
  }

}

const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\41.PNG)

* Notice that for this undefined is obtained that is because as discussed before the body of the class is executed in strict mode and this by default will set to undefined instead of global object.
* Now how can we access the instance of the circle object in the move method ??
* To solve this problem we have to use the arrow operator instead of function because when we use arrow method then this refers to the instance of the containing object.

```javascript
const _radius = new WeakMap();
const _move = new WeakMap();

class Circle {
  constructor (radius) {
    //this.radius = radius;
    _radius.set(this, radius); 
  
    _move.set(this, () => { // () is used when arrow operator is used for function
      console.log("move", this);
    });
  
  
  }

   draw() {
   console.log(_radius.get(this)); 
   _move.get(this)(); // Notice that () is needed because get function returns a function
  }

}

const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\42.PNG)

* Notice now circle instance is obtained hence we can access all the public and private properties of the circle object in the move method.
* Now one another question is why we are using separate WeakMap for each property and method and why not just one WeakMap for all the private members.
* We can do that but it increases the complexity hence not recommended.

```javascript
const _radius = new WeakMap();
const _move = new WeakMap();
const privateProps = new WeakMap();

class Circle {
  constructor (radius) {

    privateProps.set(this, {
      radius: radius,
      move: () => {

      }
    });

    // To access each members we can use

    privateProps.get(this).radius; // privateProps.get(this) returns an object


    _radius.set(this, radius); 
  
    _move.set(this, () => { // () is used when arrow operator is used for function
      console.log("move", this);
    });
  
  
  }

   draw() {
   console.log(_radius.get(this)); 
   _move.get(this)(); // Notice that () is needed because get function returns a function
  }

}

const c = new Circle(1);
```

## [7] Getters and Setters

* Notice the different and easy way of defining getters and setters in ES6 exists.
* Note that for ES5 we used `Object.defineProperty` in the constructor function itself.

```javascript
const _radius = new WeakMap();

class Circle {
  constructor (radius) {
    _radius.set(this, radius);

    Object.defineProperty(this, 'radius', {
      get: function() {
        return radius;
      },
      set: function(value) {
        radius = value;
      }
    })
  }

}

const c = new Circle(1);
```

* But in ES6 simple and more elegant ways exists.

```javascript
const _radius = new WeakMap();

class Circle {
  constructor (radius) {
    _radius.set(this, radius);
  }

  // This is first method but we have to call here function c.getRadius()
  getRadius () {
    return _radius.get(this);
  }

  // This is the second and more efficient method and here we can call radius as a property c.radius
  get radius () {
    return _radius.get(this);
  }

  set radius (value) {
    if (value <= 0) throw new Error('Invalid Error');
    _radius.set(this, value);
  }

}

const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\43.PNG)

## [8] Inheritance

* We can implement inheritance very simply using ES6 here we don't need any prototypical inheritance or resetting of the constructor.

```javascript
class Shape  {
  constructor (color) {
    this.color = color;
  }
  move() {
    console.log('move');
  }
}

class Circle extends Shape{
  constructor (color, radius) {
    this.radius = radius;
  }
  draw() {
    console.log('draw');
  }
}

const c = new Circle('red', 5);
```

* But Notice that there is an issue with this code.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\44.PNG)

* This is because whenever we add the constructor in the circle (child) class we have to call super constructor (parent) in the derived class first to initialize the base object.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\45.PNG)

## [9] Method Overriding

```javascript
class Shape  {
  move() {
    console.log('move');
  }
}

class Circle extends Shape{
  move() {
    super.move();
    console.log('circle move');
  }
}

const c = new Circle();
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\46.PNG)