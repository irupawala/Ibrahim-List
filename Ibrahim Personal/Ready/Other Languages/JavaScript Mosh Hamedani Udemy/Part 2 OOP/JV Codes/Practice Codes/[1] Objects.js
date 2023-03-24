const my_object = {
    name: "Ibrahim",
    Age: 28,
    Sex: "Male",
    message: function() {
        console.log("Ibrahim is great");
    }
}

// Calling members and functions
// console.log(my_object.Sex);
// my_object.message();

// Adding member functions
my_object.last_name = "Rupawala";
// console.log(my_object.last_name);

// Deleting member functions
delete my_object.Age;


// Iterating using for-in
for (key in my_object) {
    //console.log(key, ": ", my_object[key]);
}

// Iterating using for-of
// Object.keys returns all the keys
for (let key of Object.keys(my_object)) {
   // console.log(key);
}


// Iterating using for-of
// Object.entries returns all the key-value pairs

for (let entries of Object.entries(my_object)) {
    // console.log(entries);
}

// Iterating using in operator
if ('name' in my_object) {
    // console.log('yes');
}

// Cloning an object using for-in

const clone = {};

for (let key in my_object) {
    clone[key] = my_object[key];
}

for (let key in clone) {
   // console.log(key, ":", clone[key]);
}

// Cloning an object using spread operator

clone_1 = {...my_object};

for (let key in clone_1) {
   // console.log(key, ":", clone_1[key]);
}

// Cloning an Object using assign method

const clone_2 = Object.assign(my_object, {}, {Company : "SanDisk"});

for (let key in clone_2) {
    // console.log(key, ":", clone_2[key]);
 }
 