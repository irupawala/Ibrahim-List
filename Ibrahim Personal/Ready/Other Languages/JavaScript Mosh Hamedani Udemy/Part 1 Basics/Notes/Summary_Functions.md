## [1] Function Declarations Vs Expressions

**Function Declaration**

```javascript
// Function Declaration

function walk() {
    console.log('walk');
}
```

There is another way to define function in JS. just like how string, numbers and objects are defined.

**Function Expression**

```javascript
let run = function() {};
let x = 1;
```

* In JS functions are objects hence setting the variable to a function is similar to setting it to an object.
* Note that while defining function using Function Expression we put a semicolon (;) at the end

Function Expressions can also be of two types

**Anonymous Function Expression**

```javascript
let run = function() {
    console.log('run');
};

run();
let move = run; // here both move and run are poiting to the same object in memory

```

**Named Function Expression**

```javascript
let run = function walk() {
    console.log('run');
};

run();
```

## [2] Hoisting

**Key Difference between function Declaration and Expression**

* The function defined using declaration can be called **before definition** but function defined using expression cannot be called.
* The reason for this is function defined using expression is exactly similar to the variable.

```javascript
// Function Declaration

walk();

function walk() {
    console.log('walk');
}


// Function Expression

run(); // This will give error

let run = function walk() {
    console.log('run');
};

run();
```

* The reason is when JS engine executes the code it moves all the function declaration at the top. This is called as Hoisting. 
* **Hoisting is moving function declaration at the top of the code.**

## [3] Arguments

* JavaScript is a Dynamic language.
* This concept also applies to the arguments of a function.

```javascript
function sum(a,b) {
    return a + b; 
}
```

```javascript
console.log(sum(1,2));
console.log(sum(1));// o/p will be NaN
console.log(sum()); // o/p will be NaN
console.log(sum(1, 2, 3));
```

* In JS we also have the flexibility to pass as many arguments as we want and get their sum.

**arguments Object**

* Every function in JS has a special object called arguments. This **object** lists all the values passed to the function **along with the index.**

```javascript
function total() {
        console.log (arguments);
    }

total(1, 2, 3, 4, 5, 10);
```

hence rewriting the function sum 

```javascript
function sum () {
    let total = 0;
    for (let value of arguments)
        total += value;
    return total;
}

console.log(sum(1, 2, 3, 4, 5, 10));
```

## [4] Rest Operator

* Rest Operator (... args) will take in all the arguments passed to it just like arguments object but Rest operator will put all the arguments in an **array.**

```javascript
function sum (... args) {
	console.log(args)
}

console.log(sum(1, 2, 3, 4, 5, 10));
```

```javascript
function sum (...args) {
    return args. reduce((a, b) => a + b);
}

console.log(sum(1, 2, 3, 4, 5, 10));
```

Let's assume we want to write a function where we perform the sum of all the items in the shopping cart and then provide 10% discount.

```javascript
function sum(discount, ...args){
    const total = args.reduce((a,b) => a + b);
    return ((1 - discount) * total);
}

console.log(sum(0.1, 20, 30));
```

* Notice the difference in signature between arguments and args. **In arguments you don't have to give any parameters while in args you must give (...args) parameter to the function.**

```javascript
function total() {
        console.log (arguments);
    }
```

```javascript
function sum (... args) {
	console.log(args)
}
```

## [5] Default Parameters

* Starting from ES6 we can give default value in the function itself

```javascript
function interest(principal, rate = 3.5, years = 5) {
    return principal * rate /100 * years;
}

console.log(interest(10000))
```

* Before ES6 we have to define the default values in the following way.

```javascript
function interest(principal, rate, years) {
    rate = rate || 3.5;
    years = years || 5;
    return principal * rate /100 * years;
}

console.log(interest(10000))
```

* here note that when rate and years are not passed then those values are undefined and hence the result of || function will take truthy values.

## [6] Getters and Setters

```javascript
const person = {
    firstName: 'Mosh',
    lastName: 'Hamedani',
    fullName() {
        return `${person.firstName} ${person.lastName}`
    }
};

console.log(person.fullName());
```

