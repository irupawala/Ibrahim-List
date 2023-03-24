## [1] Inheritance

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\2.PNG)

* The figure above shows a IsA child class from a parent class. Note that this is Classical Inheritance. But in JS we have prototypical Inheritance.
* **Note that in JS we don't have classes we only have Objects.** 



## [2] Prototypes and Prototypical Inheritance

* Prototype is nothing but parent object. In JS we can define an object with all the common behavior and methods and then somehow link this object with all the methods to other objects. Now this object is called as prototype object.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\4.PNG)

* To illustrate this if we look at the description of an object in JS we will find constructor and couple of other functions. Hence every object in JS is linked to another object which is it's prototype for our discussion let's call this prototype as objectBase.
* Every object in JS directly or indirectly inherits from the objectBase.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\3.PNG)

* ObjectBase is a root of all objects in JS and it doesn't have a prototype or parent.
* This can be observed by seeing the description of above. It doesn't have a prototype or a parent.
* Notice that single objectBase exists for all the objects in memory

![image-20200208105249355](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\5.PNG)

* This can be proved by checking getPrototypeOf() function in JS

![image-20200208105613554](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\6.PNG)

**Then What is Prototypical Inheritance**

Notice that in the object x = {} example shown above. tostring() method is not defined in the x = {} object. Hence in JS if it doesn't find the method in the description of the object, it will find the method in the prototype and will go up-chain until it finds the method in any prototype all the way to root object. This is prototypical Inheritance.

![image-20200208110401500](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\7.PNG)



![image-20200208110448379](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\8.PNG)

**Every Object in JS has a prototype except the root object** 

## [3] Multi-level Inheritance

![image-20200208112510676](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\9.PNG)

Check this by typing myArray = [] in the console and check the prototype

![image-20200208112723565](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\10.PNG)

![image-20200208112839309](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\11.PNG)

This is to say all the childs will have the same parent

![image-20200208112917107](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\12.PNG)

## [4] Prototype Descriptors

Notice that none of the properties or methods defined in the objectBase are visible to us

![image-20200208114224232](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\13.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\14.PNG)

The reason being properties have attributes attached to it. Sometimes these attributes prevent the properties from being enumerated.

Let's look at the attributes of the toString method.

![image-20200208114700741](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\15.PNG)

![image-20200208114854165](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\16.PNG)

Configurable means this object can be deleted.

For our own object we can define our own attributes.

```javascript
let person = {name: 'Mosh'};

Object.defineProperty(person, 'name', {
    writable: false,
    enumerable: false,
    configurable: false

})

person.name = 'John'; // won't get changed

delete person.name // won't get deleted

console.log(person);
console.log(Object.keys(person)); // won't be displayed because enumerable is false
```

## [5] Constructor Prototypes

```javascript
Object.getPrototypeOf(myObj);

//myObj.__proto__ (parent of myObj).
// Constructor.prototype() // This will be exactly same as the (parent of myObj) above
```

* This is the way we check the prototype of the objects in JS

* However, notice that in JS constructor also has a prototype property
* Now, we know that in JS functions are objects and objects have methods and properties.
* We also have a `prototype` property. 
* In the example below Circle.prototype is the object that will be used as a parent for the object created by the circle constructor.

```javascript
function Circle(radius) {
    this.radius = radius;
}

Circle.prototype
```



![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\17.PNG)

* Notice that when object is created using literal syntax under the hood it is created using the constructor `new Object` . 
* Hence in a nutshell note that the root object for both the `obj` and all the objects created by the constructor `Object` is the same.
* Consider example of Array

![image-20200208135128214](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\18.PNG)

* Consider the example of Circle Object defined below

![image-20200208135306349](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\19.PNG)



## [6] Prototype Vs Instance Members

* Notice that lots of memory is wasted  when we create hundreds of objects all having the same function.

![image-20200208153359032](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\20.PNG)

* Hence, we can use prototypical inheritance in which JS first looks for the function definition in the object itself and if it is not found it searches it in the prototype of the object.
* In the example above we can remove the draw method out of the circle object and put it in it's prototype.
* We will have single instance of the prototype in the memory which we call circleBase hence we will have single instance of the function.
* Notice as shown below both of these properties are representing same object in the memory which is the circleBase.

