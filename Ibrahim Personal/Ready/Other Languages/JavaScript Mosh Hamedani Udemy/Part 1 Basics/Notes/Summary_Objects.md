## [1] What is an Object ?

* Objects are collections of key value pairs.
* Objects are reference types meaning we can have two objects with the exact same properties but these objects are at different memory locations. hence when we use the equality operator === we're essentially checking to see if these objects have the same reference. **Hence to properly check their properties, we need to make sure that all their properties are equal.**
* **Function of an object is to group related variables and related functions.**

```javascript
const circle = {
    radius: 1, 
    location: {
        x: 1,
        y: 1
    },
    isVisible: true,
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};

circle.draw();
```

## [2] Ways to create re-usable objects

### 1. Factory Functions

* Factory function is one of the way to create reusable objects

```javascript
// Factory Function

function createCircle(radius) {

    return { 
        radius, // In modern JS if the key-value pair is the same we can remove the value and simply add the key
        //radius: radius,  // This statement is exactly equivalent to one above it.
        draw () { // This is similar to how we define functions outside the object but without keyword "function"
            console.log('draw');
        }
    };
}

const circle1 = createCircle(1);
console.log(circle1);

const circle2 = createCircle(1);
console.log(circle2);
```

### 2. Constructor Function

* This is one another way to create or construct an object.
* While creating constructor we should use Pascal Notation by JS convention.

```javascript
// Constructor Function

function Circle(radius) {
    // this is a reference to the object that is executing this piece of code
    // imagine "this" references an empty object

    this.radius = radius;
    this.draw = function (){ // adding a method draw
        console.log('draw');
    }
}

const circle = new Circle(1);
```

When you write new 3 things happens: 

1. This new operator creates an empty JS object like this "const x = {};"

2. Now "this" keyword in function will point to new empty object {}

3. Finally function "Circle" will return that x = {} object with all the properties. Notice that this empty object didn't had any properties these were added by the constructor function.

   

**Difference between Factory Function and Constructor Function:**

1. Different ways of creating an object and returning an object.

* With Factory functions we create objects like this: 

```javascript
const myCircle = createCircle(1);
```

- In this function we simply return a new object

**In constructor function we use the new operator and instead of returning an object we use this keyword**

```javascript
// Constructor Function

function Circle(radius) {
    this.radius = radius;
    this.draw = function (){ // adding a method draw
        console.log('draw');
    }
}

const circle = new Circle(1);
```

2. Naming conventions
   1. Factory Function - Camel Convention
   2. Constructor Function - Pascal Convention

## [3] Dynamic Nature of Objects

* You can add and delete properties of the object because it is dynamic in nature

```javascript
const circle = {
    radius = 1
};

//circle = {}; // Notice that this cannot be done as object is declared as constant

circle.color = 'red';
circle.draw = function() {}

delete circle.color;
delete circle.draw;
```

* Notice that here the object is declared as `const` this does not mean that we are not able to add or delete the properties. This means that the **object circle cannot be over-ridden**.

## [4] Constructor Property

<u>**Who Creates Objects in JavaScript ?**</u>

Answer - Constructor.

* Every Object in JS has a property called constructor which was used to construct or create the object. To check the constructor of the function we can type this in console.

```javascript
objectName.constructor
```

* The output obtained is ***f Object { [native.code] }***
* This is a built-in constructor function in JS. When we create an object using object literal syntax, internally JS engine uses this constructor function.



<u>**What happens when we define new object ?**</u>

* When we define a new object `let x = {};`
* JS engine will translate that to something like this `let x = new Object();`



<u>**What is the constructor for an object created using factory function ?**</u>

```javascript
// Factory Function
function createCircle(radius) {

    return { 
        radius,
        draw () { 
            console.log('draw');
        }
    };
}

const circle1 = createCircle(1);
console.log(circle1);
```

If we try to check constructor of an circle1 object :

```javascript
circle1.constructor
```

then it will be  ***f Object { [native.code] }***. **This is a built-in constructor function in JavaScript.**

This is because we created this function first using `const circle1` and then we returned it from our factory function and because we used object literal syntax internally, it was created with this object constructor function.



<u>**Who creates other objects like strings, booleans, numbers, etc ?**</u>

Answer- In JS we have constructor for every object, example 

```javascript
new String(); // but we use string literals to create strings '', "", ``
// using the literals is cleaner and simpler than using the constructor
new Boolean(); // but we have boolean literals true, false
new Number(); // 1, 2, 3,..
```

**Every Object has a constructor property and that references a function that was used to create that object.**



## [5] Functions are Objects

**<u>Who Created Functions ?</u>**

