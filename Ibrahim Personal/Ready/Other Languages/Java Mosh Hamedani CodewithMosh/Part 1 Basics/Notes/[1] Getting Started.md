# 1. Getting Started

## [2] Anatomy of a Java Program

* Function:

A block of code that performs a task

```java
void sendEmail() {
    
}
```

* Main() function inside every java program is the entry point of program.
* Functions does not exist on their own they always belong to class.
* Class:
  * A container for related functions.
* Every Java program should have atleast one class that contains the main function that is **main class.**

```java
class Main {
    void main() {
        
    }
}
```

* Method:
  * Now as the function in Java always belong to the class we call it as a **method**. Method is a function that is a part of the class.
* Access Modifiers:
  * All these classes and methods should have access modifiers. These are the keywords which determine if other classes and methods can access these classes and methods.
  * E.g public, private

```java
public class Main {
    public void main() {
        
    }
}
```

* Naming convention:
  * Classes - Pascal Naming Convention
  * Methods - camel Naming Convention

* Package:
  * Package is the container to group related classes.
  * By convention the name of the package is the domain name of your company in reverse
* Sample Code from Intellij :

```javascript
package com.google;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("Hello World"); // System is a class defined in java.lang package
                              // out is a field of type PrintStream class
                              // println() is a method inside the PrintStream class
    }
}

```

* Notice that main method should always be static.
* Also notice that we are passing the parameter **String[] args** to this function.



## [3] How Java Code Gets Executed

 Two steps:

* Compilation
* Execution



* Compilation:
  * During compilation Java converts the Java source code in to Byte code.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\1.PNG)

* Java compiler comes with JDK downloaded.
* To generate Java Byte code we have to invoke java compiler. To do this type "javac Main.java" in terminal in IntelliJ and then look for the contents in the folder by typing "dir" in windows.
* Main.Class is the Byte Code.
* When we use IntelliJ this byte code is generated inside the ***out*** folder.
* This Main.Class file is **platform independent** meaning it can run on any OS which has Java Runtime Environment (JRE).
* This JRE has a software component called Java Virtual Machine (JVM). JVM takes Java Byte code and translates it to native code for underlying operating system. This architecture is the reason java apps are portable or **platform independent.** C# and python are platform independent as well.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\2.PNG)

* To run the java code type "java nameOfCode.java" in the terminal.

## [4] Interesting facts about Java

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\3.PNG)

# 2. Types

## [2] Variables

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        int age = 30;
        age = 35;
        System.out.println(age);

    }
}
```

## [3] Primitive Types

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\4.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\5.PNG)



```java
package com.google;

public class Main {

    public static void main(String[] args) {
        byte age = 30;
        int viewCount = 123_456_789;
        long viewsCount = 3_123_456_789L; // if we don't mention L in the end java considers the number to be int by default and will throw an error because it has exceeded int limit
        float price = 10.99F; // Also by default all the decimal numbers are considered as double
        char letter = 'A'; // Single character in single quotes
        String name = "Ibrahim"; // Double character in double quotes
        boolean isEligible = false;

    }
}
```

## [4] Reference Types

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\6.PNG)

* One of the main differences between primitive and reference types is that for the reference types we have to allocate the memory using the `new` keyword. For primitive types JRE automatically allocates and release the memory.
* But also notice that we don't need to release the memory allocated for the reference types. It will automatically get released using JRE.
* Another difference is reference types have methods (members) which are defined in the class while primitive type does not have any members.

```java
package com.google;

import java.util.Date; // Date class from java.util automatically imported

public class Main {

    public static void main(String[] args) {

        byte age = 30;
        Date now = new Date(); // memory allocated explicitly while using " new" keyword for reference type
        // This variable now is an instance of the date class. Class is a blueprint for creating new objects or instances

        //now.getTime(); // This instance of the class can access all the members using dot operators, hence we can access some methods for our use

        System.out.println(now);

    }
}
```

## [5] Primitive vs Reference Types

* As we know primitive types is for storing simple values while reference types is for storing complex objects.
* The main difference between these two types are:
  * Reference types are copied by references.
  * Primitive types are copied by values and these values are completely independent of each other.

**Example of Primitive Types** (Values independent of each other)

```java
package com.google;

