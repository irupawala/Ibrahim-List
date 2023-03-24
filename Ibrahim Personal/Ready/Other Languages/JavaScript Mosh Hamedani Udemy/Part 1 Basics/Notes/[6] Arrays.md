## [2] Adding elements

* **When you define array as constant then you cannot reassign the array but you obviously can add or remove elements from this array.**
* Elements can be added by
  * Push - end
  * Unshift - beginning
  * Splice - middle

```javascript
const numbers = [3, 4];

// End
numbers.push(5, 6);

// Beginning
numbers.unshift(1, 2);

// Middle
numbers.splice(2, 0, 'a', 'b'); // index, delete_count, values to be added.

console.log(numbers);
```

## [3] Finding Elements (Primitives)

* Finding depends on whether we are storing primitives or reference types

### 1. IndexOf 

* If the number exists in the array the output will be 0 or else the output will be -1.

* Also notice that **type of the variable given in indexOf method matters**.

```javascript
const numbers = [1, 2, 3, 4]

console.log(numbers.indexOf(1)); 
console.log(numbers.indexOf('1'));
console.log(numbers.indexOf('a'));
```

### 2. lastIndexOf 

*  Gives the index of the last occurrence of a number.

```javascript
const numbers = [1, 2, 3, 1, 4]

console.log(numbers.lastIndexOf(1)); 
```

### 3. includes Method

To check whether a given element exists in an array or not we can compare the output with -1 or 0 but the more cleaner way is .includes

```javascript
const numbers = [1, 2, 3, 1, 4];
console.log(numbers.indexOf(1) !== -1);
console.log(numbers.includes(1));
```

**Optional starting Index**

Note that all these parameters also consists an optional argument of starting index. It is from this starting index the search of an element will begin.

```javascript
const numbers = [1, 2, 3, 1, 4];

console.log(numbers.indexOf(1, 2)); \\ no_to_search, starting_index
```

## [4] Finding Elements (Reference Types)

* While dealing with objects includes method won't work, this is because when we check references for equality then their reference that is the place at which it is stored is checked.

```javascript
const courses = [
    {id: 1, name: 'a'},
    {id: 2, name: 'b'}
];

console.log(courses.includes({id: 1, name: 'a'}));
```

### 1. find method

* **When you have array with reference type you have to use find method.**
* To use the find method you have to pass function as an argument to the find method. This function is called a **predicate** because we use it to find if the condition is met or not. In this function we have to return  a boolean.
* This function (predicate) takes a parameter which is **element of an array.**
* This function will take each element of an array one by one. If the condition is **not met (that is if the match is not found) the result returned will be false and hence the search will continue.**
* If the condition **is met the element will be returned and the search will stop.**
* If there is no element in the array that matches the criteria. we'll get **undefined.**
* **Hence the find method returns the first element which matches the criteria.**

```javascript
const courses = [
    {id: 1, name: 'a'},
    {id: 2, name: 'b'}
];

//console.log(courses.includes({id: 1, name: 'a'}));

const course = courses.find(function(element)
{
    return element.name === 'a';
    //return element.name === 'xyz';
});

console.log(course);
```

### 2. findIndex

* This will return the index of the element which matches the criteria.
* If there is no match -1 will be returned.

```javascript
const courses = [
    {id: 1, name: 'a'},
    {id: 2, name: 'b'}
];

//console.log(courses.includes({id: 1, name: 'a'}));

const course = courses.findIndex(function(element)
{
    return element.name === 'a';
    //return element.name === 'xyz';
});

console.log(course);
```

## [5] Arrow Functions

* Instead of writing predicate function as seen in the code above from ES6 there is a cleaner way to write the same function using ES6.

* Arrow functions are used whenever you want to pass a function as a callback function or as an argument for different method.

```javascript
const courses = [
    {id: 1, name: 'a'},
    {id: 2, name: 'b'}
];

const course =  courses.find ( (element) => {

    return ((element.name === 'a'));
});

console.log(course);
```

Ways to make  cleaner code:

```javascript
const courses = [
    {id: 1, name: 'a'},
    {id: 2, name: 'b'}
];

/*
// Now if the function has no parameters then we have to pass empty parameters
const course =  courses.find ( () => {

    return ((element.name === 'a'));
});

// Now if the function has a single parameter you can also get rid of parantheses
const course =  courses.find ( element => {

    return ((element.name === 'a'));
});
*/

// and finally if there is only one line of code then we can also get rid of the return statement and {} braces

const course = courses.find(element => element.name === 'a');

console.log(course);
```

## [6] Removing elements

Elements can be deleted by

- Pop- end
- Shift - beginning
- Splice - middle

