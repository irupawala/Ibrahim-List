## [1] Basics

* Objects are collections of key value pairs.
* Objects are reference types meaning we can have two objects with the exact same properties but these objects are at different memory locations. hence when we use the equality operator === we're essentially checking to see if these objects have the same reference. **Hence to properly check their properties, we need to make sure that all their properties are equal.**
* Hence if there are properties of an object that are highly relatable it makes sense to bundle them into an object.
* **Function of an object is to group related variables and related functions.**

```javascript
const circle = {
    radius: 1, // The value here can be number, string, bool, 
    // null, undefined, array, function,  or another object

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

* OOP: Collection of objects that talk to each other to perform some functionality.
* In OOP terms these functions in an objects are called methods.

## [2] Factory Functions

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

## [3] Constructor Function

* This is one another way to create or construct an object.
* While creating constructor we should use Pascal Notation by JS convention.
* Camel Notation: oneTwoThreeFour
* Pascal Notation: OneTwoThreeFour

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




// Constructor Function

function Circle(radius) {
    // this is a reference to the object that is executing this piece of code
    // imagine "this" references an empty object
    // instead of returning an object in factory function we are going to use "this" keyword to initialize an object

    this.radius = radius;
    // here we are adding a property "radius" and assigning it incoming radius parameter
    // Note that In JS we can use dot notation to read a property and also to set a property
    // In JS objects are dynamic meaning once we create it we can additional propoerties or methods to them

    this. draw = function (){ // adding a method draw
        console.log('draw');
    }
}

const circle = new Circle(1);
// When you write new 3 things happens: 
// 1. This new operator creates an empty JS object like this "const x = {};"
// 2. Now "this" operator will point to this new empty object
// 3. and finally function "Circle" will return that x = {} object with all the properties from the function "Circle"

```

**Difference between Factory Function and Constructor Function:**

1. 

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

## [4] Dynamic Nature of Objects

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

* Notice that here the object is declared as `const` this does not mean that we are not able to add or delete the properties.
* This means that the **object circle cannot be over-ridden**

## [5] Constructor Property

* Every Object in JS has a property called constructor which was used to construct or create the object.
* To check the constructor of the function we can type this in console.

```javascript
objectName.constructor
```

* and the output obtained is ***f Object { [native.code] }***
* This is a builtin constructor function in JS. When we create an object using object literal syntax, internally JS engine uses this constructor function.

* When we define a new object `let x = {};`
* JS engine will translate that to something like this `let x = new Object();`

```javascript
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

If we try to check constructor here 

```javascript
circle1.constructor
```

then it will be  ***f Object { [native.code] }***. **This is a built-in constructor function in JavaScript.**

This is because we created this function first using `const circle1` and then we returned it from our factory function and because we used object literal syntax internally it was created with this object constructor function.

In JS we have few other constructors, example

```javascript
new String(); // but we use string literals to create strings '', "", ``
// using the literals is cleaner and simpler than using the constructor
new Boolean(); // but we have boolean literals true, false
new Number(); // 1, 2, 3,..
```

**Every Object has a constructor property and that references a function that was used to create that object.**



## [6] Functions are Objects

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
* As we know functions are objects hence who created this object ?
* Check `Circle.constructor`
* Answer will be ***f Function() { [native.code] }***
* hence when we declare a function using `function Circle(radius)` syntax, internally JS engine will use this function constructor to create this object.
* To check this we can create an object directly using `Function` **constructor** of the function. Just like we have `new String(), new Boolean(), new Number()` constructor functions we have `new Function()` constructor for function.

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

Now if we will check `Circle1.constructor` in the console then we will be able to observe  ***f Function() { [native.code] }***

**Now let us look into some methods of the functions**

**Call method for calling a function**

```javascript
function Circle(radius) {
    this.radius = radius;
    this. draw = function (){ // adding a method draw
        console.log('draw');
    }
}

Circle.call({}, 1); // first argument is this argument. here we need to pass an empty object {}. this in Circle will reference to the {} object that we pass in the method
// then the other argument is the radius
// if we have multiple arguments it will be mentioned in sequence Circle.call({}, 1, 2, ...)

const another = new Circle(1);
```

* `Circle.call({}, 1);` is exactly similar to `const another = new Circle(1);`
* When we use the new operator, this new operator will internally create an empty object {} and pass that as the first argument to the call method.
* When we don't use the new operator `this` will point to a global object which is **window**.
* Hence this time call method will have window as an argument instead of {}.

```javascript
Circle.call(window, 1); 

const another = Circle(1);
```

**apply method for calling a function**

apply method is similar to call method just that we pass the list of arguments in an array. This is useful when we already have an array somewhere in your application and you want to pass an array as the second argument to the apply method.

```javascript
Circle.apply(window, [1, 2, 3]); 
```

## [7] Value vs. Reference Types

**Value Types**

* Number
* String
* Boolean
* Symbol
* undefined
* null



**Refrence Types**

* Object 
* Function
* Array



* **In JS Functions and arrays are objects hence in JS we have primitives and objects.**

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



![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Images\1.PNG)



Summary:

* **Primitives are copied by their value**
* **Objects are copied by their reference**



```javascript
let number = 10;

function increase(number) {
    number ++;
}

increase (number);
console.log(number);
```

* Note that in this example the local parameter number of the increase function gets out of the scope as the function is executed. Hence here we are dealing with two individual values both having the name number

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



## [8] Enumerating Properties of an Object

### 1. Objects are not iterable using for of

```javascript
const circle = {
    radius: 1, 
    
    draw: function() { // here the value is a function in key-value pair
        console.log('draw');
    }
};


