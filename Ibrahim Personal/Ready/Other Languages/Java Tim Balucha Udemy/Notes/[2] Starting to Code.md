

* In Java before we can use a variable we have to declare it that is because Java is a statistically taught language.

# [2.20] Using var vs an Explicit type

* var is another datatype which can be used. Java documentation suggests using var wherever possible.
* But **var can only be used when we can infer the type from the assignment. If we don't assign anything to var java compiler has no way of knowing what type of value it should hold.**

```java
package academy.learnprogramming;

import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);

        int firstNumber = 2;
        int secondNumber = 5;


        var subtraction = 7;
        int answer;
        String prompt = ". Press ENTER when ready";

       // System.out.println("Think of a number between 1 and 10. Press ENTER when ready");
        System.out.println("Think of a number between 1 and 10" + prompt);
        scanner.nextLine();
        System.out.println("Multiply your number by " + firstNumber + prompt);
        scanner.nextLine();
        System.out.println("Now Multiply your number by " + secondNumber + prompt);
        scanner.nextLine();
        System.out.println("Divide the result by the number you originally thought of" + prompt);
        scanner.nextLine();
        System.out.println("Now subtract " + subtraction + prompt);
        scanner.nextLine();

        answer = firstNumber * secondNumber - subtraction;
        System.out.println("The answer is " + answer);

        scanner.close();

    }
}

```

* Notice that we have to always assign a value to an integer or variable in Java. 
* Now we are going to assign random numbers to the firstNumber, secondNumber and subtraction.
* Also notice that declaring the prompt has it's own benefit. We can change the prompt displayed anytime in our code.
* Also the random number generated in the code below ranges from 0 to 7.

```java
package academy.learnprogramming;

import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        Random randomGenerator = new Random(); // This declares Random class instance to randomGenerator. We can call the instance of this number to get the random number

        int firstNumber = randomGenerator.nextInt(8) +2; // nextInt method is used to return a random number in the range 0 to 8. Then we are adding 2 hence the range of number will be 2 to 10

        int secondNumber = randomGenerator.nextInt(8) +2;

        var subtraction = randomGenerator.nextInt(8) +2;
        int answer;
        String prompt = ". Press ENTER when ready";

       // System.out.println("Think of a number between 1 and 10. Press ENTER when ready");
        System.out.println("Think of a number between 1 and 10" + prompt);
        scanner.nextLine();
        System.out.println("Multiply your number by " + firstNumber + prompt);
        scanner.nextLine();
        System.out.println("Now Multiply your number by " + secondNumber + prompt);
        scanner.nextLine();
        System.out.println("Divide the result by the number you originally thought of" + prompt);
        scanner.nextLine();
        System.out.println("Now subtract " + subtraction + prompt);
        scanner.nextLine();

        answer = firstNumber * secondNumber - subtraction;
        System.out.println("The answer is " + answer);

        scanner.close();

    }
}

```

* Now the question is do we have to wait till the line `answer = firstNumber * secondNumber - subtraction;`to give answer its value.
* The answer is NO. `answer` here gets the value as soon as it is declared.
* Hence how can we modify the code, so that the answer is assigned a value as soon as it is declared. Line `answer = firstNumber * secondNumber - subtraction;` at the end of the code can then be deleted.

```java
package academy.learnprogramming;

import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        Random randomGenerator = new Random(); // This declares Random class instance to randomGenerator. We can call the instance of this number to get the random number

        int firstNumber = randomGenerator.nextInt(8) +2; // nextInt method is used to return a random number in the range 0 to 8. Then we are adding 2 hence the range of number will be 2 to 10

        int secondNumber = randomGenerator.nextInt(8) +2;

        var subtraction = randomGenerator.nextInt(8) +2;
        int answer = firstNumber * secondNumber - subtraction;;
        String prompt = ". Press ENTER when ready";

       // System.out.println("Think of a number between 1 and 10. Press ENTER when ready");
        System.out.println("Think of a number between 1 and 10" + prompt);
        scanner.nextLine();
        System.out.println("Multiply your number by " + firstNumber + prompt);
        scanner.nextLine();
        System.out.println("Now Multiply your number by " + secondNumber + prompt);
        scanner.nextLine();
        System.out.println("Divide the result by the number you originally thought of" + prompt);
        scanner.nextLine();
        System.out.println("Now subtract " + subtraction + prompt);
        scanner.nextLine();

        //answer = firstNumber * secondNumber - subtraction;
        System.out.println("The answer is " + answer);

        scanner.close();

    }
}

```

# [2.24] Naming Convention

* Google - Google Java Style Guide
* 

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\1.PNG)



* Note here that left is C# and right is Java.

* Java Conventions are as follows:
  * Class name Program should start with Capital
  * Class name should be at the end of line
  * method names (e.g. main) should start with lower case if it has more than one word then the subsequent word should consist of first word as capital. This is called camel casing.
  * variables names should also be in CamelCasing
  * method name nextLine() is camel casing.
  * scanner is an object(instance) of the class Scanner.
  * static method can also be spotted with the help of naming convention. ReadLine is a static method while nextLine is an instance method.
  *  Because Doctor has a Capital D, it refers to a class. That means Response and response are static methods.