* In this example we need to print the full name of the object
* We can define a method inside the object and then call that method as shown above however this methodology has some issues which is that we cannot change the person's name from outside the function and also we would like to treat the fullName method like a property (that is without {} braces while calling them) instead of function.
* This is when getters and setters comes into play. Notice that **getters is accessors in C++ while setters is mutators.**

* To covert the method to getter simply write get before method name.
* To write setter, set the value of the required parameter in the setter

```javascript
const person = {
    firstName: 'Mosh',
    lastName: 'Hamedani',
    get fullName() {
        return `${person.firstName} ${person.lastName}`
    },
    set fullName(value) {
        const parts = value.split(' ');
        // person.firstName = parts[0];
        // person.lastName = parts[1];
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};

person.fullName = 'John Smith'

console.log(person);
console.log(person.fullName);
```



## [7] Try Catch

* In the previous code we assumed that function receives only string however it may receive different type of data also.
* In those cases it is sometimes better to ignore those inputs and execute the function based on default inputs.
* Notice the if statement here if the passed data is not a string it will return the default value of the function.

```javascript
const person = {
    firstName: 'Mosh',
    lastName: 'Hamedani',
    get fullName() {
        return `${person.firstName} ${person.lastName}`
    },

    
    set fullName(value) {
        if(typeof value !== 'string') return;
        
        const parts = value.split(' ');
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};

//person.fullName = 'John Smith'
//person.fullName = true;
person.fullName = null;

console.log(person);
console.log(person.fullName);
```

* Sometimes we would like to throw an exception if the input is not what we desire.
* There is a minor difference between Error and Exception

```javascript
const e = new Error();// This will create a simple error object
```

* As soon as we throw this error it becomes an exception.

```javascript
const e = new Error();// This will create a simple error object
throw e;
```

* Hence consider the code when input is null

```javascript
const person = {
    firstName: 'Mosh',
    lastName: 'Hamedani',
    get fullName() {
        return `${person.firstName} ${person.lastName}`
    },

    
    set fullName(value) {
        if(typeof value !== 'string') 
            throw new Error('Value is not a string.'); // notice that Error is a constructor as it has a pascal notation as we wrote new we are creating a new error object

        const parts = value.split(' ');
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};


try {
person.fullName = null;
}
catch(e) { // exception thrown is caught here
    alert(e)
}

console.log(person);
console.log(person.fullName);
```

* What happens when we throw an empty string. It will consider the first name as empty string but last name is still "undefined". This is not what we want.
* Hence in the code below we will check if the length of the array created from the full name is 2 if it is not then we want to throw an error.

```javascript
const person = {
    firstName: 'Mosh',
    lastName: 'Hamedani',
    get fullName() {
        return `${person.firstName} ${person.lastName}`
    },

    
    set fullName(value) {
        if(typeof value !== 'string') 
            throw new Error('Value is not a string.'); // notice that Error is a constructor as it has a pascal notation 
                               // as we wrote new we are creating a new error object

        const parts = value.split(' ');
        if (parts.length !== 2)
            throw new Error('Enter a first and last name')
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};


try {
person.fullName = "";
}
catch(e) {
    alert(e)
}
console.log(person);
console.log(person.fullName);
```

## [8] Local Vs Global Scope

* Defines where the variable defined is accessible.
* Scope of a variable defined is limited with the code block, if statement, for statement and function within which it is defined. 
* There is also a global keyword whose scope is throughout the program.

## [9] Let Vs Var

* This code will throw an error as the scope of i is limited only within the for loop as expected.

```javascript
function start() {
    for (let i = 0; i < 5; i++)
    console.log(i);

    console.log(i);
}

start()
```

* Using var instead of let however won't throw an error as the **scope of var is limited to function and not limited to the block in which it is defined**

```javascript
function start() {
    for (var i = 0; i < 5; i++)
    console.log(i);

    console.log(i);
}

start()
```

Hence:

1. **var => function-scoped**

