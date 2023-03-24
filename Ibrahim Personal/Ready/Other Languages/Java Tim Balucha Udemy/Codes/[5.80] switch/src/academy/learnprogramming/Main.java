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
                    //break;
                    continue;
                }

            }

            System.out.println("Dispensing Coffee");
            System.out.println("Have a nice day");

        } while (!userChoice.equals("q"));


        scanner.close();
    }
}
