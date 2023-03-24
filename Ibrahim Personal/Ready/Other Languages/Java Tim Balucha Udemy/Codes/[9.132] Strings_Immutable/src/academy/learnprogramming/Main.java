package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        int x = 5;
        int y = x;
        System.out.printf("x = %d, y = %d %n", x, y);
        System.out.printf("x is the same as y: %s %n", x == y);

        String first = "This is a String";
        String second = first;


        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second);
        System.out.printf("first is the same as second: %s %n", first == second);

        System.out.println();

        // understand this part first and observe how the new string is created at different location
        /*
        first = first.replace(" ", "_");
        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second); */

        // Let's see how it behaves when we have 2 references to different strings, but strings have the same value.

        first = first.replace(" ", "_");
        first = first.replace("_"," ");
        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second);
        System.out.printf("first is the same as second: %s %n", first == second);
        System.out.printf("first.equals(second): %s %n", first.equals(second));



    }

}
