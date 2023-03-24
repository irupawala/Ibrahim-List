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