import java.util.Date; // Date class from java.util automatically imported

public class Main {

    public static void main(String[] args) {

        byte x = 1;
        byte y = x;
        x = 2;
        System.out.println(y);

    }
}
```

**Example of Reference Types** (variables storing address of the object, hence value of the object changed by one variable immediately visible to others)

```java
package com.google;

import java.awt.*;
import java.util.Date; // Date class from java.util automatically imported

public class Main {

    public static void main(String[] args) {
        Point point1 = new Point(x:1, y:1);
        Point point2 = point1;
        point1.x = 2;
        System.out.println(point2);

    }
}
```

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Images\7.PNG)

## [6] Strings

* Strings are reference types in Java. But note that when string class is called from `Java.lang` the package `Java.lang` is not needed to be imported explicitly because it is imported automatically.
* Also notice that as String is a reference type we can also declare string instance as `String message = new String("Hello World");` but as it is used often Java has created a short form of declaring string just like declaring primitive data types.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        //String message = new String("Hello World");
        String message = "Hello World" + "!!"; // This looks like primitive declaration but string is of reference type
        System.out.println(message);
    }
}

```

* As String is of reference type it also has methods.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        //String message = new String("Hello World");
        String message = "Hello World" + "!!"; // This looks like primitive declaration but string is of reference type
        System.out.println(message.endsWith(("!!")));
        System.out.println(message.startsWith(("!!")));
        System.out.println(message.length());
        System.out.println(message.indexOf("o"));
        System.out.println(message.indexOf("k"));
        System.out.println(message.replace("!", "*")); // target and replacement are parameters while ! and * are arguments
        System.out.println(message); // any methods which modifies the string creates a new method because in Java strings are immutable
        System.out.println(message.toLowerCase());
        System.out.println(message.toUpperCase());
        System.out.println(message.trim()); //gets rid of the whitespaces before and after the ''.
        
    }
}
```

## [7] Escape Sequences

```java
package com.google;

public class Main {

    public static void main(String[] args) {

       // String message = "c:\\windows\\...";
       // String message = "c:\nwindows\n...";
        String message = "c:\"windows\"...";
        System.out.println(message);

    }
}
```

## [8] Arrays

* Arrays in Java are of reference type.
* This is how arrays are defined in java `int[] numbers = new int[5];`. 
* If we try to assign something to invalid index, Java will raise an exception which is Java's way of reporting an error.
* When we try to print array then by default java returns the string which is calculated based on address of this object in memory. To print the actual items in the array we have to use class `Array` defined in `Java.Util` which returns the string representation of the array.

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        // numbers[10] = 2; // If we try to assign something to invalid index, Java will raise an exception which is
        // Java's way of reporting an error.
        // System.out.println(numbers);
        System.out.println(Arrays.toString(numbers));
    }
}

```

* Notice that toString method is defined for each datatype like float, byte, etc. This is called method overloading.
* The result is [1, 2, 0, 0, 0] the last undefined items are initialized to 0 because we are dealing with integer array. If we are dealing with boolean these default items will be initialized to false, for  string array they are initialized to empty array.
* Albeit there is a new way of defining array

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] numbers = {2, 3, 4, 1, 4};
        System.out.println(numbers.length);

        System.out.println(Arrays.toString(numbers));
    }
}
```

* **Arrays in Java are of fixed size that is once we create them we cannot add or remove additional items to them. They have the fixed length.**
* If you want to add or remove items you have to use collection classes.

**Sort Method:**

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] numbers = {2, 3, 4, 1, 4};
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
    }
}
```

## [9] Multi-dimensional arrays

To print two dimensional array we have to use `deepToString` method.

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[][] numbers = new int[2][3];
        // int[][][] numbers = new int[2][3][5];
        numbers[0][0] = 1;
        System.out.println(Arrays.deepToString(numbers)); // notice here

    }
}
```

Using curly braces

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        int[][] numbers = {{1,2,3}, {4,5,6}};
        System.out.println(Arrays.deepToString(numbers));

    }
}
```

