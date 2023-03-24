## [2] Arithmetic Operators

```javascript
let x = 10;
let y = 3;

console.log(x + y);
console.log(x - y);
console.log(x * y);
console.log(x / y);
console.log(x % y);
console.log(x ** y);

// Increment
console.log(++x); //pre-increment, 11 will be displayed on console 
console.log(x++); // post-increment, 10 will be displayed, incremented value will be seen in next call

// Decrement
console.log(--x);
console.log(x--);
```

## [3] Assignment Operator

```java
x +=5;
x *=3;
```

## [4] Comparison Operator

```javascript
let x = 1;

// Relational
console.log(x > 0);
console.log(x >= 1);
console.log(x < 0);
console.log(x <= 0);

// Equality
console.log(x === 1);
console.log(x !=== 1);
```

## [5] Equality Operators

### Strict Equality Vs Loose Equality

```javascript
// Strict Equality, Ensures equality of (Type + Value)

console.log(1 === 1);
console.log('1' === 1);

// Lose Equality
console.log(1 == 1);
console.log('1' == 1); // This operator looks at the value on the left side of equal and converts the operand on the right side to the same type and then checks if the value is equal

// hence this expression will be something like 

console.log('1' == '1');

// similarly
console.log(true == 1);
```

## [6] Ternary Operator

```javascript
let points = 110;
let type = points > 100 ? 'gold' : 'silver';
console.log(type);
```

## [7] Logical Operator with Booleans

```javascript
console.log(true && true);
console.log(true || false);
let applicationRefused = !eligibleForLoan;

```

## [8] Logical Operator with Non-Booleans

JavaScript allows to use logical operator with non-booleans

```javascript
false || 'Mosh'
false || 1
```

* The result is not necessarily true or false.
* Here the second operand is string hence we will get string back
* Also the second operand is number hence we will get the same 

* So when the JV engine looks at the expression and if the operands are not boolean it will try to evaluate the operand as **truthy or falsy**
* Falsy:
  * undefined
  * null 
  * 0
  * False
  * ' '
  * NaN
* Truthy
  * Anything that is not a false is truthy

```javascript
false || 'Mosh'
false || 1
```

In the example above JV will evaluate the first operand which is false and hence will move to second operand expecting for true or truthy. **As the second operand is truthy it will return that value**

### Short circuiting with truthy operands

```javascript
false || 1 || 2
```

* Here the result will be 1 as when the || operator finds truthy value it doesn't goes further

**Real World Example of Short Circuit**

```javascript
let userColor = 'red';
let defaultColor = 'blue';
let currentColor = userColor || defaultColor;

console.log(userColor || defaultColor);
```

```javascript
let userColor = undefined;
let defaultColor = 'blue';
let currentColor = userColor || defaultColor;

console.log(userColor || defaultColor);
```

## [9] Bitwise Operator

```javascript
console.log(1 | 2);
console.log(1 & 2);
```