```javascript
// End
const numbers = [1, 2, 3, 4];
const last = numbers.pop();

console.log(last);
console.log(numbers);

// Beginning

const pumbers = [1, 2, 3, 4];
const first = pumbers.shift();

console.log(first);
console.log(pumbers);

// Middle

const mumbers = [1, 2, 3, 4];
const middle = mumbers.splice(2, 2); // index, delete_count, values to be added.

console.log(middle);
console.log(mumbers);
```

## [7] Emptying an Array

* Before this topic please notice that array is an object and objects are of reference type hence variables will store the memory location where the objects are stored.
* When we are emptying an array it means that we are assigning it a new array itself that is empty array. Hence we cannot assign this array as constant.
* Consider the scenario: 

```javascript
let numbers = [1, 2, 3, 4];
let another = numbers;
```

### Solution 1:

* **Works when there are no references to the original array**
* Simply reassign it to a new array

```javascript
numbers = [];

console.log(numbers);
console.log(another);
```

* If there are no references to the original memory eventually it will be removed by the garbage collector.
* if we have another reference like this "let another = numbers;" then it won't be removed by garbage collector because **IT IS POINTING THE SAME OBJECT HENCE STORING THE SAME MEMORY LOCATION.**
* When numbers is assigned new empty array it is now pointing to the new address where this empty array is stored but another is still storing the address of the original array.

### Solution 2:

* Used when there are multiple references to the original array.
* Simply make the length of an array to 0, this will truncate the array.

```javascript
numbers.length = 0;

console.log(numbers);
console.log(another);
```

* Here when we make the length 0 then both the numbers and pointers will display the empty array as an output because eventually both are storing the same address of the same object.

### Solution 3:

* Splice all the elements of an array

```javascript
numbers.splice(0, numbers.length);

console.log(numbers);
console.log(another);
```

### Solution 4:

* pop all the elements of an array.

```javascript
while (numbers.length > 0)
    numbers.pop();

console.log(numbers);
console.log(another);
```

* Very performance exhaustive.

## [8] Combining and Slicing Arrays

### 1. Concat - Combining arrays

```javascript
const first = [1, 2, 3];
const second = [4, 5, 6];

const combined = first.concat(second);
console.log(combined);
```

### 2. Slice - Slicing arrays

array_name.slice(start_index, end_index-1);

```javascript
const first = [1, 2, 3];
const second = [4, 5, 6];

const combined = first.concat(second);
console.log(combined);

// const slice = combined.slice(2, 4);
// console.log(slice);

const slice = combined.slice(2, );
console.log(slice);

// const slice = combined.slice();
// console.log(slice);
```

### Copying by value Vs copying by reference

* **Notice that when there are values/ primitives in the arrays then values are copied in the target array but when you are copying the objects, references are copied in the target array.**
* This means that the elements in both the input and output arrays are pointing to the same object.

```javascript
const first = [{id: 1}];
const second = [4, 5, 6];

const combined = first.concat(second);
first[0].id = 10; // changing the value of the object in first array


const slice = combined.slice(); 
console.log(combined); // The result in the combined array will also get changed as the objects are copied by reference
console.log(slice);
```

## [9] The Spread Operator

* To combine arrays. More cleaner then concat
* Gives more flexibility to add different elements in the middle of two arrays then combine method.

```javascript
const first = [1, 2, 3];
const second = [4, 5, 6];

const combined = [...first, ...second];
const combined = [...first, 'a', ...second, 'b'];

//copying the array
const slice = [...combined];
```

## [10] Iterating an Array

3 Ways

1. For - in loop (Displays Index)
2. For - of loop
3. forEach (Displays Index)

```javascript
const numbers = [1,2,3];

for (number in numbers)
    console.log(number, numbers[number]);
```

```javascript
const numbers = [1,2,3];

for (let number of numbers)
    console.log(number);
```

```javascript
const numbers = [1,2,3];

numbers.forEach(function(number) {
    console.log(number);
});

numbers.forEach(number => console.log(number));
```

```javascript
const numbers = [1,2,3];

numbers.forEach((number, index) => console.log(number));
```

## [11] Joining Arrays

```javascript
const numbers = [1, 2, 3];
const joined = numbers.join(",");


console.log(joined);

const message = 'This is my first message';
const parts = message.split(' ');
console.log(parts);

const combined = parts.join('-');
console.log(combined);
```

## [12] Sorting Arrays

Sorting primitives in arrays:

```javascript
const numbers = [2, 3, 1];

numbers.sort();
console.log(numbers);

numbers.reverse();
console.log(numbers);
```

Sorting references in arrays:

* Split method optionally takes an argument and that's a function that is used for comparison.