2. **let , const => code block-scoped**

   

* **The second problem with var is whenever we define var outside the function this creates a global variable to the window object in the browser.**
* In contrast when we use the let keyword to define a global variable it won't attach itself to the window object.
* Window is something central and there is only one instance of window object. If you are using a third party library and if that library also has a variable with the same name, that variable can override your variable. So you should avoid adding stuff to the window object.
* Also notice that function defined is also a global function and attaches itself to the window object. **To prevent this we have to encapsulate these functions in separate modules so they are not added to the windows object.**

```javascript
var color = 'red';
let age = 30;

function sayHi() {
    console.log('hi');
}
```

### **Three problems with Var:**

1. **Scope** - Scope of var is limited to function and not limited to the block in which it is defined.
2. **Global Window Object** - Whenever we define var outside the function this creates a global variable to the window object in the browser.
3.  **Re-declaration** - *let* variables cannot be re-declared while var variable can be re-declared in the same scope. 

Refer the link for more info:

 https://codeburst.io/difference-between-let-and-var-in-javascript-537410b2d707 



**Example 2:**

Even if the *let* variable is defined as same as *var* variable globally, the *let* variable will not be added to the global window object. 

Check this code:

```javascript
var varVariable = 'this is a var variable';
let letVariable = 'this is a let variable';

console.log(window.varVariable); //this is a var variable
console.log(window.letVariable); //undefined
```

**Example 3:**

```javascript
var varVariable = 'this is a var variable';
var varVariable = 'this is a var variable';
let letVariable = 'this is a let variable';
let letVariable = 'this is a let variable';


console.log(window.varVariable); //this is a var variable
console.log(window.letVariable); //undefined
```

## [10] This Keyword

* ***this*** keyword refers to an object, that object which is executing the current bit of javascript code. 
* ***this*** refers to the object that is executing the current function.
* To understand ***this*** keyword, only we need to know how, when and from where the function is called, does not matter how and where function is declared or defined. 

### 1. Implicit Binding

* **If the function is a part of the object we call it a method. So if that function is a method in an object `this` references the owner object itself.**

```javascript
const video = {
    title: 'a',
    play() {
        console.log(this);
    }
}

video.stop = function() {
    console.log(this);
};

video.stop()
video.play();
```

* In the example above as the function is a method defined inside an object this references that object itself.

### 2. Default Binding

i. **if that function is a regular function which means it is not part of an object, then `this` references to the global object, which is the window object in the browsers and global in node.**

* When the function is defined outside the object then if we log this on the console, we're going to see the global object which is window in browser and global in node.

```javascript
function playVideo() {
    console.log(this);
}

playVideo(); // This will give Window object in browser
```

​		ii. **Also alone, `this` refers to the global object.** 

```javascript
console.log(this);
```

​		iii.  **In a function, in strict mode, `this` is `undefined`.** 

write in console.

```javascript
"use strict";
console.log(this);
```

**Another Example of Default and Implicit Binding**

```javascript
var obj1 = {
  name: "Pulsar",
  bike: function() {
    console.log(this.name);
  }
}
var obj2 = { name: "Gixxer", bike: obj1.bike };
var name = "Ninja";
var bike = obj1.bike;

bike();           // "Ninja"
obj1.bike();      // "Pulsar"
obj2.bike();      // "Gixxer"
```

### 3. Explicit Binding

* The `call()`,  `apply()` and `bind()` methods are predefined JavaScript methods.

* They can be used to call an object method with another object as argument.
* They all attach ***this*** into function (or object) and the difference is in the function invocation.

**1. Call Method:**

 **call** attaches ***this*** into function and executes the function immediately: 

```javascript
var person = {  
  name: "James Smith",
  hello: function(thing, space) {
    console.log(this.name + " says hello " + thing + " " + space);
  }
}

person.hello("world", "earth");  // output: "James Smith says hello world"

person.hello.call({ name: "Jim Smith" }, "world", "mercury");

```

**2. Apply Method:**

 **apply** is similar to **call** except that it takes an array-like object instead of listing the arguments out one at a time: 

