# [12] Structure of a Java Program

```java
package academy.learnprogramming;

public class Main {	

    public static void main(String[] args) {
	    System.out.println("Hello World!");
    }
}
```

* **Package** in [Java](https://www.geeksforgeeks.org/java/) is a mechanism to encapsulate a group of classes, sub packages and interfaces. Packages are used for:
  
* Preventing naming conflicts. For example there can be two classes with name Employee in two packages, college.staff.cse.Employee and college.staff.ee.Employee.
  
* For More information refer 
  
  [Geeks](https://www.geeksforgeeks.org/packages-in-java/#targetText=Package%20in%20Java%20is%20a,Preventing%20naming%20conflicts.&targetText=A%20default%20member%20(without%20any,in%20the%20same%20package%20only.)
  
* **In Java, every line of code that can actually run needs to be inside a class.** This line declares a class named `Main`, which is `public`, that means that any other class can access it.

* **Notice that when we declare a public class, we must declare it inside a file with the same name (Main.java), otherwise we'll get an error when compiling.**

* ```java
  public static void main(String[] args) {
  ```

This is the entry point of our Java program. the main method has to have this exact signature in order to be able to run our program.

- `public` again means that anyone can access it.
- `static` means that you can run this method without creating an instance of `Main`.
- `void` means that this method doesn't return any value.
- `main` is the name of the method.

The arguments we get inside the method are the arguments that we will get when running the program with parameters. It's an array of strings.

```java
System.out.println("This will be printed");
```

- `System` is a pre-defined class that Java provides us and it holds some useful methods and variables.
- `out` is a static variable within System that represents the output of your program (stdout).
- `println` is a method of out that can be used to print a line.



# [13] Dot Notation Part 1



```java
package academy.learnprogramming;

import javax.print.Doc;
import java.util.Scanner; // Scanner is a class in java.util package used for obtaining the input of the primitive types like int, double, etc. and strings. 

public class Main {

    public static void main(String[] args) {
	    var scanner = new Scanner(System.in); // Scanner is a class which reads user inputs. 

        System.out.println(Doctor.intro());
        // before we got some inputs from the user though we have to print some instructions from Doctor Class
        // Doctor class has a method called intro which returns the introduction string
        // To use the method of the class we have to use .notation
        // That way java knows intro is a method defined in Doctor class
        
	    scanner.close();
    }
}
```

# [14] Dot Notation Part 2

```java
package academy.learnprogramming;

import javax.print.Doc;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    var scanner = new Scanner(System.in); // Scanner is a class which reads user inputs

        System.out.println(Doctor.intro());// before we got some inputs from the user though we have to print some instructions from Doctor Class
        // Doctor class has a method called intro which returns the introduction string
        // To use the method of the class we have to use .notation
        // That way java knows intro is a method defined in Doctor 
        
        
        var userInput = ""; // defining an empty string 
       // userInput = scanner.nextLine(); // Inputs from the keybord are stored into the string userInput variable. Notice that scanner is defined above. Note here that we cannot have conversation with Eliza if the userImput is taken only once.

        while(!userInput.equalsIgnoreCase( "quit")) { // To request input continuosly till the quit is typed. Note here that the while loop continues till the userInput string does not equals to quit.
            // Also equalsIgnoreCase Method is used to make quit case insensitive
            userInput = scanner.nextLine();
            String response = Doctor.response(userInput); // prviding userInput to Eliza as an argument and getting the response back from the Eliza. Here we are providing input to the response method of the Doctor Class
            System.out.println(response); // printing out response
            
        }

	    scanner.close();
    }
}

```

```java
// SAME PROGRAM WITHOUT COMMENTS

package academy.learnprogramming;

import javax.print.Doc;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    var scanner = new Scanner(System.in); 

        System.out.println(Doctor.intro());
        var userInput = ""; 

        while(!userInput.equalsIgnoreCase( "quit")) { 
            userInput = scanner.nextLine();
            String response = Doctor.response(userInput); 
            System.out.println(response);  
        }

	    scanner.close();
    }
}

```

* Note here that we have two classes here main Class and Doctor Class.
* Note that the java looks for a special method called main during runtime.
* Here the main method is a specific method and also it should have a specific signature. 
* Note that main method should have the exact same signature as defined for it to fulfill the conditions for the main method that a program can execute.
* Main Method is the entry point in the code.