## [10] Constants

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        final float PI = 3.14F;
    }
}
```

## [11] Arithmetic Expressions

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int result1 = 10 + 3;
        double result2 = (double) 10/ 3;
        int x = 1;
        //int y = x++;
        int y = ++x;
        System.out.println(result1);
        System.out.println(result2);
        System.out.println(x);
        System.out.println(y);
    }
}
```

## [12] Order of Operations

## [13] Casting

**Implicit Casting**:

* Short takes 2 bytes and int takes 4 bytes hence we can store 2 bytes value in 4 byte variable. Therefore when short is added to long like x + 2 as shown in ex below. x is first stored to an **anonymous int variable at anonymous location** under the hood which gets assigned automatically by java and then it is added to int 2. This is called implicit casting.
* Whenever we have a value and that value can be converted to a datatype that is bigger, casting or conversion happens implicit or automatically. hence conversion happens in this fasion **byte > short > int  > long > double**.
* **Hence implicit casting happens whenever there is no possibility of data loss.**

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        // Implicit casting
        short x = 1;
        int y = x + 2;
        System.out.println(y);
    }
}
```

**Explicit Casting:**

* Explicit casting happens when the variable of larger size is converted to the variable of smaller size.
* This means data loss happens here.
* **Explicit casting can only happen between compatible types. Meaning string cannot be casted to int.**

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        // Implicit casting
        double x = 1.1;
        int y = (int)x+ 2;
        System.out.println(y);
    }
}
```

Here in the example below, x cannot be converted to int

```java
package com.google;

import java.sql.SQLOutput;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        // Implicit casting
        String x = "1";
        int y = (int)x+ 2;
        System.out.println(y);
    }
}
```

* But in Java for all the primitive classes we have wrapper classes. These wrapper classes are of reference type. For example we have `Integer` class in `Java.lang` package which has a method called `parseInt()` which takes in the string and returns the int. 
* Similarly we have wrapper class for all primitive data types like float, double, etc

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        // Implicit casting
        String x = "1";
        String a = "1.1";
        int y = Integer.parseInt(x)+ 2;
        double b = Double.parseDouble(a)+ 2;
        //short y = Short.parseShort(x) + 2;
        System.out.println(y);
        System.out.println(b);
    }
}
```

## [14] The Math Class

```java
package com.google;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int result = Math.round(1.1F);
        int result1 = (int)Math.ceil(1.1F);// type-casted to int as ceil produces result in double
        int result2 = (int)Math.floor(1.1F);
        int result3 = Math.max(1, 2);
        double result4 = Math.random(); // random double between 0 to 1
        double result5 = Math.random() * 100; // random double between 0 to 100
        int result6 = (int) Math.round(Math.random() * 100);
        int result7 = (int) (Math.random() * 100);

        System.out.println(result7);
    }
}
```

## [15] Formatting Numbers

* Sometimes no should be represented in currency and also in %. This is called formatting.
* Java.text package has lots of class for handling date, text, numbers and so on.
* Notice here that NumberFormat() is the abstract class and we cannot create instance of abstract class.
* Hence we have to use getCurrencyInstance() which can create instance of NumberFormat class. This method is used for formatting numbers as currency.
* Hence instead of using new operator we are going to use getCurrencyInstance(). This is what is called as factory method because it is used to create new objects. getCurrencyInstance() returns object of type NumberFormat.

```java
package com.google;

import java.text.NumberFormat;


public class Main {

    public static void main(String[] args) {
        //NumberFormat currency = new NumberFormat();
        NumberFormat currency = NumberFormat.getCurrencyInstance(); // here numberFormat object is stored in this variable currency.
        String result = currency.format(1234567.891); // This object has methods for formatting values // This method returns string representation of the number formatted as a currency.

        System.out.println(result);
    }
}
```

Similarly we have getPercentInstance for formatting number as percent.

```java
package com.google;

import java.text.NumberFormat;


public class Main {

    public static void main(String[] args) {
        //NumberFormat percent = new NumberFormat();
        NumberFormat percent = NumberFormat.getPercentInstance(); // here numberFormat object is stored in this variable percent.
        String result = percent.format(0.1); // This object has methods for formatting values // This method returns string representation of the number formatted as a percent.

        //String result = NumberFormat.getPercentInstance().format(0.1); // method chaining
        System.out.println(result);
    }
}
```

## [16] Reading Input

```java
package com.google;

