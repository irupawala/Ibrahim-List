## [2] Object Literals

```javascript
const circle = { // Object literals
  radius: 1,
  location : { x:1, y:2}, // properties
  draw: function() { // methods
    console.log('draw');
  }
}; 

circle.draw();

```

## [3] Factories 

* Objects can be defined using Object literals but they can also be defined using constructors and factory functions.
* Using object literals we have to duplicate the entire code to define another circle object.
* This can be a problem if we have one or more methods in our object because we have to duplicate the method each time.

```javascript
function createCircle (radius) { // Camel Convention

  return {
    radius,
    location : { x:1, y:2},
    draw() {
      console.log('draw')
    }
  }
};

const circle1 = createCircle(1);

console.log(circle1);
```

## [4] Constructors 

```javascript
function Circle (radius) { // Pascal Convention
   // console.log('this', this);
    this.radius = radius;
    this.location = { x:1, y:2};
    this.draw =  function() {
      console.log('draw')
  }

};

const circle1 = new Circle(1);

console.log(circle1);
```

* Both Factories and Constructors are same. Programmers from Java and C# prefer constructors as it looks like creating an instance but **remember that we don't have classes in JavaScript.**



## [5] Constructor Property

* **Every object in JavaScript has a property called constructor and that refers to the function which was used to create that object.**
* This can be checked by typing `objectname.constructor`
* Note that the Circle constructor in the example above is function which is a Built-in constructor function in JavaScript.
* When we create an object using object literal syntax internally JS engine uses an internal constructor function which is called factory function.

```javascript
let x = {};

// let x = new object(); // internally converted to this by JS
```

* Similarly we have constructor functions for

```java
* new String(); // literals - '', "", ``
* new Boolean(); // literals - true, false
* new Number(); // literals - 1,2,3
```

## [6] Functions are Objects

* This can be checked using the . operator and observing all the methods and properties.

```javascript
Circle.name
Circle.length
Circle.constructor
```

* Notice the constructor of the Circle function is the constructor function `Function()`.
* Hence when we create a function like this

```javascript
function Circle (radius) { 
    this.radius = radius;
    this.draw =  function() {
      console.log('draw')
  }

};
```

* Internally it is converted to this

```javascript
const Circle1 = new Function('radius', ` // Notice the Capital F. Also arguments are // passed as a string
this.radius = radius;
this.draw =  function() {
  console.log('draw')
}
`);
```

* Now we can create the circle object in the similar way

```javascript
const another  = new Circle(1);

const circle = new Circle1(1);
```

### **Methods of the function**

1. Call Method

* first argument is ***this*** argument while other arguments can be passed after that.

```javascript
function Circle (radius) { 
    this.radius = radius;
    this.draw =  function() {
      console.log('draw')
  }

};

Circle.call ({}, 1) // passing empty object for this and radius as 1.
```

* This expression is exactly similar to this expression below. Whenever we use the `new`  operator. This `new` operator will internally create an empty object and pass it as a first argument to the call method

```javascript
const another = new Circle(1);
```

* We know that when we don't write new operator then the `this` will point to the global object.

```javascript
const another = Circle(1);
```

* This can be written using the call method like this

```javascript
Circle.call (window, 1)
```



2. Apply Method

* Exactly similar to Call method but arguments are passed as an array

```javascript
Circle.apply ({}, [1, 2, 3])
```

## [7] Value vs Reference Types

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\1.PNG)



**Summary:**

* **Primitives are copied by their value**
* **Objects are copied by their reference**



Example of Primitive:

```javascript
let number = 10;

function increase (number) {
  number ++;
}

increase (number);
console.log(number);
```

Example of Reference:

```javascript
let number = {value: 10};

function increase (number) {
  number.value ++;
}

increase (number);
console.log(number);
```

## [8] Adding or Removing Properties

### **Adding Properties:**

* Objects in JavaScript are dynamic meaning after the creation of objects you can add or remove properties.
* This is very useful in real world as we can additional stuff to the existing object on the fly. **Here we don't have classes hence we don't need to define the properties ahead of time. We can add them whenever we need them, this makes JavaScript extremely powerful and easy to work with.**
* **In Java or C# every time we have a new property we have to go back and change our classes**

```javascript
function Circle (radius) { 
  this.radius = radius;
  this.draw =  function() {
    console.log('draw');
  }
}

const circle = new Circle(1);

circle.location = {x:1}; // dot notation
circle['location'] = {x:1}; // bracket notation
```

Bracket notation is used to access the propertyName dynamically 

```javascript
const propertyName = 'location';
circle[propertyName] = {x: 1};
```

Another use case is when we are dealing with propertyNames which are not valid identifiers

```javascript
const propertyName = 'location-surat';
//circle.location-surat; // this cannot be used like this.
circle[propertyName] = {x: 1};
```

### **Removing Properties:**

Similar to the adding properties we can use dot notation and bracket notation to do the same.

```javascript
delete circle.location;
delete circle['location'];
```

## [9] Enumerating Properties

### 1. Using For-in :

```javascript
function Circle (radius) { 
  this.radius = radius;
  this.draw =  function() {
    console.log('draw');
  }
}

const circle = new Circle(10);

for (let key in circle) {
  console.log(key, circle[key]);
}
```

Displaying only the properties

```javascript
function Circle (radius) { 
  this.radius = radius;
  this.draw =  function() {
    console.log('draw');
  }
}

const circle = new Circle(10);

for (let key in circle) {
  if (typeof circle[key] !== 'function')
    console.log(key, circle[key]);
}
```

