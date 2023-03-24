package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String courseName = "Learn Java for Beginners Crash Course";

        String to_remove = courseName.substring(0, 5);
        System.out.println(courseName.replaceFirst(to_remove, "Earn"));
    }
}