import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // in the () we have to mention where to get input from, From a file, from a terminal, etc
        System.out.print("Age: ");
        byte age = scanner.nextByte();
        System.out.println("You are " + age); // implicit casting converting age to string
    }
}
```

* Notice here that if we will try to input floating point number here we will get an exception because `nextByte` method can only parse byte values. Hence to get rid of exception we have to use `nextFloat` or `nextDouble` .
* For reading a string we have `next()` and `nextLine()` methods.
* `next()` method reads one token (one word separated by whitespace from other). Every time we call `next()` it reads one token. for this reason `nextLine()` method is used which reads the entire line

```java
package com.google;

import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // in the () we have to mention where to get input from, From a file, from a terminal, etc
        System.out.print("Name: ");
        String name = scanner.next();
        System.out.println("You are " + name); // implicit casting converting age to string
    }
}
```

# 3. Control Flow

## [1] Introduction

## [2] Comparison Operator

```java
package com.google;

import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        int x = 1;
        int y = 1;
        System.out.println(x == y);
        System.out.println(x != y);
        System.out.println(x > y);
        System.out.println(x < y);
        System.out.println(x >= y);
        System.out.println(x <= y);
    }
}
```

## [3] Logical Operator

And - &&

OR - ||

Not - !

## [4] If Statements

Syntax:

```java
if () {
    
} else if () {
    
}else {
    
}
```

## [5] Simplifying If Statements

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        int income = 120_000;
        boolean hasHighIncome = (income > 100_000);
    }
}
```

## [6] Ternary Operator

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        int income = 120_000;
        boolean hasHighIncome = (income > 100_000) ? true: false;
    }
}
```



## [7] Switch

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        String role = "admin";
        switch (role) {
            case "admin":
                System.out.println("You're an admin");
                break;
            case "moderator":
                System.out.println("You're a moderator");
                break;
            default:
                System.out.println("You're a guest");
        }
    }
}
```

## [8] Exercise - FizzBuzz

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.printf("Enter the number: ");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        System.out.println(number);
        if (number % 15 == 0)
            System.out.println("FizzBuzz");
        else if (number % 5 == 0)
            System.out.println("Buzz");
        else if (number % 3 == 0)
            System.out.println("Fizz");
        else
            System.out.println("Tari Gand");
    }
}
```

## [9] For Loops

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++)
            System.out.println("Hello World");
    }
}
```

## [10] While Loops

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String input = "";
        // while (input != "quit"); // This statement is wrong as input is a string which is of reference type and we cannot use comparison operator between reference types because it will compare the address of the string objects and not their values.
        // Here the two different strings are stored in two different memory locations even if they have same value "quit".To handle this we need to use equals() method of the string object.

        Scanner scanner = new Scanner(System.in); // It is always recommended to create a Scanner object (instance) outside the while loop or else it will make 10 objects in the memory.

        while (!input.equals("quit")) {
            System.out.println("Input: ");
            input = scanner.nextLine().toLowerCase();
            System.out.println(input);
        }
    }

```

## [11] Do-While Loops

* Do-while loop gets executed once even if condition is false.

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String input = "";

        Scanner scanner = new Scanner(System.in); 
        do {
            System.out.println("Input: ");
            input = scanner.nextLine().toLowerCase();
            System.out.println(input);
        } while (!input.equals("quit"))
    }
}
```

## [12] Break and Continue

* Break - breaks out of loop
* Continue - Sends control to the beginning of the loop

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String input = "";
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Input: ");
            input = scanner.nextLine().toLowerCase();
            if (input.equals("pass"))
                continue;
            if (input.equals("quit"))
                break;
            System.out.println(input);
        }
    }
}