```javascript
// here we want JavaScript to come first that is to sort in alphanetical order.
// As we are comaring the alphabetical orders of the strings the comparison will happen based on ASCII code of the first letter.
// hence we have to remove the case-sensivity of the strings first so that results are not clitched

const courses = [
    {id: 1, name: 'Node.js'},
    {id: 2, name: 'JavaScript'},
];

courses.sort(function(a, b) {
    // a < b => -1
    // a > b => 1
    // a == b => 0

    const nameA = a.name.toUpperCase();
    const nameB = b.name.toUpperCase();

    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
    return 0;
});

console.log(courses);
```

```javascript
// here we want JavaScript to come first that is to sort in alphanetical order.

const courses = [
    {id: 1, name: 10},
    {id: 2, name: 5},
];

courses.sort(function(a, b) {
    // a < b => -1
    // a > b => 1
    // a == b => 0

   // const nameA = a.name.toUpperCase();
   // const nameB = b.name.toUpperCase();
   const nameA = a.name;
   const nameB = b.name;

    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
    return 0;
});

console.log(courses);
```

## [13] Testing elements of an Array

### 1. Every Method

* Returns true if all the elements of an array fulfill the condition.

* As soon as the condition is not met the function will not be checked for further elements it will return false and the process will be terminated.

```
const numbers = [1, 2, 3];

const AllPositive = numbers.every(function(value) {
    return (value > 0);
});

console.log(AllPositive);
```

### 2. Some Method

* Returns True if atleast one element in the array fulfills the condition.
* As soon as an element satisfies the condition it will return true and won't check further.

```javascript
const numbers = [-1, -2, 3];

const alteaseOnePositive = numbers.some(function(value) {
    return (value > 0);
});

console.log(alteaseOnePositive);
```

## [14] Filtering an Array

* Returns the new filtered array.

* Same as the every and some method but will continue the search and will return all the elements of an array which matches the criteria.
* Note that whenever you observe the callbackfn in the suggested parameters of the visual studio notice that this callbackfn can take 3 arguments 1. value 2. index 3. array

```javascript
const numbers = [1, -1, -2, 3];

// const filtered = numbers. filter(function(value) {

//     return (value >= 0);
// });

const filtered = numbers. filter(value => value >= 0);
console.log(filtered);
```

## [15] Mapping an Array

* Returns the new mapped array

```javascript
const numbers = [1, -1, 2, 3];

const filtered = numbers. filter(value => value >= 0);

const items = filtered.map(n => '<li>' + n + '<li>');

const html = '<ul>' + items.join(' ') + '<ul>';

console.log(html);
```

You can also map the elements to an object the same way you have mapped the elements to a string as shown above.

```javascript
const numbers = [1, -1, 2, 3];

const filtered = numbers. filter(value => value >= 0);

const items = filtered.map(n => {
    const obj = { value: n}; // here we mapped each item to value property
    return obj;
});


console.log(items);
```

* As we know we can convert it to a single line of code

```javascript
const numbers = [1, -1, 2, 3];

const filtered = numbers. filter(value => value >= 0);

const items = filtered.map(n => {value: n});

console.log(items);
```

* But the results displayed here will be undefined. The reason is {} braces are used by the callbackfn to represent code blocks hence as soon as JS sees {} it thinks of it as a code block but we are using {} braces here to represent object. hence to avoid this scenario if we meant to represent object we have to enclose the object inside the () braces like this ({Object}).

```javascript
const numbers = [1, -1, 2, 3];

const filtered = numbers. filter(value => value >= 0);

const items = filtered.map(n => ({value: n}));

console.log(items);
```

Also all these methods can be chained

```javascript
const numbers = [1, -1, 2, 3];

const items = numbers
    .filter(value => value >= 0)
    .map(n => ({value: n}))
    .filter(obj => obj.value > 1)
    .map(obj => obj.value);


console.log(items);
```

## [16] Reducing an Array

* Reduce method is used to reduce all the elements of entire arrays into a single value. This single value can be a number, string, object, or anything else.

```javascript
const numbers = [1, -1, 2, 3];

let sum = 0;

for (let n of numbers)
    sum += n;

console.log(sum);
```

* There is a more elegant way to solve this problem and that is to use reduce method.
* Reduce method takes in two arguments first: callback function and second: the initial value of an accumulator.

```javascript
const numbers = [1, -1, 2, 3];


const sum = numbers.reduce((accumulator, currentValue) => { // accumulator is like sum=0, currentValue is each element of array
    return accumulator + currentValue // internally this reduce method will store the result in accumulator
}, 0);

//This is same as 

//const sum = numbers.reduce(function(accumulator,currentValue){
//    return (accumulator + currentValue);
//}, 0)

console.log(sum);
```

* Notice that if we don't initialize the accumulator it will take the first element of the array as the initial value and the **currentValue will be assigned second element of an array.**

