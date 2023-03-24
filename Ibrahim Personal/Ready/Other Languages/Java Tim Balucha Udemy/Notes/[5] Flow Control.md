# [5.59] For Loops

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        for(int i=0; i<5; i++) {
            System.out.println(i);
        }
    }
}

```

# [5.60] IntelliJ Debugger 

* Create a checkpoint by clicking on the margin.
* Then start debugger by clicking shift+F9. 
* Also notice that you can avoid multiple debugging steps by creating multiple debuggers and then using resume program to jump between debugging steps.



# [5.61] While Loops

```java
package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String userChoice = "A";

        System.out.println("Please choose one of the following options");
        System.out.println("1 - Cappucino");
        System.out.println("2 - Latte");
        System.out.println("3 - Americano");
        System.out.println("4 - Mocha");
        System.out.println("5 - Macchiato");
        System.out.println("6 - Espresso");
        System.out.println("Q - Quit the program");

       while (!userChoice.equals("q")) {
//     while (!(userChoice.equals("q") || userChoice.equals("Q"))) {

        userChoice = scanner.nextLine();
        userChoice = userChoice.toLowerCase();
        System.out.println("You chose " + userChoice);
        }

        scanner.close();
    }
}
```

# [5.70] do - while Loop

While loop will go around 0 or more times.

Do-While loop will go around 1 or more times.

```java
package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String userChoice;

        System.out.println("Please choose one of the following options");
        System.out.println("1 - Cappucino");
        System.out.println("2 - Latte");
        System.out.println("3 - Americano");
        System.out.println("4 - Mocha");
        System.out.println("5 - Macchiato");
        System.out.println("6 - Espresso");
        System.out.println("Q - Quit the program");

        do {
            userChoice = scanner.nextLine();
            userChoice = userChoice.toLowerCase();
            System.out.println("You chose " + userChoice);
        } while (!userChoice.equals("q"));

        scanner.close();
    }
}

```

