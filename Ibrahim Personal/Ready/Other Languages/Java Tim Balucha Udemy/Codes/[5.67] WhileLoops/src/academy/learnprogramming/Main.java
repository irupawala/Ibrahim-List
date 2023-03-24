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

      // while (!userChoice.equals("q")) {
//        while (!(userChoice.equals("q") || userChoice.equals("Q"))) {
        do {
            userChoice = scanner.nextLine();
            userChoice = userChoice.toLowerCase();
            System.out.println("You chose " + userChoice);
        } while (!userChoice.equals("q"));

        scanner.close();
    }
}
