## [1] Variables

* `var` was used to declare a variable
* From ES6 `let` is used 

```javascript
let name = 'Ibrahim';
console.log(name)

// Rules for variables
// Cannot be reserved keyword
// Should be meaningful
// Cannot start with a number
// Cannot contain a space or hyphen
// Are case-sensitive
// let interestRate - camelCasing
```

## [2] Constants

* Uses keyword `const`
* Does not allow re-assignment if defined as const

```javascript
const interestRate = 0.3;
interestRate = 1;
console.log(interestRate);
```

## [3] Primitive Types

* There are two kinds of values you can assign to a variable in JV.
  1. Primitive/ Value Types
  2. Reference Types
* Primitive Types has following categories
  * String
  * Number
  * Boolean
  * undefined
  * Symbol (defined new in ES6)
  * Null

```javascript
let name = 'Ibrahim'; // string literal
let age = 30; // Number literal
let isApproved = true; // Boolean literal
let firstName; // undefined literal
let middleName = undefined; // undefined literal
let SelectedColor = null; // undefined literal, used in situation where one wants to clear a value of variable
```

## [4] Dynamic Typing

* In static language the type of the variable cannot be changed once defined.
* In Dynamic language like JavaScript the type of a variable can change at runtime.

```javascript
// Type this in console

typeof name;
name = 1;
typeof name; // note now that type will be changed
```

```javascript
// Type this in console

typeof(age);
age = 30.5
typeof(age);
```

* **Note that in JV we don't have floating point numbers and integer numbers. All numbers are just numbers.**

```javascript
typeof isApproved;
typeof firstName; // value is undefined and also the type is undefined
typeof selectedColor; // type of null is Object

```

* for firstName value is undefined and also the type is undefined
* type of null is Object

## [5] Objects (Reference Types)

* There are 3 reference types in JavaScript:
  * Object
  * Array
  * Function
* Object is like an object in real life. Think of a person it has name, age, address and so on.
* You can put multiple variable inside of an object.
* If some variables are highly related then we can define an object which contains all these variables and then reference these objects.

```javascript
let name = 'Mosh';
let age = 30;

let person = { // these curly braces are called object literals
    name: 'Mosh', // In this literals we have to also add key:value pairs
    age: 30 // These are also called properties of an object
};

console.log(person); // referencing the object
```

```javascript
// There are two ways of accessing properties

// Dot Notation
person.name = 'John';

// Bracket Notation
person['name'] = 'Mary'; // Notice that here we have pass a STRING of target property

console.log(person.name);
console.log(person['name']);
```

Dot Notation is concise. While bracket notation has its own advantages:

- sometimes we don't know the name of the target property during until the runtime. The user will select the name of the property during runtime. Hence at those times we can assign the property to the variable and use bracket notation to access the property in a dynamic way.

```javascript
// Bracket Notation
let selection = 'name'; // assign during runtime
person[selection] = 'Mary'; // accessed dynamically using variable selection
```

## [6] Arrays (Reference Types)

- Array is a data structure to create list of items
- In Javascript we can store different types in an array.

```javascript
let selectedColors = ['red', 'blue']; 
console.log(selectedColors);
comsole.log
```

- Hence technically the array is an object as it has key value pairs or properties which we can access using dot notation.

```javascript
typeof selectedColors
```

- Hence we can see the property of this array or object using dot notation

```javascript
//console.log('Ibrahim');

let selectedColors = ['red', 'blue']; // array literal
selectedColors[2] = 'green';
selectedColors[3] = 1;
console.log(selectedColors);
console.log(selectedColors[0]);
console.log(selectedColors.length); // like length we have many properties
```

## [7] Functions (Reference Types)

* A set of statement that performs a task

```javascript
function greet() {

    console.log('Hello World');

}

greet();

function person(name) { // name is the parameter to the person function

    console.log('Hello ' + name);
}

person('John'); // John is an argument to the person function

function person_name(name, lastName) {

    console.log('Hello ' + name + lastName);
}

person_name ('John ', ); // note what happens when the parameter is undefined
```

**Remember that the default value of any parameter in java is undefined**

## [8] Types of Functions

There are two kinds of functions:

* Performing a task
* Calculating a value

```javascript
// Performing a task
function person_name(name, lastName) {

    console.log('Hello ' + name + lastName);
}

person_name ('John ', ); // note what happens when the parameter is undefined

// Calculating a value
function square(number) {
    return number * number;
}


console.log(square(2)); // console.log is also a function
```

