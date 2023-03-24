package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String first = "This is a String";
        String second  = new String("This is a String");
       // String second = "THIS IS A STRING";

        System.out.println(first == second);
        System.out.println(second == first);
        System.out.println(first.equalsIgnoreCase(second));
        System.out.println(second.equalsIgnoreCase(first));
    }
}