```javascript
Circle.prototype === c1.__proto__
```



![image-20200208154737896](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\19.PNG)



Also, note that using the prototype we can overwrite the implementation of the method in prototypes of the circle object.

![image-20200208155502814](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\21.PNG)

* Notice in the case above JS will first look search for the toString method in the circle object and if it doesn't find it, it will go to the prototype.
* The interesting thing is even though we have the implementation of toString in the objectBase, the implementation defined by us will be used because it is more accessible.



* Notice that in both these types of members (instance and prototype) you can reference other members.

* Adding instance member in prototype member.

![image-20200208162134918](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\22.PNG)

* Similarly in an instance member we can refer prototype member

![image-20200208162325294](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\23.PNG)



## [7] Iterating Instance and Prototype Members

* Notice that it doesn't matter if the prototype members is defined before or after the object declaration. even if you define the prototype members after the object declaration the object will still have the prototypes.

```javascript
function Circle (radius) {
    // Instance Members
    this.radius = radius;
    this.move = function {
        console.log('move');
    }
}

const c1 = new Circle(1);

// Prototype members
Circle.prototype.draw = function() {
    console.log('draw');
}

c1.draw();
```

![image-20200208183826924](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\24.PNG)

* Notice in the program below, the `Object.keys` returns only instance members while for-in returns all the instance + prototype members.
* In JS, many documents refers the instance members as own members. hence, we also have a function called hasOwnProperty()

```javascript
function Circle (radius) {
    // Instance Members
    this.radius = radius;
    this.move = function() {
        console.log('move');
    }
}

const c1 = new Circle(1);

// Prototype members
Circle.prototype.draw = function() {
    console.log('draw');
}

// Returns Instance members
console.log(Object.keys(c1));

// Returns all members (instance + prototype)
for (let key in c1) console.log(key);

console.log(c1.hasOwnProperty('radius'));
```



## [8] Avoid Extending the built-in Objects

* Never extend the built-in object in JS though it is easy to extend it in JS in the prototypes.
* This is not advisable because if we use a third party library someone might have over-written the function defined by you in the prototype.

![image-20200208193239580](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\25.PNG)



## [10] Exercise

* Convert the stopwatch code written before to move all the functions to from instance members to prototype members.

```javascript

function Stopwatch() { 
    let startTime, endTime, running, duration = 0;
  
  
    Object.defineProperty(this, 'duration', {
      get: function() { return duration; },
    //  set: function(duration) {this.duration = duration;}
      set: function(value) {duration = value;}
    });

    Object.defineProperty(this, 'startTime', {
        get: function() { return startTime; }
      });

    Object.defineProperty(this, 'endTime', {
        get: function() { return endTime; }
      });

    Object.defineProperty(this, 'running', {
        get: function() { return running; }
      });


  }


  Stopwatch.prototype.start = function() {

    if (this.running) 
    throw new Error('Stopwatch has already started.');
    
    this.running = true; 
    
    this.startTime = new Date();
  }

  Stopwatch.prototype.stop = function() {

    if (!this.running) 
    throw new Error('Stopwatch is not started.');

    this.running = false; 
    
    this.endTime = new Date();

    const seconds = (this.endTime.getTime() - this.startTime.getTime()) / 1000;
    this.duration += seconds; 
  }

  Stopwatch.prototype.reset = function() {

    this.startTime = null;
    this.endTime = null;
    this.running = false; 
    this.duration = 0; 
  }


```

* Notice that in the code above, duration is public read only property hence we cannot modify duration from outside. We can solve the problem by adding a setter for `duration` .
* But notice that setting duration from outside might create a huge mess, as user can now change the duration by it's own terms. remember that objects should be reliable that is the reason we use abstraction so that we can hide unnecessary complexity and expose to the clients of the objects only few members so that the clients can work without messing up the state.

```javascript
const sw = new Stopwatch();
sw.duration = 10;
```

