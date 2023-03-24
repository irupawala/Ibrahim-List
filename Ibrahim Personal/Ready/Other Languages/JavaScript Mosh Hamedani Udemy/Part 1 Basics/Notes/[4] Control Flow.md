## [1] If-else

```javascript
if (condition) {
    statement;
}
else if (anotherCondition) {
    statement;
}
else {
    statement;
}
```

## [2] Switch...case

* The case can be string or integer.

```javascript
let role;

switch (role) {
    case 'guest' :
        console.log('Guest User');
        break;

    case 'moderator':
        console.log('Moderator User');
        break;

    default:
        console.log('Unknown User')
}
```

## [3] For 

We have these loops in JS:

* For
* While
* Do...while
* For...in
* For...of

```javascript
for (let i=0; i < 5; i++) {
    console.log('Hello World', i);
}
```

## [4] While

```javascript
let i = 0;
while (i<=5) {
    if (i%2 !== 0) console.log(i);
    i++;
}
```

## [5] Do...while

```javascript
let i = 0;
do{
    if(i%2 !== 0) console.log(i);
    i++;
} while(i <= 5);
```

## [7] For...in

```javascript
name = 'Ibrahim';

for (let i in name){
    console.log(name[i]);
};

const person = {
    name: 'Mosh',
    age: 30
};

for (let key in person)
    console.log(key, person[key]);
```

## [8] For..of

* Ideal way of iterating over arrays

```javascript
const colors = ['red', 'green', 'blue'];

for (let index in colors)
    console.log(index, colors[index]);


// for - of
for (let color of colors)
    console.log(color);
```

## [9] Break and Continue

Break - Jump out of a loop

Continue - Jump out of an iteration

```javascript
let i = 0;
while(i <= 10) {
   // if (i === 5) break;
   if (i%2 === 0) {
       i++;
       continue;
   }
    console.log(i);
    i++;
}
```

## [10] Exercise - Max of Two Numbers

```javascript
let number = max(5,10);
console.log(number);

function max(a,b) {
    return (a > b) ? a : b;
}
```

## [11] Exercise - Landscape or Portrait

```javascript
// If portrait then return true

function isLandscape(width, height) {

    return (height > width);
}

console.log(isLandscape (2, 3));
```

## [12] Exercise - FizzBuzz

```javascript
const output = fizzBuzz(15);
console.log(output);


function fizzBuzz(input){
    if(typeof(input) !== 'number')
    return NaN;

    if(input % 15 == 0)
    return "fizzBuzz";

    if(input % 5 == 0)
    return 'Buzz';

    if(input % 3 == 0)
    return 'Fizz';

    return input 
}
```

## [13] Exercise - Demerit Points

```javascript
console.log(checkSpeed(130));

function checkSpeed (speed) {
    const speedLimit = 70;
    kmPerPoint = 5;
    const speedAboveLimit = speed - speedLimit;
    const licenseSuspendLimit = 180 + kmPerPoint;
    const licenseSuspendPoint = (licenseSuspendLimit - speedLimit)/ 5;
    let points = 0;
    if (speed >= speedLimit) {
        for (let i = 0; i <= speedAboveLimit; i+=5) {
            points++;
        }
    }

    if (points >= licenseSuspendPoint)
        return "License Suspended";
    if (points > 0)
        return points;
        return 'OK';
}
```

Code By Mosh

```javascript
checkSpeed (130);

function checkSpeed(speed) {
    const speedLimit = 70;
    const kmPerPoint = 5;

    if (speed < speedLimit + kmPerPoint) {
        console.log('OK');
        return;
    }

    const points = Math.floor((speed - speedLimit) / kmPerPoint) 
    if (points >= 12)
        console.log('License Suspended');
    else
        console.log('Points', points);
}
```

## [14] Exercise - Even and Odd

```javascript
showNumber(10);

function showNumber(limit) {
    for (let i=0; i <= limit; i++) {
        const message = (i%2 === 0) ? 'EVEN' : 'ODD'
        console.log(i, message);
    }
}
```

## [15] Exercise - Count Truthy

```javascript
const array = [0, null, undefined, '', 2, 3, 4];

console.log(countTruthy(array));

function countTruthy(array) {
    let count = 0;
    for (let value of array)
        //if (value !== false || value !== undefined) // note here that we have not written the statement above
        // if the argument in if statement is not boolean the JS engine trys to evaluate it as truthy or falsy
        // If the result is truthy count will be incremented
        if (value)  
        count++;
    return count;

}
```

## [16] Exercise - String Properties

```javascript
const movie = {
    title: 'a',
    releaseYear: 2018,
    rating: 4.5,
    director: 'b'
};

showProperties(movie);

function showProperties (movie) {
    for (let key in movie) {
        if (typeof(movie[key]) === 'string')
        console.log(key + ':',movie[key]);
    }
}

```

## [17] Exercise - Sum of Multiples of 3 and 5

```javascript
function sum (limit){
    let sum = 0;   

    for (let i = 0; i<=limit; i++)
        if ((i % 3 === 0) || (i % 5 === 0))
            sum+=i;
    
    return sum;
}

console.log(sum (10));
```

## [18] Exercise - Grade

```javascript
function calculateGrade(marks) {
    const average = calculateAverage(marks);
    if (average < 60) return 'F';
    if (average < 70) return 'D';
    if (average < 80) return 'C';
    if (average < 90) return 'B';
    return 'A';
}

function calculateAverage(array) {
    let sum = 0;
    for (let value of array)
        sum += value;
    return sum / array.length;
}

const marks = [90, 90, 95]

console.log(calculateGrade(marks));
```

## [19] Exercise - Stars

```javascript
function showStars(rows){
    for (let row = 1; row <= rows; row++) {
        let pattern = '';
        for (let j = 0; j < row; j++) 
            pattern += '*';
    console.log(pattern);
    }
}

showStars(3);
```

## [20] Exercise - Prime Numbers

```javascript
function showPrimes(limit) {
    primeNumbers = [2];
    for (let no = 3; no <= limit; no++) {
    flag = true;
        for (let prime = 0; prime < primeNumbers.length; prime++)
            if (no%primeNumbers[prime] === 0) 
                flag = false;
                
    if (flag)
        primeNumbers.push(no);
    }

    //console.log(primeNumbers);
    displayPrime(primeNumbers);
            
}

function displayPrime (array) {
    for (let value of array)
        console.log(value)
}

showPrimes(100);
```

**Mosh Code**

```javascript
function showPrimes(limit) {
    for (let number = 2; number <= limit; number++)
        if(isPrime(number)) console.log(number);
}

function isPrime(number) {
    for (let factor = 2; factor < number; factor++)
        if (number % factor === 0)
            return false;

    return true;
}

showPrimes(100);
```



