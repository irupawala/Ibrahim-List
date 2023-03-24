# [6.74] If Statement

* final declares constant. final tells the Java that value can't be changed.
* Constant declarations have to be at the class level which is why they are not inside main method
* Also notice that if we make these constant int ROCK, PAPER, SCISSORS as public then they can also be accessed outside the class.
* We have declared ROCK, PAPER, SCISSORS as static and the main method is also static hence the main method is also able to access this and we are able to use this constants in static method

```java
package academy.learnprogramming;

import java.util.Random;
import java.util.Scanner;

public class Main {

    private static final int ROCK = 0; // final declares constant. final tells the Java that value can't be changed
    private static final int PAPER = 1;
    private static final int SCISSORS = 2;
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {


        Random randomGenerator = new Random();

        String playerChoice;
        int playerValue = -1;
        do {
            int computerValue = randomGenerator.nextInt(3);
            String computerChoice = " ";

            if (computerValue == ROCK) {
                computerChoice = "rock";
            } else if (computerValue == PAPER) {
                computerChoice = "paper";
            } else if (computerValue == SCISSORS) {
                computerChoice = "scissors";
            }

            System.out.println("Please enter rock, paper or scissors ");
            playerChoice = scanner.nextLine().toLowerCase();


            if (playerChoice.equals("rock")) {
                playerValue = ROCK;
            } else if (playerChoice.equals("paper")) {
                playerValue = PAPER;
            } else if (playerChoice.equals("scissors")) {
                playerValue = SCISSORS;
            } else {
                System.out.printf("%s is not a valid character %n", playerChoice);
            }

            System.out.printf("Computer chose %s, player chose %s. %n", computerChoice, playerChoice);

            if (playerValue == computerValue) {
                System.out.println("It's a Draw!");
            } else if (playerValue - 1 == computerValue || (playerValue == ROCK && computerValue == SCISSORS)) {
                System.out.println("Player Wins!");
            } else {
                System.out.println("Computer Wins!");
            }
        } while (getYesOrNo("Would you like to play again ?"));
        scanner.close();
    }

    public static boolean getYesOrNo(String question) {
        String answer;

        while (true) {
            System.out.printf("%s%n", question);
            answer = scanner.nextLine();
            answer = answer.toLowerCase();

            if (answer.equals("y")) {
                return true;
            }

            if (answer.equals("n")) {
                return false;
            }
        }
    }
}
```

# [6.80] Switch Statement

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
            switch (userChoice) {
                case "1":{
                    System.out.println("Making a Cappucino");
                    break;
                }
                case "2":{
                    System.out.println("Making a Latte");
                    break;
                }
                case "3":{
                    System.out.println("Making a Americano");
                    break;
                }
                case "4":{
                    System.out.println("Making a Mocha");
                    break;
                }
                case "5":{
                    System.out.println("Making a Macchiato");
                    break;
                }
                case "6":{
                    System.out.println("Making a Espresso");
                    break;
                }
                case "q":{
                    System.out.println("Quitting the program. Bye-Bye");
                    break;
                }

                default:{
                    System.out.println("Please input a valid value");
                    break;
                }

            }
        } while (!userChoice.equals("q"));


        scanner.close();
    }
}
```

# [6.83] Break Statement

* Break stops the execution of the further statement

# [6.84] Continue Statement

* Continue skips the current iteration of the loop.

# [6.85] Ternary Operator

```java
booleanExpression ? expression1 : expression2
```

