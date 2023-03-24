## [1] Creating your own prototypical Inheritance

* Prototypical Inheritance is a way using which we can inherit.
* Let's say we have a function called `duplicate` which we should be able to inherit for all the shapes like circle and square. In other words, in the example below we don't want duplicate to be defined as a prototype function for all the constructors like circle, square, etc.
* Hence, we will have a shape object and put this duplicate object there and than inherit duplicate method to all the objects like circle, square, etc.

```javascript
// Shape Objects
function Shape() {
}

Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

// Circle Objects
function Circle(radius) {
  this.radius = radius;
}

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1);
```

* Notice that in the case above `s.__proto__.__proto__ === c.__proto__.__proto__`

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\26.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\27.PNG)

* For Inheritance to work we want circleBase inherit from shapeBase.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\28.PNG)

* To do this we have a method in JS to create an object with given prototype called `object.create`
* circleBase used to inherit from the objectBase. But now we will change the circleBase to a NEW object which inherits from shapeBase.
* We want a new circleBase object which inherits from shapeBase instead of objectBase
* `create` is a method for creating an object with given prototype. Argument to the function is Object to use as a prototype.
* `Object.create(Shape.prototype)` returns an object which inherits from shapeBase

```javascript
// Shape Objects
function Shape() {
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

// Circle Objects
function Circle(radius) {
  this.radius = radius;
}

// Before Changing the prototype of Circle

Circle.prototype = Object.create(Object.prototype); // circleBase used to inherit from the objectBase
// This is implit relationship

// But now we will change the circleBase to a NEW object which inherits from shapeBase
// After Changing the prototype of Circle

// To setup inheritance circleBase should inherit from shapeBase
// We want a new circleBase object which inherits from shapeBase instead of objectBase
Circle.prototype = Object.create(Shape.prototype) // create is a method for creating an object with given prototype. Argument to the function is Object to use as a prototype
// This statement above will returns an object which inherits from shapeBase


// NOTICE THIS VERY IMPORTANT POINT. Here it is necessary to add the draw function after changing the prototype of Circle.
// If you define this before changing the circle prototype then draw method won't be available in new circleBase
Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\29.PNG)

* Notice from the image above that Circle is inherited from circleBase which is now inherited from shapeBase (and not objectBase) which is again inherited from objectBase.
* Also notice that name besides `__proto__:` Shape, Object is the parent object from which given object is inherited.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\30.PNG)

* Notice that now c has duplicate object which is inherited from shapeBase. This is prototypical inheritance in action.



## [2] Resetting the Constructor

* Consider the code below

```javascript

// Shape Objects
function Shape() {
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

// Circle Objects
function Circle(radius) {
  this.radius = radius;
}

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1);
```

* Remember that

```javascript
Circle.prototype === c1.__proto__
```

* Every Object in JS has a constructor property that returns the function that was used to construct or create that object.
* Now observe the image below

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\31.PNG)

* Notice that with the property constructor in circleBase we can create an object in the dynamic fashion as shown above using `new Circle.prototype.constructor(1)`. This expression is equivalent to `new Circle (1)`. We use the later form because it is clean but in some scenarios we have to also use the constructor property to dynamically create an object using the constructor function.

* Now for the prototypical Inheritance when we change the circleBase to a new object which inherits from the objectBase, the new prototype for the Circle object that is new CircleBase does not have constructor property.

```javascript

// Shape Objects
function Shape() {
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

// Circle Objects
function Circle(radius) {
  this.radius = radius;
}

Circle.prototype = Object.create(Shape.prototype)

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\32.PNG)

* Notice in the figure above the Circle.prototype no longer has the constructor. Hence when we try to create an object using the constructor in the prototype of the circle we get Shape {}
* The reason we are having this problem is because we have reset the prototype of the circle. Hence we will no longer be able to create an object dynamically using the `Circle.prototype.constructor()`
* Hence as a best practice whenever we reset the prototype of an object we should also reset the constructor.

```javascript

// Shape Objects
function Shape() {
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

// Circle Objects
function Circle(radius) {
  this.radius = radius;
}

// Circle.prototype.constructor = Circle;
// new Circle.prototype.constructor() ==> new Circle(); These two statements are exactly equivalent
// Notice that before the line below constructor was Circle.prototype.constructor = Circle as shown above
Circle.prototype = Object.create(Shape.prototype);
// Hence resetting the constructor back to circle after changing the prototype
Circle.prototype.constructor = Circle;

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1);
```

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\33.PNG)

