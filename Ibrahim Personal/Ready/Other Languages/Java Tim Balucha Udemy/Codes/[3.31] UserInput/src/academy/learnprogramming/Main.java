package academy.learnprogramming;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner (System.in);
        System.out.println("Please Enter your name");
        String name = scanner.nextLine();
        System.out.println("Hello " + name);
        System.out.println("How old are you ?");

        // Note here the error
        // int age = scanner.nextLine(); // Note that nextLine only works with string hence if you will
        // try to use any other datatype like int with nextLine Java Compiler will throw an error.

        // Using the parseInt method
       // int age = Integer.parseInt(scanner.nextLine());
        //System.out.println(name + " is " + age + " years old");

        // using the nextInt method
        int age = scanner.nextInt();
        System.out.println(name + " is " + age + " years old");
        System.out.printf("%s is %d years old%n", name, age);

        scanner.close();

    }
}
