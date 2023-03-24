package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String courseName = "Learn Java for Beginners Crash Course";

        int position;
        int lastindexposition;

        position = courseName.indexOf("J");
        System.out.println("index of the position is " + position);
        lastindexposition = courseName.lastIndexOf("C");
        System.out.println("Last index of the position is " + lastindexposition);
    }
}
