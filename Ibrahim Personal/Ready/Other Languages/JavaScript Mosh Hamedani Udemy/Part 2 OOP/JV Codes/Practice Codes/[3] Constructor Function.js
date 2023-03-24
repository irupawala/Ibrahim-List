function Ibrahim (age, sex, last_name) {
    this.age = age,
    this.sex = sex,
    this.last_name = last_name,
    this.message = function(){
        "Ibrahim is still great"
    }
}

const Old_Ibrahim = new Ibrahim (40, "Male", "Rupawala");

console.log(Old_Ibrahim.age);