```

## [13] For - Each Loop

Disadvantages of For-Each loop:

* It can be iterated in the forward direction only.

* No access to the index of the item.

## [14] Project - Mortgage Calculator

```java
package com.codewithmosh;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        int principal = 0;
        float monthlyInterest = 0;
        int numberOfPayments = 0;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Principal: ");
            principal = scanner.nextInt();
            if (principal >= 1000 && principal <= 1_000_000)
                break;
            System.out.println("Enter a value between 1000 and 1000000");
        }

        while (true) {
            System.out.print("Annual Interest Rate: ");
            float annualInterest = scanner.nextFloat();
            if (annualInterest >= 1 && annualInterest <= 30) {
                monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Enter a value between 1 and 30");
        }

        while (true) {
            System.out.print("Period (Years): ");
            byte years = scanner.nextByte();
            if (years >= 1 && years <= 30) {
                numberOfPayments = years * MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Enter a value between 1 and 30.");
        }

        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: " + mortgageFormatted);
    }
}
```

# 4. Clean Coding

## [3] Creating Methods

```java
package com.google;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String message = greetUser("Ibrahim", "Rupawala");
        System.out.println(message);
    }

    public static String greetUser (String firstName, String lastName) {// public means this method can be called from outside of this class, we define static method which belongs to a class as oppose to an object
        return ("Hello " + firstName + " " + lastName);
    }
}
```

## [4] Refactoring

* Refactoring means changing the structure of the code without changing its behavior.
* For refactoring the code always look for 2 things:
  * Extract highly related statements.
  * Extract repetitive patterns in the code.
* Use the **Refactor > Extract > Method** feature of IntelliJ.
* Single Method should ideally between 5 to 10 lines of code and no more than 20 lines.
* 

```java
package com.codewithmosh;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    final static byte MONTHS_IN_YEAR = 12;
    final static byte PERCENT = 100;

    public static void main(String[] args) {
        int principal = (int) readNumber("Principal: ", 1000, 1_000_000);
        float annualInterest = (float) readNumber("Annual Interest Rate: ", 1, 30);
        byte years = (byte) readNumber("Period (Years): ", 1, 30);

        printMortgage(principal, annualInterest, years);
        printPaymentSchedule(principal, annualInterest, years);
    }

    private static void printMortgage(int principal, float annualInterest, byte years) {
        double mortgage = calculateMortgage(principal, annualInterest, years);
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println();
        System.out.println("MORTGAGE");
        System.out.println("--------");
        System.out.println("Monthly Payments: " + mortgageFormatted);
    }

    private static void printPaymentSchedule(int principal, float annualInterest, byte years) {
        System.out.println();
        System.out.println("PAYMENT SCHEDULE");
        System.out.println("----------------");
        for (short month = 1; month <= years * MONTHS_IN_YEAR; month++) {
            double balance = calculateBalance(principal, annualInterest, years, month);
            System.out.println(NumberFormat.getCurrencyInstance().format(balance));
        }
    }

    public static double readNumber(String prompt, double min, double max) {
        Scanner scanner = new Scanner(System.in);
        double value;
        while (true) {
            System.out.print(prompt);
            value = scanner.nextFloat();
            if (value >= min && value <= max)
                break;
            System.out.println("Enter a value between " + min + " and " + max);
        }
        return value;
    }

    public static double calculateBalance(
            int principal,
            float annualInterest,
            byte years,
            short numberOfPaymentsMade
    ) {
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
        float numberOfPayments = years * MONTHS_IN_YEAR;

        double balance = principal
                * (Math.pow(1 + monthlyInterest, numberOfPayments) - Math.pow(1 + monthlyInterest, numberOfPaymentsMade))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        return balance;
    }

    public static double calculateMortgage(
            int principal,
            float annualInterest,
            byte years) {

        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
        float numberOfPayments = years * MONTHS_IN_YEAR;

        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        return mortgage;
    }
}

```

# 5. Debugging and Deploying Applications

## [2] Types of Errors

* Compile time Errors - Syntax Errors
* Run time Errors - Logical Errors

## [4] Debugging Java Applications

* Look Videos

## [5] Packaging Java Applications

* Application can be deployed by packaging them up in JAR (Java Archive) file.
* JAR file can run on any system having JRE.
* Here we will be deploying console or command line applications. These are called programs to differentiate it from mobile or web applications.
* **Module is another level of abstraction above Packages**