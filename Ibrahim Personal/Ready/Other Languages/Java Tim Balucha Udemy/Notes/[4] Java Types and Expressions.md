# [4.38] Primitive Types

Check out the link:

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html

* Strings are immutable. They can't be changed. When they appear to change a new string is created in memory
* Byte cab store a value from -128 and 127.
* This example demonstrates the use of MIN_VALUE and MAX_VALUE to find the min and max of any datatype.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here

        System.out.printf("byte minimum = %s, maximum = %s%n", Byte.MIN_VALUE, Byte.MAX_VALUE);
        System.out.printf("short minimum = %s, maximum = %s%n", Short.MIN_VALUE, Short.MAX_VALUE);
        // Here Byte with capital B is a wrapper object and not a primitive datatype.
        // Bytes is used where memory is an issue and in embedded applications
        // Bytes are to be used because many data streams are streams of bytes. So if we're processing a JPEG image, for example, 
        // you'd be reading bytes from the JPEG file in JAVA.
        // Don't use bytes if you are dealing with numbers. Think of bytes as eight bits and only use bytes if what you are dealing with
        // something that is 8 bits like color in the bitmap or pixel on the screen

    }
}
```

# [4.39] Int and Long

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here

        System.out.printf("int minimum = %s, maximum = %s%n", Integer.MIN_VALUE, Integer.MAX_VALUE);
        System.out.printf("long minimum = %s, maximum = %s%n", Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
```

# [4.40] Float and Double

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        System.out.printf("float minimum = %s, maximum = %s%n", Float.MIN_VALUE, Float.MAX_VALUE);
        System.out.printf("double minimum = %s, maximum = %s%n", Double.MIN_VALUE, Double.MAX_VALUE);
        
       // A Java Double has 52 bits of precision while float has 23 bits of precision
        // A Double is 64 bits in size but 52 bits of that are significant.
        // Float is single precision while Double is a double precision number
        // Double has 15 to 16 bits of precision while float has only 7 bits of precision.

    }
}
```

# [4.41] Float and Double Precision

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
        
        
        System.out.printf("float minimum = %s, maximum = %s%n", Float.MIN_VALUE, Float.MAX_VALUE);
        System.out.printf("double minimum = %s, maximum = %s%n", Double.MIN_VALUE, Double.MAX_VALUE);

       // A Java Double has 52 bits of precision while float has 23 bits of precision
       // A Double is 64 bits in size but 52 bits of that are significant.
       // Float is single precision while Double is a double precision number
       // Double has 15 to 16 bits of precision while float has only 7 bits of precision.

        float f = 123.4567890123456789f; // Note here the error is not because we have used more than 7 bits of precision but because the default floating point number in Java is a Double. We can't assign a double value to a variable of type float.To assign a literal value yo a float we have to assign f in the end just like C++.
        double d = 123.4567890123456789;

        System.out.printf("f is %.99f %n", f); // This will give floating point rounding error and this happens because some decimal numbers cannot be precisely stored in binary format
        System.out.printf("d is %.99f %n", d);
        
        
        System.out.println("f is " + f); // This will give 7 digits of precision
        System.out.println("d is " + d); // This will give 15 digits of precision

    }
}

```

# [4.42] BigDecimal and Floating Point Accuracy

```java
package academy.learnprogramming;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {

        float f = 123.4567890123456789f; // Note here the error is not because we have used more than 7 bits of precision but because the default floating point number in Java is a Double. We can't assign a double value to a variable of type float. To assign a literal value to a float we have to assign f in the end just like C++
        double d = 123.4567890123456789;

        System.out.printf("f is %.99f %n", f); // This will give floating point rounding error and this happens because some decimal numbers cannot be precisely stored in binary format
        System.out.printf("d is %.99f %n", d);


        System.out.println("f is " + f); // This will give 7 digits of precision
        System.out.println("d is " + d); // This will give 15 digits of precision

        BigDecimal z = new BigDecimal("123.456789012345678901234567890123456789"); // This will give 28 to 29 digits of precision, Also notice that we have typed a string instead of a number because if we will type a floating point number then it will default to double and we will lose the precision of the BigDecimal
        System.out.printf("z is %.99f %n", z);

        // Note the precision is much better. Also the accuracy of numerical calculations is much better with big decimal. The BigDecimal class provides methods for mathematical operations and you can't use operators like + and - which you can use with the float and double

    }
}

```

# [4.43] BigDecimal Accuracy