Now we can create the objects dynamically using `Circle.prototype.constructor(1)`

## [3] Calling the Super Constructor

* In the previous example discussed what if we have a parameter in our parent prototype `color` here. Then by the inheritance point of view every circle object should also have color property and that should be initialized at the time of creating the circle.
* To do this in the color constructor we should call the shape constructor.

```javascript
function Shape(color) {
    this.color = color
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

function Circle(radius, color) {
    Shape(color);
  this.radius = radius;
}

Circle.prototype = Object.create(Shape.prototype);
Circle.prototype.constructor = Circle;

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1, "red");
```

* But notice that when we check the `c object`  in the console than we will not see color property this is because when we use new operator then it created empty object and then sets ***this*** to point to that object. Hence here we have set radius property to that new object and finally that new object will be returned from the constructor.
* Also, it didn't worked because when we called Shape in the Circle constructor we didn't new it up hence when we don't use new than this in the shape is pointing to window in browser and global in node. Hence color property is not set on Circle object but the window object. check this by typing window.color in console.
* If `new Shape(color)` used in the Circle than ***this*** will create another object and it will set color property on that new object.
* To fix this we have to use call method and set ***this*** in the shape function to point to the new instance of the circle object.

```javascript

function Shape(color) {
  this.color = color;
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

function Circle(radius, color) {
  Shape.call(this, color);
  this.radius = radius;
}


Circle.prototype = Object.create(Shape.prototype);
Circle.prototype.constructor = Circle;

Circle.prototype.draw = function() {
  console.log('draw');
}

const s = new Shape();
const c = new Circle(1, "red");
```



![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\34.PNG)

* Observe now that c has both the properties, color and radius.

## [4] Intermediate function Inheritance

```javascript

function Shape(color) {
  this.color = color;
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

function Circle(radius, color) {
  Shape.call(this, color);
  this.radius = radius;
}


Circle.prototype = Object.create(Shape.prototype);
Circle.prototype.constructor = Circle;

Circle.prototype.draw = function() {
  console.log('draw');
}

function Square (size) {
  this.size = size;
}

Square.prototype = Object.create(Shape.prototype);
Square.prototype.constructor = Square;

Square.prototype.dimension = function() {
  Console.log('dimension');
}

const s = new Shape();
const c = new Circle(1, "red");
const sq = new Square(3);
```

* Notice that how in the code above we have defined a new object Square which inherits from the Shape Object.
* But notice that the 2 lines required to create prototypical inheritance is kind of too much of code and can lead to errors when too many objects are required to be inherited.
* Hence we can define a function with this two parameters and name the two parameters parent and child as shown in the code below. This extend function is what we call `intermediate function inheritance.`

```javascript
function extend (Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}

```



```javascript
function Shape(color) {
  this.color = color;
}
Shape.prototype.duplicate = function() {
  console.log('duplicate');
}

function extend (Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}

function Circle(radius, color) {
  Shape.call(this, color);
  this.radius = radius;
}

extend (Circle, Shape);
Circle.prototype.draw = function() {
  console.log('draw');
}

function Square (size) {
  this.size = size;
}

extend (Square, Shape);
Square.prototype.dimension = function() {
  Console.log('dimension');
}

const s = new Shape();
const c = new Circle(1, "red");
const sq = new Square(3);
```



## [5] Method Overriding

* Using the same method name with different functionality in the child object.
* We can do this by simply redefining the same method on the child object as shown below. This should be done only after the extend function because that will define the method in the new prototype set in the extend function.

```javascript
function extend (Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}

function Shape() {
}

Shape.prototype.duplicate = function() {
  console.log('duplicate');
}


function Circle() {
}

extend (Circle, Shape);

Circle.prototype.duplicate = function() {
  console.log('duplicate Circle');
}

const c = new Circle();
```

* Notice that this happens because the way in which javascript prototypical inheritance works is that when we access the method or property JS engine walks up the prototypical chain and picks the first implementation.
* But notice that sometimes we need to call the method in the parent object, to do that we have to simply call the method defined in the parent into the child method.

