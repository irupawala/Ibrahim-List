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