- **Notice that floating point arithmetic isn't completely accurate.**
- **BigDecimal Datatypes solves most of the problems associated with rounding.**

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here

        double result1 = 0.1 * 8;
        double result2 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1;

        System.out.printf("result1 is %.99f %n", result1);
        System.out.printf("result2 is %.99f %n", result2);

        double difference = result1- result2;
        System.out.printf("The difference is %.99f %n", difference);

        // The reason for this error is because some numbers cannot be exactly represented in binary format.
        // The same is also true for BigDecimal.
        // The common example in double is 1/3 where the fraction 1/3 is exact but the decimal representation is 0.3333... is a recurring fraction. The decimal representation is close to 1/3 but it can't represent it exactly
        // The double value 0.1 is a recurring fraction in binary. The binary representation is very close to 1/10 but it isn't exact.
        // Also as you perform more operation with that slightly inaccurate value like in result2 the error becomes more and more evident. result2 is slightly more inaccurate as compared to result1 above.
    }
}

```

* **BigDeimal is immutable** - meaning its value can't be changed once it's been set.
* We don't use BigDecimal all the time as performing arithmetic on BigDecimal numbers is very much (20 times) slower than using doubles or floats

# [4.44] Expressions

```java
package academy.learnprogramming;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {
	// write your code here

        double result1 = 0.1 * 8;
        double result2 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1;

        System.out.printf("result1 is %.99f %n", result1);	// Expression 1 
        System.out.printf("result2 is %.99f %n", result2);  // Expression 2

        double difference = result1- result2; // Expression 3
        System.out.printf("The difference is %.99f %n", difference); // Expression 4

    }
}

```

* Note here the obvious expression evident is `difference = result1 - result2` but the expressions at other places are less evident. but the result1 and result2 are evaluated first before getting assigned in Exp 1,2 and 3.
* Note that `double result1` and `double result2` declared first are not expressions but declaration. result1 and result2 doesn't have a value until that line has been executed.
* Also expression can't be put on the left hand side of an equal sign, only on the right hand side.
* E.g you can't write `result1 - result2 = 0;` the problem here is the left hand side of the assignment has to be a variable and not an expression. Notice here the problem is there is expression on both the sides of the assignment operator **and you can't assign something to an expression**
* **A literal is a constant value or a constant expression. 0 here is a numeric literal.** String is also a literal called as string literal.

# [4.45] Boolean Expressions

* When testing for equality in Java we have to use `==` sign. single `=` is used to assign values to variables.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int apples = 18;
        int oranges = 9;
        double applePrice = 12.60;
        double orangePrice = 4.50;

        System.out.println(apples == oranges);
        System.out.println(apples != oranges);

        System.out.printf("%d > %d is %s %n", apples, oranges, apples > oranges);
        System.out.printf("%d < %d is %s %n", apples, oranges, apples < oranges);
        System.out.printf("%d >= %d is %s %n", apples, oranges, apples >= oranges);
        System.out.printf("%d <= %d is %s %n", apples, oranges, apples <= oranges);

        System.out.printf("Reducing apple cost: %s %n", (apples > oranges) && (applePrice > orangePrice));
        System.out.printf("Reducing apple cost: %s %n", (apples > oranges) || (applePrice > orangePrice));
        System.out.printf("Reducing apple cost: %s %n", (apples < oranges) || (applePrice < orangePrice));

    }
}

```

# [4.48] Boolean Variables

* **Note that boolean variables true and false are typed in lowercase letter in java**

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int apples = 18;
        int oranges = 9;
        double applePrice = 12.60;
        double orangePrice = 4.50;

        boolean moreApples;
        boolean applesAreDearer;

        moreApples = (apples > oranges);
        applesAreDearer = (applePrice > orangePrice);
        System.out.printf("We have more apples: %s %n", moreApples);
        System.out.printf("Apples are dearer: %s %n", applesAreDearer);

        boolean moreApplesAndDearer = moreApples && applesAreDearer;
        boolean moreApplesOrDearer = moreApples || applesAreDearer;
        System.out.printf("Reducing cost of apples: %s %n", moreApplesAndDearer);
        System.out.printf("Reducing cost of apples: %s %n", moreApplesOrDearer);

    }
}

```

# [4.51] Classes and Objects

* **In Java all methods have to appear in a class unlike in C++ where methods can also be defined outside class.**
* **Also all the variables have to appear inside a class or a method of the class.**
* Methods have to be written with braces `.method_name()`

# [4.52] Classes and Class Instance

```java
package academy.learnprogramming;


public class Main {

