package academy.learnprogramming;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {


//        System.out.printf("byte minimum = %s, maximum = %s%n", Byte.MIN_VALUE, Byte.MAX_VALUE);
//        System.out.printf("short minimum = %s, maximum = %s%n", Short.MIN_VALUE, Short.MAX_VALUE);
//
//        System.out.printf("int minimum = %s, maximum = %s%n", Integer.MIN_VALUE, Integer.MAX_VALUE);
//        System.out.printf("long minimum = %s, maximum = %s%n", Long.MIN_VALUE, Long.MAX_VALUE);
//
//        System.out.printf("float minimum = %s, maximum = %s%n", Float.MIN_VALUE, Float.MAX_VALUE);
//        System.out.printf("double minimum = %s, maximum = %s%n", Double.MIN_VALUE, Double.MAX_VALUE);

       // A Java Double has 52 bits of precision while float has 23 bits of precision
        // A Double is 64 bits in size but 52 bits of that are significant.
        // Float is single precision while Double is a double precision number
        // Double has 15 to 16 bits of precision while float has only 7 bits of precision.

        float f = 123.4567890123456789f; // Note here the error is not because we have used more than 7 bits of precision
        // but because the default floating point number in Java is a Double. We can't assign a double value to a variable of type float.
        // To assign a literal value yo a float we have to assign f in the end just like C++
        double d = 123.4567890123456789;

        System.out.printf("f is %.99f %n", f); // This will give floating point rounding error and this happens because some decimal numbers cannot be
        // precisely stored in binary format
        System.out.printf("d is %.99f %n", d);


        System.out.println("f is " + f); // This will give 7 digits of precision
        System.out.println("d is " + d); // This will give 15 digits of precision

        BigDecimal z = new BigDecimal("123.456789012345678901234567890123456789"); // This will give 28 to 29 digits of precision, Also notice that
        // we have typed a string instead of a number because if we will type a floating point number then it will default to double and
        // we will lose the precision of the BigDecimal
        System.out.printf("z is %.99f %n", z);

        // Note the precision is much better. Also the accuracy of numerical calculations is much better with big decimal.
        // The BigDecimal class provides methods for mathematical operations and you can't use operators like + and - which
        // you can use with the float and double

    }
}
