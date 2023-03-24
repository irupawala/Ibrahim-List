package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
        // write your code here

        // Instances of Car Class or objects of Type Car or variable of type Car

        // Instance of the Class is an object whose type is that defining class
        Car myCar = new Car("Ibrahim's Car");
        Car anotherCar = new Car("Tim's Car");

        myCar.accelerate(1); // Calling methods on these objects.
        myCar.accelerate(3);
        myCar.accelerate(5);
        myCar.accelerate(6);

        myCar.brake(2);
        myCar.brake(3);
        myCar.brake(3);
        myCar.brake(5);
        myCar.accelerate(2);

        anotherCar.brake(1);


        // With the primitive types, we could just assign values to them while declaring the variable.
        // But we can't do that with user-defined types such as our Car because we have to tell java to create instance of this
        // class by using the new keyword.

        // Think of this as telling Java to create a new instance of the Car class and then assigning a reference to that
        // instance to the myCar variable
    }
}


class Car { // Class, note that Car starts with capital as per java convention

    private int speed = 0;
    private String name;

    public Car(String carName) {
        name = carName;
    }

    public void accelerate(int amount) { // Method, note that  starts with capital as per java convention
        //System.out.println("You are going faster.");
        speed += amount;
        // System.out.printf("%s is going %d kilometers per hour. %n", name, speed);
        showSpeed();
    }

    public void brake(int amount) { // Method
        speed -= amount;
        if (speed < 0) {
            System.out.println("Speed cannot be below 0");
        }else {
            showSpeed();
        }
        //System.out.println("You are going slower.");
        //System.out.printf("%s is going %d kilometers per hour. %n",name, speed);

    }

    private void showSpeed() {
        System.out.printf("%s is going %d kilometers per hours. %n", name, speed);
    }

}





