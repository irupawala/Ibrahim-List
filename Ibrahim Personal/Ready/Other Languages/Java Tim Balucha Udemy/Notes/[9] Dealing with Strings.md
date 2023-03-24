# [9.122] What is a String?

* Note down 3 methods of printing a string

## charAt method:

* This method returns the character at a particular index of the string.

```java
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

```

# [9.126] IndexOf & LastIndexOf

* IndexOf method is used to return the index of the character passed.
* LastIndexOf method returns the index of the last occurrence of the character passed.

```java
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
```

# [9.128] ReplaceFirst and substring

* ReplaceFirst is the method used to replace one string with another as mentioned in the syntax.
* substring is used to grab a portion of the string from the string mentioned.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String courseName = "Learn Java for Beginners Crash Course";

        String to_remove = courseName.substring(0, 5);
        System.out.println(courseName.replaceFirst(to_remove, "Earn"));
    }
}
```

# [9.129] String Methods Documentation

https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html

# [9.130] String Equality

* Equal can mean two different things:
  * Both the things are actually the same.
  * Both the things have the same value

* **Testing the java strings equal method focuses on the value of the string**
* **== operator will check reference equality and NOT the value. Which means that its testing of both the objects are same**
* **In a nutshell**
  * **== operator is used for the reference equality**
  * **string method equals is used for the logical equality**

* **In Java, all the strings are created in string constant pool or string literals pool.** 
* When you create a new string its content is added to the string pool. However a check is done first to see if that literal value already exists in the pool. If it already exists, then the existing reference is used and the new string isn't added.
* Even though in the example below you are creating two different strings, both of these variable are sharing a reference to the same literal as contained in the string literal pool.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        String first = "This is a String";
        String second = "THIS IS A STRING";

        System.out.println(first == second);
        System.out.println(second == first);
        System.out.println(first.equalsIgnoreCase(second));
        System.out.println(second.equalsIgnoreCase(first));
    }
}
```

* Note now that when we force java to create a new string rather than grabbing the value from java constant pool, the results for == operator will be false.

# [9.131] Value and Reference Types

Java types fall into two categories

1. Value type
2. Reference type

**Java string are reference types. with the exception of string all the built-in Java types are value type**

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\2.PNG)

* Think of reference  as the address in memory where the value really lives.
* **Value Types are copied by value.**
* **When we create a copy of a reference type, the reference is copied to the new variable's memory location. reference types are copied by reference**

```java
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
    }
}

```

# [9.132] Strings are immutable

* Any methods attempting to modify the string is not actually modifying it but creating a new string.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\3.PNG)

```java
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
```

The figure below demonstrates the situation in the code above

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\4.PNG)

# [9.133] StringBuilder Class

* Java provides stringbuilder class that works a lot like string class but allows its value to be modified without creating new object each time. Hence instance of the stringbuilder object is mutable. This is a mutable reference type.

* replace method has slightly different syntax for StringBuilder.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
//
//        String first = "This is a String";
//        String second = first;

        StringBuilder first = new StringBuilder("This is a String");
        StringBuilder second = first;

        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second);
        System.out.printf("first is the same as second: %s %n", first == second);
        System.out.printf("first.equals(second): %s %n", first.equals(second));

        System.out.println();

        first = first.replace(4, 5, "_");
    //    first = first.replace("_"," ");
        System.out.printf("first: %s %n", first);
        System.out.printf("second: %s %n", second);
        System.out.printf("first is the same as second: %s %n", first == second);
        System.out.printf("first.equals(second): %s %n", first.equals(second));



    }

}
```

**Notice that when strings are immutable first and second are not referring to the same object and second is unchanged and still refers to the original string.**

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\5.PNG)

* But When we use the StringBuilder class we can make change to the object reference type is referring to. The object, in this case at address 5008 has changed. Hence we have replaced the string at the same location. Hence in this case first and second are referring to the same object although we called first to replace the object.

* There is only one object we have two references to it, first and second but there's only one stringbuilder instance.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\6.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\7.PNG)

# [9.135] Equality with Reference Types

* Unlike string StringBuilder class does not have implementation of the equals method.
* The default equals class is used from the object class where a class does not have its own implementation.
* **Here the default method equals checks for REFERENC EQUALITY internally. Hence internally equals method call is using the equals, equals operator to test for equality.**
* Hence notice that for the block commented the results of equals method will be zero. To solve this problem we have to replace the stringbuilder objects to string and then use the equals method on them

```java
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
```

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\8.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Tim Balucha Udemy\Images\9.PNG)

# [9.136] StringBuilder Methods

* Some of the StringBuilder Methods like delete, append returns the reference of the object and not the object itself and hence we can we can use these methods on top of each other in one line of code.

​        `first.delete(0, first.length()).append("Another String").append(" "). append("Another String");`

* Notice that not all the methods returns the reference of the object. To find which object does refer oracle's documentation.
* Also you can check if method returns the reference by checking if it returns the same reference as the original substring on which it is applied.

```java
        if(first.delete(0, first.length()) == first) {
            System.out.println("References are the same");
        }
```

```java
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
```

# [9.139] Introduction to overloaded methods

* Notice that append method of stringbuilder is a overloaded function, meaning there are lots of functions with the same name but it will call the corresponding append function based on the type of argument passed in while calling the function.
* https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/lang/StringBuilder.html

```java
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
```

# [9.140] toString and valueOf Methods

* append method calls valueOf and ValueOf calls toString method.

## toString

* notice that to call the string methods to stringBuilder, stringBuilder should be first converted to string using toString method.

## valueOf

* The **java string valueOf()** method converts different types of values into string. By the help of string valueOf() method, you can convert int to string, long to string, boolean to string, character to string, float to string, double to string, object to string and char array to string.

```java
public static String valueOf(boolean b)  
public static String valueOf(char c)  
public static String valueOf(char[] c)  
public static String valueOf(int i)  
public static String valueOf(long l)  
public static String valueOf(float f)  
public static String valueOf(double d)  
public static String valueOf(Object o)  
```

Returns

string representation of given value