```javascript
// Constructor Function

function Circle(radius) {
    this.radius = radius;
    this.draw = function (){ // adding a method draw
        console.log('draw');
    }
}

const another = new Circle(1);
```

* Functions are objects in Javascript to check this type `Circle. + tab` in Visual studio. The list of all the methods and property will be observed.
* As we know functions are objects hence who created this object ? We can check this using `Circle.constructor`
* Answer -  ***f Function() { [native.code] }***
* Hence when we declare a function using `function Circle(radius)` syntax, internally JS engine will use this function constructor to create this object.



**<u>Creating an object directly using constructor function</u>**

* To understand constructor function more deeply we can create an object directly using `Function constructor`

* Just like we have `new String(), new Boolean(), new Number()` constructor functions we have `new Function()` constructor for function.

  

**Function defined using the string literals**

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function (){ // adding a method draw
        console.log('draw');
    }
}

const another = new Circle(1);
```



**Function defined using the constructor `new Function()`**

```javascript
const Circle1 = new Function('radius',// one argument is radius, other arguments to this function is all other lines of codes in Circle
    ` this.radius = radius;              
      this. draw = function (){ 
        console.log('draw');
		}
`); // When we declare a function, internally it is represented like this.


// Now we can direcly call the Circle1 just like Circle Function
const circle = new Circle1(2);
```

* if we will check `Circle1.constructor` or `circle.constructor` in the console then we will be able to observe  ***f Function() { [native.code] }*** as expected.



**<u>Methods of the functions</u>**

* Now let us look into some methods of the functions. There are two ways of calling a function.
  1. Call Method
  2. Apply Method



### 1. Call Method

* The `call()` method is a predefined JavaScript method.

* It can be used to invoke (call) a method with an owner object as an argument (parameter).

* With `call()`, an object can use a method belonging to another object.

Example:

```javascript
var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"John",
  lastName: "Doe"
}
person.fullName.call(person1, "Oslo", "Norway");
```

* Now notice that instead of passing an object with properties if we pass empty object and assign properties in the function then the empty object will get those properties and thus a new object will be created. See example below.
* To check this type the name of the object `person1` in the console.

```javascript
var person = {
    fullName: function(firstName, lastName, city, country) {
        this.firstName = firstName;
        this.lastName = lastName;
      return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
  }
  var person1 = {};
  console.log(person.fullName.call(person1, "John", "Doe", "Oslo", "Norway"));
```

* Now what if the function is not inside any object in that case we can assume it to be inside global object
* Even then we can use the call method to create a new object.

```javascript
function FullName (firstName, lastName, city, country) {
        this.firstName = firstName;
        this.lastName = lastName;
      return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
  
  var person1 = {};
  console.log(FullName.call(person1, "John", "Doe", "Oslo", "Norway"));
```



**Circle Example:** 

* Now similarly observe how call method is used to create circle object in the previous examples when an empty object is passed to the call method.

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function (){ // adding a method draw
        console.log('draw');
    }
}

another = {}
Circle.call(another, 1); 

// this in Circle will reference to the {} object that we pass in the method
// The other argument is the radius. if we have multiple arguments it will be mentioned in sequence Circle.call({}, 1, 2, ...)
```

The same object can be created using `const another = new Circle(1);` as observed previously.

```javascript
const another = new Circle(1);
```

* Hence `Circle.call({}, 1);` is exactly similar to `const another = new Circle(1);`

* When we use the new operator, this new operator will internally create an empty object {} and pass that as the first argument to the call method.



* When we don't use the new operator `this` will point to a global object which is **window**.
* Hence this time call method will have window as an argument instead of {}.

```javascript
Circle.call(window, 1); 

const another = Circle(1);
```

### **2. Apply method**

* The `apply()` method is similar to the `call()` method.

* The difference is:

  The `call()` method takes arguments **separately**.

  The `apply()` method takes arguments as an **array**.

* The apply() method is very handy if you want to use an array instead of an argument list. This is useful when we already have an array somewhere in your application and you want to pass an array as the second argument to the apply method.

```javascript
Circle.apply(window, [1, 2, 3]); 
```

## [6] Value vs. Reference Types

**Value Types**

* Number
* String
* Boolean
* Symbol
* undefined
* null



**Reference Types**

* Object 
* Function
* Array



**Summary:**

* **Primitives are copied by their value**
* **Objects are copied by their reference**



Example 1:

**Value type**

```javascript
let x = 10;
let y = x;

x = 20;
```

In the example above the x and y are independent of each other. when you change x the value of y doesn't change hence the output will be x = 20, y = 10.

**Objects**

```javascript
let x = {value: 10};
let y = x;

x = {value: 20};
```

Notice here that object is not stored in the variable, **the object is stored somewhere in the memory and the address of that memory location is stored inside that variable. Changes made by one variable is immediately visible to another variable.**



![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 1 Basics\Images\1.PNG)



Example 2:

**Value type**

```javascript
let number = 10;

function increase(number) {
    number ++;
}

increase (number);
console.log(number);
```

* Note that in this example the local parameter number of the increase function gets out of the scope as the function is executed. Hence here we are dealing with two individual values both having the name *number*

**Objects**

```javascript
let obj = {value: 10}

function increase(obj) {
    obj.value ++;
}

increase (obj);
console.log(obj);
```

* But notice that in case of object, we will get the incremented value because here we are passing value by reference. hence the local parameter obj points to the same obj defined globally.
* Hence here we are not dealing with different objects but we have two values pointing to the same object hence any changes made will be immediately visible by both the variables.

## [7] Enumerating Properties of an Object

### 1. Objects are not iterable using for of

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};


// iterable using for-in loop:
for (key in circle) 
console.log(key, circle[key]);

// notice that this will give error as objects are not iterable
for (let key of circle)
console.log(key);
```

* Hence we have to use **Object.keys** which will return an array of all the keys hence made iterable.
* Similar to Object.keys we have **Object.entries** method which will return an array of all the key-value pairs.

### 2. Object.keys and Object.entries

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};


for (let key of Object.keys(circle))
console.log(key);

for (let entry of Object.entries(circle))
console.log(entry);
```

### 3. In Operator

* Finally sometimes we want to see if given object has given property or method. For this we can use `in operator`

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};