```javascript
const numbers = [1, -1, 2, 3];


const sum = numbers.reduce((accumulator, currentValue) => { // accumulator is like sum=0, currentValue is each element of array
    return accumulator + currentValue // internally this reduce method will store the result in accumulator
});

console.log(sum);
```

* Reducing the code complexity

```javascript
const numbers = [1, -1, 2, 3];


const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue) ;

console.log(sum);
```

## [17] Exercise 1 - Array from Range

```javascript
const numbers = arrayFromRange(-4,-4);

console.log(numbers);

function arrayFromRange(min, max) {

    let my_array = [];
    while(min <= max)
    {
        my_array.push(min);
        min += 1;
    }
    
    return (my_array);
}
```

## [18] Exercise 2 - Includes

```javascript
const numbers = [1, 2, 3, 4];

console.log(includes(numbers, -4));


function includes(numbers, searchElement)
{
    for (let element of numbers)
    {
        if (element === searchElement)
            return true;
    }

    return false;
}
```

## [19] Exercise 3 - Except

```javascript
const numbers = [1, 2, 3, 4];

const output = move(numbers, 3, -3);

console.log(output);

function move(array, index, offset) {
    const position = index + offset;
    if (position >= array.length || position < 0) {
        console.error('Invalid offset.');
        return;
    }

    const output = [...array];
    const element = output.splice(index, 1)[0];
    console.log(element);
    console.log(output);
    output.splice(position, 0, element);
    return output;

}
```



## [20] Exercise 4 - Move Elements

```javascript
const numbers = [1, 2, 3, 4];

console.log(move(numbers, 3, -4));

function move(numbers, index,  offset) {

    const position = index + offset ;

    if (position > (numbers.length-1)  || (position) < 0) 
        return ('Invalid offset');

     deleted_num = numbers.splice(index, 1).pop();
     numbers.splice(position, 0, deleted_num);
     return numbers;
    
}
```

## [21] Exercise 5 - Count Occurrences	

```javascript
const numbers = [1, 2, 3, 4, 5, 1, 1];

const count = countOccurences(numbers, 3)

console.log(count);

function countOccurences(array, searchElement) {
    let occurence = 0;
    for(let arrayElement of array)
        if(arrayElement === searchElement) {
            occurence += 1;
        }

        return occurence;
}
```

**Same Implementation using reduce function**

```javascript
const numbers = [1, 2, 3, 4, 5, 1, 1];

const count = countOccurences(numbers, 1)

console.log(count);

function countOccurences(array, searchElement) {

return array.reduce((accumulator, currentValue) => {
    const occurence = (currentValue === searchElement) ? 1 : 0
    console.log(accumulator, occurence, currentValue, searchElement);
    return occurence + accumulator;
    
}, 0);
}
```

## [22] Exercise 6 - Get Max

```javascript
const numbers = [-1, -2, -3, -4];

const max = getMax(numbers);

//console.log(Array.isArray(numbers));

console.log(max);

function getMax(array) {

    if (array.length === 0 || !(Array.isArray(array))) return undefined;

    let Max = array[0];
    for (let item of array)
        if(item > Max)
            Max = item;

    return Max;
}
```

**Same Implementation using reduce function**

```javascript
const numbers = [-1, -2, -3, -4, -5];

const max = getMax(numbers);

console.log(max);

function getMax(array) {

    if (array.length === 0 || !(Array.isArray(array))) return undefined;


   return array.reduce((accumulator, currentValue) => {
        if(accumulator < currentValue)
            accumulator = currentValue;

        return accumulator;
        
    });

}
```

**Implementation by Mosh**

```javascript
const numbers = [-1, -2, -3, -4, -5];

const max = getMax(numbers);

console.log(max);

function getMax(array) {

    if (array.length === 0 || !(Array.isArray(array))) return undefined;

   return array.reduce((a, b) => (a > b) ? a : b);

}
```

## [23] Exercise 7 - Movies

* Notice that sort function return a negative, zero, or positive value, depending on the arguments.
* function(a, b){return a-b}
* https://www.w3schools.com/jsref/jsref_sort.asp
* When the sort() method compares two values, it sends the values to the compare function, and sorts the values according to the returned (negative, zero, positive) value.

```javascript
const movies = [
    { title: 'a', year: 2018, rating: 4.5},
    { title: 'b', year: 2018, rating: 4.7},
    { title: 'c', year: 2018, rating: 3},
    { title: 'd', year: 2017, rating: 4.5},
    { title: 'e', year: 2018, rating: 4.8},
    { title: 'f', year: 2018, rating: 4.9}

];

// All movies in 2018 with rating > 4
// Sort them by their rating 
// Descending order
// Pick their title and display it on the console.

console.log(movies.filter(m => m.year = 2018 && m.rating > 4)
.sort((a,b) => a.rating-b.rating)
.reverse()
.map(m => m.rating)
);
```