```javascript
function extend (Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}

function Shape() {
}

Shape.prototype.duplicate = function() {
  console.log('duplicate');
}


function Circle() {
}

extend (Circle, Shape);

Circle.prototype.duplicate = function() {
  Shape.prototype.duplicate(this); // Notice that this function does not make any difference in this example.
  console.log('duplicate Circle');
}

const c = new Circle();

```

## [6] Polymorphism

```javascript
function extend (Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}

function Shape() {
}

Shape.prototype.duplicate = function() {
  console.log('duplicate');
}


function Circle() {
}

extend (Circle, Shape);

Circle.prototype.duplicate = function() {
  console.log('duplicate Circle');
}

function Square() {
}

extend (Square, Shape);

Square.prototype.duplicate = function() {
  console.log('duplicate Square');
}

// Ibrahim
// const c = new Circle();
// const sq = new Square();

// my_array = [c, sq];

// my_array.forEach(element => { element.duplicate(); });

// Mosh
shapes = [
  new Circle(),
  new Square()
]

for (let shape of shapes) {
  shape.duplicate();
}
```

* Notice that polymorphism is nothing but calling the function of same name in different objects. Advantage being each method of a particular object will have it's own implementation.
* It is very powerful to use the OOP and Polymorphism because if we don't do that code will be large and difficult to manage

```javascript
for (let shape of shapes) {
  if (shape.type === 'circle')
  	duplicateCircle();
  else if (shape.type === 'square')
  	duplicateSquare();
  else
    duplicateShape();
}
```

* The advantage of OOP is that in the object we encapsulate the method and properties together.

## [7] When to use Inheritance

* Don't use inheritance in the small programs.
* Notice that inheritance is not the only solution to enable code reuse. There is another technique called composition.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\35.PNG)

* Notice that when we have a new object Goldfish then our hierarchy is broken here because goldfish cannot walk. 
* To solve this problem we should change the hierarchy.

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\36.PNG)

* Now the hierarchy is more complex and it will become more and more complex if we many animals. 
* Hence **Avoid Creating Inheritance hierarchies**. Keep the inheritance hierarchies only till one level.
*  Favor Composition over inheritance.
* Instead of using inheritance we can define various features for our animals as independent objects. 
* Hence we can have 3 objects as shown with certain properties and methods.
* Now we can have person object and compose it from canWalk and canEat.
* Also we can have Goldfish object composed of canEat and canSwim

![](C:\Users\1000249643\Desktop\Programming Langauages\JavaScript Mosh Hamedani Udemy\Part 2 OOP\Images\37.PNG)

* Hence we can create any number of objects with different composition.
* In JS we use Mixins to achieve the composition.
* Study the code below 

```javascript
const canEat = {
  eat: function() {
    console.log('eating');
  }
};

const canWalk = {
  walk: function() {
    console.log('walking');
  }
}

function canSwim = {
  swim: function() {
    console.log('swim');
  }
}

// creating objects in the instance
// const person = Object.assign({}, canEat, canWalk);
// console.log(person);

// We can also use the constructor for this technique

function Person() {

}

// creating objects in the prototypes
Object.assign(Person, canEat, canWalk);
// here we modified the prototype of the person and added the capabilities to eat and walk
// hence now if we create person object then that person will have this capabilities.
const person = new Person();

function Goldfish() {

}

Object.assign(Goldfish.prototype, canEat, canSwim);

const goldfish = new Goldfish();
console.log(goldfish);
```

* To make this code more readable we can make a function for the `Object.assign` line

## [10] Exercise 1

```javascript
function HtmlElement() {
  this.click = function () {
    console.log('clicked');
  }
}

HtmlElement.prototype.focus = function() {
  console.log('focused');
}


HtmlSelectElement.prototype = new HtmlElement;
// 
function HtmlSelectElement(...items) {
  this.items = items;

  this.addItem = function(item) {
    this.items.push(item);
  }

  this.removeItem = function() {
    this.items.pop();
  }
}
```

* Notice that earlier in this section we use `HtmlSelectElement.prototype = Object.create(HtmlElement.prototype);`
* This approach will not work here because baseHtmlElement here only has one method `focus()` but not other method `clicked()`