if ('radius' in circle) console.log('yes');
```

## [8] Cloning an Object

Using the enumerating property of the object we can clone an object.

### 1. Using for-in 

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};

const another = {};

for (let key in circle)
    another[key] = circle[key];

console.log(another);
```

However this method of copying using the for-in loop is little bit old.

### 2. Using assign method

* Object.assign(target object, source_object1, source_object2, ......);
* target object can be empty object {}
* there can be one or more source objects, hence we can use it to clone/ combine multiple objects into single object.

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};

//const another = Object.assign({}, circle);

const another = Object.assign({color: "yellow"}, circle);

console.log(another);
```

### 3. Spread operator

spread operator takes all the properties and methods of an object and puts them into another object.

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};

const another = {...circle};

console.log(another);
```

## [9] Garbage Collector

* The job of the **Garbage Collector** is to find the variables and constants that are no longer used and then de-allocate the memory that were allocated to them.

## [10] Built-in Object - Math

Refer - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

## [11] Built-in Object - String

**Primitive types does not have properties and objects only objects do**

* But we are able to observe properties and methods for string which is of primitive type
* The reason is because we have two kinds of strings in JS

```javascript
// String primitive
const message = 'This is my  first string';

// String object
const another = new String('hi');

typeof(message);
typeof(another);
```

**when we use the dot notation with a string 'primitive' JS engine internally wraps this with a 'string object'. hence we are able to work with it like a string object.**

### 1. String Methods

```javascript
message.length
message[0]
message.includes('my')
message.startswith('This')
message.endswith('e')
message.indexof('my')
message.replace('first', 'second') // returns new string not the original one
message.touppercase()
message.trim() // removes whitespace before and after the message
message.trimleft()
```

### 2. Escape Notation

![1569429739400](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 1 Basics\Images\2.png)

## [13] Template Literals

* Code looks really ugly and messy when we want to use escape notation.

```javascript
const message = 'This is my\n' + 
'\'first\' message'
```

* To avoid this situation from ES6 we have template literals

* Similar to 
  * Object literal `{}`
  * Boolean `true, false`
  * String literal `'', ""`

* **We have template literal ``**

Example:

```javascript
const another = 
`This is my
'first' message`;
```



* This is particularly useful while writing an email.

* Another benefit is that here we can use place holders instead of using the concatenate operator + with escape notation.

```javascript
const name = 'John';

const another =      
`Hi ${name}, ${2 + 3},

Thank you for joining my mailing list.

Regards,
Ibrahim`
```

* Note here that in place of placeholder we can add any expressions that produces a value in between the curly braces. We can also add function which returns a value.

## [14] Date

* All these three constructors below are used for creating date object.
* There are many other formats apart from these three which are supported, these formats can be found in documentation.

```javascript
const now = new Date();
const date1 = new Date('May 11 2018 9:00') 
const date2 = new Date(2018, 4, 11, 9, 0)
```

* All these have get and set method

```javascript
console.log(now.getDate());
now.setFullYear(2017);
```

* All these date objects have few methods for converting them to a string.

```javascript
console.log(now.toDateString());
console.log(now.toTimeString());
console.log(now.toISOString());
```