for (key in circle) 
console.log(key, circle[key]);

// notice that this will give array as objects are not iterable
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



Summary of what we have learnt so far

1. Whenever we create an object using object literal syntax, internally the call to Object constructor function is made.

```javascript
const x = {value: 1}; // using object literal syntax
const x = new Object(); // the above statement is translated internally like this

function Object() {} // Object constructor function defined somewhere internally is thus called.

```

2. All functions in JS are objects, hence the property and methods of the functions can be accessed using the dot notation.





### 3. In Operator

Finally sometimes we want to see if given object has given property or method. For this we can use `in operator`

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

if ('radius' in circle) console.log('yes');
```



## [9] Cloning an Object

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

## [10] Garbage Collector

In low level languages like C/C++ we have to allocate the memory while creating an object and when we're done we need to deallocate memory.

In JS though when we create an object, memory is allocated to this object next we can use that but when we are done using we don't need to deallocate the memory because of **Garbage Collector**

The job of this **Garbage Collector** is to find the variables and constants that are no longer used and then deallocate the memory that were allocated to them.

## [11] Builtin Object - Math

Refer - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

## [12] Builtin Object - String

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

![1569429739400](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1569429739400.png)

## [13] Template Literals

Code looks really ugly and messy when we want to use escape notation.

```javascript
const message = 'This is my\n' + 
'\'first\' message'
```

To avoid this situation from ES6 we have template literals

Similar to 

Object literal `{}`

Boolean `true, false`

String literal `'', ""`

**we have template literal ``**

Example 

```javascript
const another = 
`This is my
'first' message`;
```

This is particularly useful while writing an email.

Another benefit is that here we can use place holders instead of using the concatenate operator + with escape notation.

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

```javascript
// All these three constructors below are used for creating date object.
// There are many other formats apart from these three which are supported, these formats can be found in documentation.

const now = new Date();
const date1 = new Date('May 11 2018 9:00') 
const date2 = new Date(2018, 4, 11, 9, 0)


// All these have get and set method
console.log(now.getDate());
now.setFullYear(2017);

// All these date objects have few methods for converting them to a string.
console.log(now.toDateString());
console.log(now.toTimeString());
console.log(now.toISOString());
```

## [15] Exercise 1 - Address Object

```javascript
address = {
    street: 'Lisbon Dr',
    city: 'San Jose',
    zipcode: 95132
}

//console.log(address.street);


function printObject() {
for (let value in address) 
    console.log(value, ":", address[value]);
}

printObject();

/* OTHER WAYS TO ITERATE OVER OBJECT
for (let value of Object.keys(address)) {
    console.log(value, ":", address[value]);
}

for (let entry of Object.entries(address)) {
    console.log(entry);
} */
```

## [16] Factory and Constructor Function

```javascript
function address(street, city, zipcode) {
    return {
    street,
    city,
    zipcode,
    };
}

Ibrahim_address = address ("Lisbon", "San Jose", 95132);

console.log(Ibrahim_address);

function ConstructorAddress(street, city, zipcode) {
    this.street = street;
    this.city = city;
    this.zipcode = zipcode;
}

address1 = new ConstructorAddress("Lisbon", "San Jose", 95132);

console.log(address1);
```

## [17] Exercise 3 - Object Equality

* Objects are reference types meaning we can have two objects with the exact same properties but these objects are at different memory locations. hence when we use the equality operator === we're essentially checking to see if these objects have the same reference. **Hence to properly check their properties, we need to make sure that all their properties are equal.**
* **When we use === operator we're essentially checking to see if these objects have the same reference.**

```javascript

function Address(street, city, zipcode) {
    this.street = street;
    this.city = city;
    this.zipcode = zipcode;
}

let address1 = new Address("Lisbon", "San Jose", 95132);
let address2 = new Address("Lisbon", "San Jose", 95132);
let address3 = address1;

function areEqual(address1, address2) { // check to see if they have same properties

   return (address1.city === address2.city && address1.street === address2.street && address1.zipcode === address2.zipcode);
}

function areSame(address1, address2) { // check to see if they are pointing to the exact same object.

    return (address1 === address2);
}

console.log(areSame(address1, address3));
console.log(areEqual(address1, address2));
```

## [18] Exercise 4 - Blog Post Object

```javascript
let blogpost = {
    title: "Google",
    body: "Senior Software Engineer at Google",
    author: "Ibrahim",
    views: 10000,
    comments: [{author: "Family", body: "Olay"}, {author: "Friends", body: "Halaluea"}],
    isLive: true
}

console.log(blogpost);
```

## [19] Exercise 5 - Constructor Functions

```javascript
let blogpost = {
    title: "Google",
    body: "Senior Software Engineer at Google",
    author: "Ibrahim",
    views: 10000,
    comments: [{author: "Family", body: "Olay"}, {author: "Friends", body: "Halaluea"}],
    isLive: true
}

//console.log(blogpost);

function ConstructorBlogPost (title, body, author) {

    this.title = title,
    this.body = body,
    this.author = author,
    this.views = 0,
    this.comments = [],
    this.Live = false
}

let newpost = new ConstructorBlogPost('a', 'b', 'c');

console.log(newpost);
```

## [20] Exercise 6 - Price Range Objects

```javascript
let priceRange = [
    { label: '$', tooltip: 'Inexpensive', minPerPerson: 0, maxPerPerson: 10},
    { label: '$$', tooltip: 'Moderate', minPerPerson = 11, maxPerPerson: 20},
    { label: '$$$', tooltip: 'Expensive', minPerPerson = 21, maxPerPerson: 50}

]

let restaurants = [
    { averagePerPerson: 5}
]
```