### 2. To view only keys

```javascript
const keys = Object.keys(circle);
console.log(keys);
```

### 3. Using in keyword:

```javascript
if ('radius' in circle) 
 console.log('Circle has a radius');
```

## [10] Abstraction

Abstraction is:

* Hide the details
* Show the specific.

```javascript
function Circle (radius) { 
  this.radius = radius;
  this.defaultLocation = {x: 0, y: 0};
  this.computeOptimumLocation = function () {
    //
  }
  
  this.draw =  function() {
    this.computeOptimumLocation();
    console.log('draw');
  };
}

const circle = new Circle(10);
circle.defaultLocation = false;
```

* Notice in this example we only want draw function to use computeOptimumLocation and defaultLocation but not user.
* In other words it will be a disaster if user changes the defaultLocation = false as shown above

## [11] Private Properties and Methods



```javascript
function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};
  let computeOptimumLocation = function () {
    //
  }
  
  this.draw =  function() {
    computeOptimumLocation(0.1); // accessing variable from parent function
      
      // this.radius; // accessing member of the circle object
    
    console.log('draw');
  };
}

const circle = new Circle(10);
```

* Notice that if we use let keyword instead of this then those variables are only available within the function and will not be the part of the object.
* Now notice that we are able to use the **variables defined in the parent function Circle in the child function draw because of a concept available in JavaScript called closure.**

Scope: 

* Scope defines the region in which the variables will be available.
* Example x and y will be available only within the function draw

```javascript
  this.draw =  function() {
    let x, y;
      
    computeOptimumLocation(0.1);
    console.log('draw');
  };
}
```

* When we finish the execution of this function x and y will go out of scope.
* In contrast to scope we have closure.

Closure:

* Closure determines what variables will be accessible to the inner function.
* In the example above the draw function will have access to all the variables defined within itself as well as all the variables defined in the parent function.



Notice :

* **Scope is temporary and it dies after the function draw is executed.**
* **Closure stays in the memory even after the function draw has completed execution.**



* Now if we access the members of the circle object we will only see draw() and radius

```javascript
const circle = new Circle(10);
circle.draw();
circle.radius;
```

## [12] Getters and Setters

* Notice that technically the two variables that we have converted to private cannot be called as private members because technically they are not inside circle object.

* They are local variables that we have defined inside circle function but from OOP point of view we can refer them as private member of a circle object.

### Getter 

* Now what if we want to read these variables - one option is to define a function and return the variable.

```javascript
function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};

  this.getDefaultLocation = function() {
    return defaultLocation;
  }
  
  // this.draw =  function() {
  //   console.log('draw');
  // };
}

const circle = new Circle(10);
console.log(circle.getDefaultLocation()); // called like a method
```

* Now what if we don't want to call it like a method, that is without brackets () then we have to define a getter.
* Getter and setters can be defined in javascript using the method defineProperty or defineProperties (if you want to define multiple properties in one go) of an object.
* Getters are the function which are used to read values and not modify them.

```javascript
function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};

//  this.getDefaultLocation = function() {
//    return defaultLocation;
//  }
  
  // this.draw =  function() {
  //   console.log('draw');
  // };


// Syntax is 
// (first argument is the object to which we want to add the property, 
// second argument is the name of the property and 
// third argument is the object and in this object we have a key-value pair, the key is get which is a special keyword in JS and value is the function)
  Object.defineProperty(this, 'defaultLocation', {
    get: function() {
      return defaultLocation;
    }
  });
}

const circle = new Circle(10);
console.log(circle.defaultLocation);
```

```javascript
function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};

  // this.getDefaultLocation = function() {
  //   return defaultLocation;
  // }
  
  // this.draw =  function() {
  //   console.log('draw');
  // };


// Syntax is 
// (first argument is the object to which we want to add the property, 
// second argument is the name of the property and 
// third argument is the object and in this object we have a key-value pair, the key is get which is a special keyword in JS and value is the function)
    
  Object.defineProperty(this, 'defaultLocation', {
    get: function() {
      return defaultLocation;
    }
  });
}

const circle = new Circle(10);
console.log(circle);
```

* **Notice that this new getter function won't be visible as a property on the object. That is we won't have circle.defaultLocation AS A PROPERTY**

* type the object name in the console to get the details of the getter property. Also notice that this is a computed property meaning it will be displayed as (...) in the output. When we click it then it will be computed and details will be shown.

### Setter

* Notice that getter is a function which has read only property. Now what if we want to set the value of the property from outside then we define a setter.
* Setter can also be defined using similar syntax

```javascript
function Circle (radius) { 
  this.radius = radius;

  let defaultLocation = {x: 0, y: 0};

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
```

## [13] Exercise Solutions

```javascript

function Stopwatch() { 
  let startTime, endTime, running, duration = 0;

  this.start = function() {
    if (running) 
      throw new Error('Stopwatch has already started.');
    
    running = true; 

    startTime = new Date();
  };

  this.stop = function() {
    if (!running) 
      throw new Error('Stopwatch is not started.');

    running = false; 
      
    endTime = new Date();

    const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
    duration += seconds; 
  };

  this.reset = function() { 
    startTime = null;
    endTime = null;
    running = false; 
    duration = 0; 
  };

  Object.defineProperty(this, 'duration', {
    get: function() { return duration; }
  });
}
```