```javascript
person.hello.apply({ name: "Raghuram Rajan" }, ["world", "jupiter"]);
```

**3. Bind Method:**

* bind will return a new function and sets this to point to the object defined here permanently.

 **bind** attaches **this** into function and it needs to be invoked separately like this: 

```javascript
var helloFunc = person.hello.bind({ name: "Ibrahim Rupawala" });
helloFunc("world", "venus");  
```

 or like this: 

```javascript
var helloFunc = person.hello.bind({ name: "Jim Smith" }, "world", "pluto");
helloFunc();  
```

Entire code combined

```javascript
var person = {  
  name: "James Smith",
  hello: function(thing, space) {
    console.log(this.name + " says hello " + thing + " " + space);
  }
}

person.hello("world", "earth");  // output: "James Smith says hello world"

person.hello.call({ name: "Jim Smith" }, "world", "mercury");

person.hello.apply({ name: "Raghuram Rajan" }, ["world", "jupiter"]);

var helloFunc = person.hello.bind({ name: "Ibrahim Rupawala" });
helloFunc("world", "venus");  

var helloFunc = person.hello.bind({ name: "Jim Smith" }, "world", "pluto");
helloFunc();  
```



### 4. This for Constructor function

* Now what if we have a constructor function. The in that case `this`  refers to the new object created using constructor function.
* In this case we will get new Object Video.

```javascript
function Video(title) {
    this.title = title;
    console.log(this);
}

const v = new Video('b'); // {}
```

**Another Example**

```javascript
function bike() {
  var name = "Ninja";
  this.maker = "Kawasaki";
  console.log(this.name + " " + maker);  // undefined Bajaj
}

var name = "Pulsar";
var maker = "Bajaj";

obj = new bike();
console.log(obj.maker); // "Kawasaki"
console.log(obj.name); // undefined
```

* Here name is undefined because any property gets assigned to the empty function created by constructor if it is assigned like this `this.name = name`
* Also undefined Bajaj is printed by the function because `this` is a constructor object here and `name` is not defined by the constructor. Also it is written `maker` in console.log and not `this.maker` hence maker refers to the global `maker` and `maker` is being attached to the window object using `var maker` later hence Bajaj gets printed



**Example of this:**

* We want to print the elements of an array using this keyword.

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag){
            console.log(tag);
    });
}
};

video.showTags();
```

Now what if we want to print the title along with each tags.

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag){
            console.log(this.title, tag);
            //console.log(this, tag); // try this piece of code
    });
}
};

video.showTags();
```

* Notice here that this.title won't refer to the object here, this is because here "this" is inside a function and not the method.
* **To refer the object itself we have to define this within the method and not the function within the method.**

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag){ // notice that forEach method has two arguments, callback function and this arg
            console.log(this.title, tag);
    }, this /*{firstName: 'Mosh'}*/); // here we are not inside a callback function hence this references to the current object, we are still in the execution context of the showTags method
}
};

video.showTags();
```

* But notice that not all the methods give the flexibility to add this argument as a parameter like forEach

## [11] Changing this

* Notice that for those kind of methods which do not allow declaring this as an argument we can assign this to a new variable before the function starts in the showTags() method itself

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        const self = this;
        this.tags.forEach(function(tag){ 
            console.log(self.title, tag);
    }); 
                                      
}
};

video.showTags();
```

* Also, we can use bind method to point to a particular object permanently.

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag){ 
            console.log(this.title, tag); // notice here that this in the function now is binded to whatever the object is given in bind as an argument
    }.bind(this /*video*/)); // this references video object, we can also use video
                                      
}
};

video.showTags();
```

* But there is a more elegant way to solve this problem.
* Whenever we use the arrow function => then, the arrow function will inherit this from the containing function. 
* In other words "this" in the callbackfn is not rebound to a new object but refers to the same object the method containing it refers to.

```javascript
const video = {

    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(tag => { 
            console.log(this.title, tag);
    }); 
                                      
}
};

video.showTags();
```
