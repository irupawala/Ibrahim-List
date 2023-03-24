function Ibrahim (Age) {

    return {
        Age,
        message()
        {
            console.log("Ibrahim is great");
        },
        Sex: "Male"

            }
}

const Young_Ibrahim = Ibrahim(23);

console.log(Young_Ibrahim.Age);
console.log(Young_Ibrahim.Sex);

