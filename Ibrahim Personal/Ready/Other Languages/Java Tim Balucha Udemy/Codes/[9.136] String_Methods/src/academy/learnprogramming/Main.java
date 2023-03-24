package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        StringBuilder first = new StringBuilder("This is a String");
        StringBuilder second = new StringBuilder("This is a String");

        System.out.printf("first: %s %n", first);
        System.out.println("Clearing first");

        if(first.delete(0, first.length()) == first) {
            System.out.println("References are the same");
        }

        // first.delete(0, first.length()); // This returns the reference to the stringBuilder method that it was called on.
        // hence in this case it clears out first and then returns reference to it. hence we are able to call delete after
        // the call to delete.

        // System.out.printf("first: *%s* %n", first);
        // first.append("Another String"); // also the append method also returns the reference of the object on which it is called on
        // hence we can call other methods again on this append.

        first.delete(0, first.length()).append("Another String").append(" "). append("Another String");
        System.out.printf("first: *%s* %n", first);

    }

}