package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
//
//        String first = "This is a String";
//        String second = first;

        StringBuilder first = new StringBuilder("This is a String");
        StringBuilder second = new StringBuilder("This is a String");

        /*
        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second);
        System.out.printf("first is the same as second: %s %n", first == second);
        System.out.printf("first.equals(second): %s %n", first.equals(second));
        */

        String firstString = first.toString();
        String secondString = second.toString();

        System.out.printf("first: %s %n", firstString);
        System.out.printf("second: %s %n", secondString);
        System.out.printf("first is the same as second: %s %n", firstString == secondString);
        System.out.printf("first.equals(second): %s %n", firstString.equals(secondString));
    }

}