    public static void main(String[] args) {

        // Instances of Car Class or objects of Type Car or variable of type Car

        // Instance of the Class is an object whose type is that defining class
        Car myCar = new Car();
        Car anotherCar = new Car();

        myCar.accelerate(); // Calling methods on these objects.
        anotherCar.brake();

        // With the primitive types, we could just assign values to them while declaring the variable.
        // But we can't do that with user-defined types such as our Car because we have to tell java to create instance of this class by using the new keyword.
        // Think of this as telling Java to create a new instance of the Car class and then assigning a reference to that instance to the myCar variable
    }
}



class Car { // Class, note that Car starts with capital as per java convention

    public void accelerate() { // Method, it starts with capital as per java convention
        System.out.println("You are going faster.");
    }

    public void brake() { // Method
        System.out.println("You are going slower.");
    }
}

```

# [4.53] Members and Fields

* Classes can have several different kinds of members. Methods are one of the members of the class.
* One another kind of member is called Field.
* Methods are members that perform actions whereas **fields are members that store state of values that represent some aspect of each class instance.**
* **Note that in JAVA var can never be used to declare a field. You have to specify the type explicitly.**
* Also notice that field is available in all the class methods. In our example we are going to use it in accelerate method and break method.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        Car myCar = new Car();
        Car anotherCar = new Car();

        myCar.accelerate(); // Calling methods on these objects.
        myCar.accelerate();
        myCar.accelerate();
        myCar.accelerate();

        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.accelerate();

        anotherCar.brake();

    }
}

class Car { // Class, note that Car starts with capital as per java convention

    private int speed = 0;

    public void accelerate() { // Method, note that  starts with capital as per java convention
        //System.out.println("You are going faster.");
        speed++;
        System.out.printf("You are going %d kilometers per hour. %n", speed);
    }

    public void brake() { // Method
        speed--;
        //System.out.println("You are going slower.");
        System.out.printf("You are going %d kilometers per hour. %n", speed);
    }
}
```

* Note that in the example above the speed value of myCar does not affect the speed value of anotherCar, **hence each instance of car has its own speed value.**

# [4.54] Class Constructor

* Car class has a field that we initialize to zero. There is another way to initialize class fields and that's to use constructor.
* Keep in mind that when we don't define a constructor, the Java compiler will create a basic, empty constructor also known as a default constructor. But when we create a constructor the Java compiler won't attempt to create one itself.
* Constructor is a method with the same name as the class but without any return type. So its really a special method for a class.
* **A constructor is a method that's called automatically when you create a new instance of a class.**

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here

        // Instances of Car Class or objects of Type Car or variable of type Car

        // Instance of the Class is an object whose type is that defining class
        Car myCar = new Car("Ibrahim's Car");
        Car anotherCar = new Car("Tim's Car");

        myCar.accelerate(); // Calling methods on these objects.
        myCar.accelerate();
        myCar.accelerate();
        myCar.accelerate();

        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.accelerate();

        anotherCar.brake();



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

    public void accelerate() { // Method, note that  starts with capital as per java convention
        //System.out.println("You are going faster.");
        speed++;
        System.out.printf("%s is going %d kilometers per hour. %n", name, speed);
    }

    public void brake() { // Method
        speed--;
        //System.out.println("You are going slower.");
        System.out.printf("%s is going %d kilometers per hour. %n",name, speed);
    }
}
```



# [4.55] Private and Public Members

* Private members aren't available for outside of the class they are declared in.
* In the example below showSpeed is made private. Accelerate and break can use it as they are the part of the class but it cannot be accessed outside the class.
* Also notice that how the private member showSpeed is used to remove the repetition of writing the code.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here

        // Instances of Car Class or objects of Type Car or variable of type Car

        // Instance of the Class is an object whose type is that defining class
        Car myCar = new Car("Ibrahim's Car");
        Car anotherCar = new Car("Tim's Car");

        myCar.accelerate(); // Calling methods on these objects.
        myCar.accelerate();
        myCar.accelerate();
        myCar.accelerate();

        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.brake();
        myCar.accelerate();

        anotherCar.brake();



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

    public void accelerate() { // Method, note that  starts with capital as per java convention
        //System.out.println("You are going faster.");
        speed++;
       // System.out.printf("%s is going %d kilometers per hour. %n", name, speed);
        showSpeed();
    }

    public void brake() { // Method
        speed--;
        //System.out.println("You are going slower.");
        //System.out.printf("%s is going %d kilometers per hour. %n",name, speed);
        showSpeed();
    }

    private void showSpeed()
    {
        System.out.printf("%s is going %d kilometers per hours. %n", name, speed);
    }

}
```









