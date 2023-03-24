package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        StringBuilder first = new StringBuilder("This is a String");

        int a = 12;
        int b = 24;
        int c = 36;

        first.append(' '); // string
        first.append(a);
        first.append(' ');
        first.append(3.45);
        first.append(' ');
        first.append(a == 12);
        first.append(' ');
        first.append(b > c);

        System.out.println(first);

    }

}