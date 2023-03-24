package academy.learnprogramming;

import javax.print.Doc;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    var scanner = new Scanner(System.in); // Scanner is a class which reads user inputs

        System.out.println(Doctor.intro());// before we got some inputs from the user though we have to print some instructions from Doctor Class
        // Doctor class has a method called intro which returns the introduction string
        // To use the method of the class we have to use .notation
        // That way java knows intro is a method defined in Doctor class
        var userInput = "";
       // userInput = scanner.nextLine();

        while(!userInput.equalsIgnoreCase( "quit")) {
            userInput = scanner.nextLine();
            String response = Doctor.response(userInput);
            System.out.println(response);

        }

	    scanner.close();
    }
}
