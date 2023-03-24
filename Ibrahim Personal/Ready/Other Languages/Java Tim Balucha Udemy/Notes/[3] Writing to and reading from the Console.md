# [3.29] Console Input with nextLine



* Scanning Input using the nextline method of the Scanner class on object scanner

```java
package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please choose one of the following options");
        System.out.println("1 - Cappucino");
        System.out.println("2 - Latte");
        System.out.println("3 - Americano");
        System.out.println("4 - Mocha");
        System.out.println("5 - Machhiato");
        System.out.println("6 - Espresso");
        System.out.println("7 - Quit the program");

        String userChoice = scanner.nextLine(); //using the nextline method of the scanner class
        System.out.println("You chose " + userChoice);

        scanner.close();
    }
}

```

# [3.31] Console Input Text and Numbers

* `nextLine` only works with string hence if you will// try to use any other datatype like int with nextLine Java Compiler will throw an error.
* There are two ways to solve this problem:
  * Convert the string obtained from `nextLine` to int use `Integer.parseInt(String)`
  * Directly user `nextInt` method of the scanner. This does the same  process of converting the string to int in the background.
* Also Notice that in `parseInt` method you will get an error if you enter something which cannot be converted to Int.
* Also notice that if you use the int as a string in a sentence then it won't throw an error but only when you try to do some arithmetic operations on it.
* See the code below

```java
package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        System.out.println("Please Enter your name");
        String name = scanner.nextLine();
        System.out.println("Hello " + name);
        System.out.println("How old are you ?");

        // Note here the error
        // int age = scanner.nextLine(); // Note that nextLine only works with string hence if you will
        // try to use any other datatype like int with nextLine Java Compiler will throw an error.

        // Using the parseInt method
       // int age = Integer.parseInt(scanner.nextLine());
        //System.out.println(name + " is " + age + " years old");

        // using the nextInt method
        int age = scanner.nextInt();
        System.out.println(name + " is " + age + " years old");


        scanner.close();

    }
}

```

# [3.32] Reading Numbers in HammerBitcoin (using a function)

```java
    private int getNumber(String message) {
        while (true) {
            System.out.print(message);
            String userInput = scanner.nextLine();
            try {
                return Integer.parseInt(userInput);
            } catch (Exception ignored) {
                System.out.printf("%s isn't a number!%n", userInput);
            }
        }
    }
```

* In this function notice the try and catch expression which is used to catch errors if any.

# [3.33] Console Output Text and String Formatting

* We have noticed in the println method before that to display a variable we have to concatenate string and variable. Concatenating this way is inefficient and reduces the readability, instead of this we can use printf method to print formatted text.

```java
package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        System.out.println("Please Enter your name");
        String name = scanner.nextLine();
        System.out.println("Hello " + name);
        System.out.println("How old are you ?");


        int age = scanner.nextInt();
        System.out.println(name + " is " + age + " years old");
        System.out.printf("%s is %d years old%n", name, age);
        // %n - new line, printf doesn't add new line automatically like println
        // %s - string
        // %d - integer
        


        scanner.close();

    }
}

```

* Note here how the access specifiers %s, %d and %n are defined.

# [3.34] String Format Alignment

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
        // write your code here

        String apples = "Apples";
        int appleQuantity = 8;
        int applePrice = 100;

        String oranges = "Oranges";
        int orangeQuantity = 12;
        int orangePrice = 80;

        String column1Heading = "Fruit";
        String column2Heading = "Quantity";
        String column3Heading = "Price";

        System.out.printf("%-12s %8s %6s%n", column1Heading, column2Heading, column3Heading);
        System.out.printf("%-12s %-8d %6d cents%n", apples, appleQuantity, applePrice);
        System.out.printf("%-12s %-8d %6d cents%n", oranges, orangeQuantity, orangePrice);

    }

}

```

* Note here that when -ve sign is used before access specifiers then the string or int is aligned to left.

* Or else if a number greater than the number of characters in the strings are used before access specifiers then the string is aligned to right.

* Also notice that if we make the width too small for the value we are printing then java will ignore the width and print the entire string.


# [3.35] More about String Formatting

* In this example we are going to format the string to display all the prices in a currency format for this we are going to use built in number format class of the java.
* Note that while using the number formatting we have to use %s as access specifiers and not %d as the results displayed will be $x.xx
* Also, Notice that the number formatting will display the result in $'s and not cents hence over here we are converting cents to dollars by dividing the price by 100.0. We are using 100.0 because we want to force the java to display the results in floating point format and not Int.
* Also notice how we are able to n number of minimum digits with the help of setMinumumFractionDigits

```java
package academy.learnprogramming;

import java.text.NumberFormat;

public class Main {

    public static void main(String[] args) {
        // write your code here


        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
        currencyFormat.setMinimumFractionDigits(3);


        String apples = "Apples";
        int appleQuantity = 8;
        int applePrice = 100;

        String oranges = "Oranges";
        int orangeQuantity = 12;
        int orangePrice = 80;

        String column1Heading = "Fruit";
        String column2Heading = "Quantity";
        String column3Heading = "Price";

        System.out.printf("%-12s %8s %6s%n", column1Heading, column2Heading, column3Heading);
        System.out.printf("%-12s %-8d %6s %n", apples, appleQuantity,
                currencyFormat.format(applePrice / 100.0));
        System.out.printf("%-12s %-8d %6s %n", oranges, orangeQuantity,
                currencyFormat.format(orangePrice / 100.0));

    }

}

```

* Notice how width and precision works

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        System.out.printf("PI is %f %n", Math.PI);
        System.out.printf("PI is %.3f %n", Math.PI);
        System.out.printf("PI is %.0f %n", Math.PI);
        System.out.printf("PI is %.12f %n", Math.PI);
        System.out.printf("PI is %.99f %n", Math.PI);
        System.out.printf("PI is %16.4f %n", Math.PI);

    }

}

```

