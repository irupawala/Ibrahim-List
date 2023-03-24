package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String courseName = "Learn Java for Beginners Crash Course";
        String message = "Welcome to";

        // concatenate courseName and message to create a new String
        System.out.println(message + courseName);

        // use string format
        String fullMessage2 = String.format("%s%s", message, courseName);
        System.out.println(fullMessage2);

        // use printf
        System.out.printf("Hello, and %sthe %s.%n", message, courseName);

        for (int i=0; i < courseName.length(); i++) {
            char character = courseName.charAt(i);
            System.out.println(character);
        }
    }
}
