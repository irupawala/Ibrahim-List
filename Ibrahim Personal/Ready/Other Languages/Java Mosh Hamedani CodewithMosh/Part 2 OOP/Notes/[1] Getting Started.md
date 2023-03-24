# 1. Getting Started

## [2] Programming Paradigms

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\1.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\2.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\3.PNG)



## [3] Benefits of OOP

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\4.PNG)

# 2. Classes

## [2] Classes & Objects

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\5.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\6.PNG)

## [3] Creating Classes

* In Java each class should be created in a separate file.
* Notice that In Java never leave even the reference data types uninitialized as by default they will be set to null and give NullPointerException thus crashing our program.

```java
package com.google;

public class TextBox {
   // public String text; // Try this code with the main file by uncommenting this line.
    public String text = ""; // Field

    public void setText(String text) {
        this.text = text; // this.text is the text of the class (field, reference to the current object).
                          // this keyword is used when field and the parameter passed to the method has the same name
                          // Notice here the dot operator will also have other methods which are members of the object.
                          // These members are inherited automatically when we declare any class in Java.
    }

    public void clear() {
        text = "";
    }

}

```

## [4] Creating Objects

```java
package com.google;

public class Main {

    public static void main(String[] args) {
	// write your code here
        //TextBox textBox1 = new TextBox();
        var textBox1 = new TextBox(); // using var keyword we can write shorter code. When we write var, Java will identify the type of the object automatically based on the object declaration on the RHS.
        textBox1.setText("Box 1");
        System.out.println(textBox1.text.toUpperCase());

        var textBox2 = new TextBox();
        textBox2.setText("Box 2");
        System.out.println(textBox2.text.toUpperCase());

    }
}
```

## [5] Memory allocations

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\7.PNG)

* Notice that the Objects are created in heap. In the example discussed above the objects TextBox() is created in heap while the variables textBox1 and textBox2 are created in stack thus storing the address of the object in the stack. This is the reason objects are called reference types.
* In the example below when we create new object textBox2, then the new variable textBox2 copies the address of textBox1 hence now both are pointing to the same object in the heap thus now any change brought by any variable will be immediately visible by other.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
	// write your code here
        //TextBox textBox1 = new TextBox();
        var textBox1 = new TextBox(); // using var keyword we can write shorter code. When we write var, Java will identify the type of the object automatically based on the object declaration on the RHS.
        var textBox2 = textBox1;
        textBox2.setText("Hello World");
        System.out.println(textBox1.text);
    }
}
```

* Memory deallocation happens automatically in Java unlike C++
* When we exit a method JRE will immediately remove all the variables stored in the stack. In the example above when the execution of main method is done the variables textBox1 and textBox2 will be immediately removed.
* But the TextBox() object remains as it is. For that there is another process in the background which keeps on monitoring these objects. If it remains unused for specific amount of time it will automatically remove the object from the heap. This is called as **"Garbage Collection"**.

## [6] Procedural Programming

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        int baseSalary = 50_000;
        int extraHours = 10;
        int hourlyRate = 20;

        int wage = calculateWage(baseSalary, extraHours, hourlyRate);
        System.out.println(wage);
    }

    public static int calculateWage(
            int baseSalary,
            int extraHours,
            int hourlyRate
    ){
        return baseSalary + (extraHours * hourlyRate);
    }
}
```

There are some disadvantages of Procedural Programming:

* Each method becomes very bulky and messy.
* Very difficult to reuse the code.

## [7] Encapsulation

* Encapsulation means Bundle the data and methods that operate on the data in a single unit.
* The main difference in OOP is methods inside the class has no parameters, here instead of passing parameters like in procedural programming we should encapsulate the values with the methods which operate on them inside the single object.

Main.Java

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var employee1 = new Employee();
        employee1.baseSalary = 50_000;
        employee1.hourlyRate = 20;
        int wage = employee1.calculateWage(10);
        System.out.println(wage);

    }
}
```

Employee.Java

```java
package com.google;

public class Employee {
    public int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }
}
```

## [8] Getters and Setters

* Getters are used to make sure that user does not enter invalid values for certain fields in the class thus the fields are made private in the class instead of public and then accessed using a method called getters within the class. Also there will be conditions placed in this class to ensure that the user does not input the invalid values for the fields.
* Now to access the fields from the class there will be a method defined in the similar fashion called getters. These methods simply returns the fields.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var employee1 = new Employee();
        employee1.setBaseSalary(50_000);
        employee1.setHourlyRates(20);
        int wage = employee1.calculateWage(10);
        System.out.println(wage);

    }
}
```

```java
package com.google;

public class Employee {
    private int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }

    public void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    public int getBaseSalary () {
        return baseSalary;
    }

    public void setHourlyRates (int hourlyRate) {
        if (hourlyRate < 0)
            throw new IllegalArgumentException("Hourly Rates cannot be less then zero");
        this.hourlyRate = hourlyRate;
    }

    public int getHourlyRate() {
        return hourlyRate;
    }
}
```

## [9] Abstraction

* Reduce complexity by hiding unnecessary details in our classes.
* With abstraction we want to hide the implementation details of the class and treat it like a black box.

## [10] Coupling

* Level of dependency between classes.
* We want to reduce the coupling as much as possible because the more the dependency between the class the more changes are required for the dependent class when any of the class is changed.
* Also for big applications changing the class would require recompilation of all the dependent classes.
* The more the public methods we have in our class the more are the coupling points to the Main class hence to reduce the coupling we can make our setters private in the class.

```java
package com.google;

public class Employee {
    private int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }

    public void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    private int getBaseSalary () {
        return baseSalary;
    }

    public void setHourlyRates (int hourlyRate) {
        if (hourlyRate < 0)
            throw new IllegalArgumentException("Hourly Rates cannot be less then zero");
        this.hourlyRate = hourlyRate;
    }

    private int getHourlyRate() {
        return hourlyRate;
    }
}
```

## [11] Reducing Coupling

* OOP is all about coupling, impact of changes, abstraction.

````java
package com.google;

public class Main {

    public static void main(String[] args) {
        var browser = new Browser();

        browser.navigate("www.google.com");
    }
}
````

```java
package com.google;

public class Browser {
    public void navigate (String address) {
        String ip = findIPAddress(address);
        String html = sendHTTPrequest(ip);
        System.out.println(html);
    }

    private String sendHTTPrequest(String ip) {
        return "<html><html>";
    }

    private String findIPAddress(String address) {
        return "10.195.64.87";
    }
}
```

* Notice the example here where sendHTTPrequest and findIPaddress are made private thus not accessible to the main class.
* Here the only coupling point is navigate.



## [12] Constructors

* Notice that in the employee example above the calculateWage method won't work without us providing values for HourlyRate and BaseSalary. Hence it is necessary that user enters HourlyRate and BaseSalary  before calculateWage for the program to work correctly. As a programmer we want to reduce the guess work for the user as much as possible and make the interface of the class simple. Hence constructors are used in which we will ask the user to pass the necessary parameters as an argument to the object.



* A constructor is a special method called when we create a new object.
* Notice that when we don't explicitly create a constructor Java will use automatically created method called "Default Constructor" to create a new object.
* Java use Default constructor to initialize our fields with default values. Numbers are going to be zero, Booleans false and reference types null
* **Notice that constructor does not have any return types**.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var employee1 = new Employee(50_000, 20);
        int wage = employee1.calculateWage(10);
        System.out.println(wage);

    }
}
```

```java
package com.google;

public class Employee {
    private int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public Employee(int baseSalary, int hourlyRate) {
        setBaseSalary(baseSalary);
        setHourlyRates(hourlyRate);
    }

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }

    private void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    private int getBaseSalary () {
        return baseSalary;
    }

    private void setHourlyRates (int hourlyRate) {
        if (hourlyRate < 0)
            throw new IllegalArgumentException("Hourly Rates cannot be less then zero");
        this.hourlyRate = hourlyRate;
    }

    private int getHourlyRate() {
        return hourlyRate;
    }
}
```

## [13] Method Overloading

* Creating a different implementation of the method with different parameters.
* In the calculateWage(10) method we are passing extrahours but what if the employee did not worked any extra hours, in that case we have to make we have to call a method without any arguments but we cannot do that
* hence we create a new method with no arguments. This is method overloading.

```java
    public int calculateWage() {
        return calculateWage(0);
    }
```

* **Also notice that in languages like C++ and python we can give default argument to the constructor itself but in Java that is not possible as shown below.**

```java
    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }
```

* **Hence the only way to make a parameter optional in Java is overloading a method.**
* However overloading a method make a program ugly and hard to maintain. hence overload only when absolutely necessary.

## [14] Constructor Overloading

* In the employee example above what if we want to create an employee which doesn't have hourlyRate ?
* Hence we can overload constructor in the same fashion.

```java
    public Employee(int baseSalary) {
        //setBaseSalary(baseSalary); // this is one method to use
        //setHourlyRates(0);

        // another is to use this keyword. As we know "this" is a reference to current object

        this(baseSalary, 0);
    }
```

## [15] Static Members

* There are two members in the OOP a class can have:
  * instance members
  * static members
* Instance members belongs to instances or objects. Example all the fields and members that we declared for the employee class belongs to the instance of the object hence they are instance members.
* We can view all the instance members by dot operator with the object name

```java
ObjectName. 
```

```java
employee1.
```

* Static and Class members belongs to a class and not objects.
* **Static fields are created when value is independent of objects and we are going to share it across all objects.**
* We can view all the instance members by dot operator with the class name.

```java
ClassName.
```

```java
Employee.
```

* The purpose of static members is to represent a concept that should be in a single place. For example in the employee example "numberOfEmployees" does not belong to individual employee. This is where we use static members.
* Notice in the example below we have created numberOfEmployees field which we will increment each time an object is created.
* **Notice that static members can be accessed without creating instance of an object like instance members in the main class.**

```java
    public static int numberOfEmployees;

    public Employee(int baseSalary, int hourlyRate) {
        setBaseSalary(baseSalary);
        setHourlyRates(hourlyRate);
        numberOfEmployees++;
    }
```

* Similarly we can also create static methods.

```java
 public static void printNumberOfemployees() {
        System.out.println(numberOfEmployees);
    }
```

* **But notice that this static method cannot access any members of the object but only static members inside the class**. although it is inside the employee class. To access the members of the object we have to first create an instance of the object inside this static class.
* **That is the reason we declared all the methods in the main class as static so that they can be called from the main method in the first part of the course.**
* **Also Main method is declared as static to enable the JRE to directly call Main method without having to create a new object.**

Final Code:

Main.Java

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var employee1 = new Employee(50_000, 20);
        //System.out.println(Employee.numberOfEmployees);
        Employee.printNumberOfemployees();
        int wage = employee1.calculateWage(10);
        System.out.println(wage);

    }
}
```

Employee.Java

```java
package com.google;

public class Employee {
    private int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public static int numberOfEmployees;

    public Employee(int baseSalary, int hourlyRate) {
        setBaseSalary(baseSalary);
        setHourlyRates(hourlyRate);
        numberOfEmployees++;
    }

    public static void printNumberOfemployees() {
        System.out.println(numberOfEmployees);
    }
    public Employee(int baseSalary) {
        //setBaseSalary(baseSalary); // this is one method to do this
        //setHourlyRates(0);

        // another is to use this keyword. As we know "this" is a reference to current object

        this(baseSalary, 0);
    }

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }

    public int calculateWage() {
        return calculateWage(0);
    }

    private void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    private int getBaseSalary () {
        return baseSalary;
    }

    private void setHourlyRates (int hourlyRate) {
        if (hourlyRate < 0)
            throw new IllegalArgumentException("Hourly Rates cannot be less then zero");
        this.hourlyRate = hourlyRate;
    }

    private int getHourlyRate() {
        return hourlyRate;
    }
}
```

# 3. Refactoring towards an Object-oriented Design

# 4. Inheritance

## [2] Inheritance

* Inheritance means reusing the members of the parent class so that reusability increases.
* Observe the example of TextBox() class inheriting from UIControl() class

Main Class

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        //var control = new UIControl();
        var control = new TextBox();
        control.isEnabled();
        System.out.println(control.isEnabled());
    }
}
```

UIControl Class

```java
package com.google;

public class UIControl {
    private boolean isEnabled = true;

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
        }
}
```

TextBox Class

```java
package com.google;

public class TextBox extends UIControl{ 
    private String text = ""; // Field

    public void setText(String text) {
        this.text = text; // this.text is the text of the class (field, reference to the current object).
                          // this keyword is used when field and the parameter passed to the method has the same name
                          // Notice here the dot operator will also have other methods which are members of the object.
                          // These members are inherited automatically when we declare any class in Java.
    }

    public void clear() {
        text = "";
    }

}
```

**Notice how TextBox is Inheriting from the UIControl**

```java
public class TextBox extends UIControl{ 
```

## [3] The Object Class

* Every class that we declare directly or indirectly inherits from the object class.

* Here TextBox() inherits from the UIControl() and UIControl() inherits from the Object Class.

* Note that we don't need to explicitly write 

* ```java
  public class UIControl extends Object
  ```

* Java Compiler automatically asks this for us.

* Object Class is declared in Java.lang package and hence it is available everywhere.

* To Check out what methods object class have we can declare a new object in the main class which is instantiated from the Object class.

```java
var obj = new Object(); 
        //obj.getClass(); // Returns class object. To read metadata about an object. Example all the methods and fields defined in that object
        //obj.equals(); // For comparing objects
        //obj.hashCode(); // returns an integer based on the address of this object in a memory
        //obj.toString(); // returns the string equivalent of an object
```

* hashcode() method returns an integer calculated based on the address of the object in memory.
* The address of the object goes to a function called hash function and this function will map it to a numeric value called hash.
* The hash code is used in lots of situation one of them is comparing objects in memory.

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        //var control = new UIControl();
        //var obj = new Object(); // Object Class is declared in Java.lang package and hence it is available everywhere
        //obj.getClass(); // Returns class object. To read metadata about an object. Example all the methods and fields defined in that object
        //obj.equals(); // For comparing objects
        //obj.hashCode(); // returns an integer based on the address of this object in a memory
        //obj.toString(); // returns the string equivalent of an object

        var box1 = new TextBox();
        System.out.println(box1.hashCode()); // returned is an integer calculated based on the address of the object in memory
        // the address of the object goes to a function called hash function and this function will map it to a numeric value called hash.
        // the hash code is used in lots of situation one of them is comparing objects in memory.

        var box2 = box1;
        System.out.println(box1.hashCode());
        System.out.println(box2.hashCode());
        System.out.println(box1.equals(box2)); // This compares the hashcodes of the memory.

        System.out.println(box1.toString());
        // return result is com.google.TextBox@3feba861 // package.class@hashCode in Hex

    }
}
```

## [4] Constructors and Inheritance

* Notice that constructors are created by super(). **super() is added in each class constructor automatically by compiler.**
*  As we know well that default constructor is provided by compiler automatically but it also adds super() for the first statement. 
* If a constructor does not explicitly invoke a superclass constructor, the Java compiler automatically inserts a call to the no-argument constructor of the superclass. If the super class does not have a no-argument constructor, you will get a compile-time error.  
* Note the following cases:
  * Parameterized constructor or Non Parameterized constructor of the derived class will not throw any error if there is a Non Parametrized constructor defined in the base class. Also if no class is defined in the base class then also we don't have any problem as in that case it will invoke the default built-in constructor of the base class.
  * Parameterized constructor or Non Parameterized constructor of the derived class **will throw an error if there is a Parametrized constructor defined in the base class because in this case you are asking java to use user-defined constructor.**
  * In this case as we are not using default built-in constructor of Java nor we are using non-parameterized constructor of the base class **super() will not be added automatically by compiler at the beginning of the constructor.** **Hence in those scenarios we have to explicitly call Super() in the derived class to create a base class constructor**
  *  The base class constructor will be called before the derived class constructor. This makes sense because it guarantees that the base class is properly constructed when the constructor for the derived class is executed. This allows you to use some of the data from the base class during construction of the derived class. 
* Refer these links
  *  https://www.geeksforgeeks.org/super-keyword/ 
  *  https://stackoverflow.com/questions/7173019/why-is-constructor-of-super-class-invoked-when-we-declare-the-object-of-sub-clas/7173164 

Main Class:

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var control = new TextBox("Ibrahim");
    }
}

```

UIControl Class:

```java
package com.google;

public class UIControl {
    private boolean isEnabled = true;
    
    public UIControl(boolean isEnabled) {
        this.isEnabled = isEnabled;
        System.out.println("UI Parameterized Control");
    }

//    public UIControl() {
//        System.out.println("UI Control");
//    }

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
        }
}
```

TextBox Class:

```java
package com.google;

public class TextBox extends UIControl{
    private String text = ""; // Field

//    public TextBox() {
//        System.out.println("Text Box");
//    }
    
    public TextBox(String text) {
        super(true);
        System.out.println(text);
    }

    public void setText(String text) {
        this.text = text;
    }

    public void clear() {
        text = "";
    }

}
```

## [5] Access Modifiers

* Public members are accessible from outside of the class
* **Private members are NOT accessible from outside of the class also they are not inherited by the subclasses.**
* **They are used to hide the implementation details of the class.**
* **Protected members are also available in Java. They are public inside the package but not accessible by other packages. Protected members are accessible in the CHILD class (and not Main Class) OF THE SAME PACKAGE AS WELL AS ANOTHER PACKAGE.**

* **Hence, protected members are public in their package. But they are also accessible by child classes in different packages.**
* Generally using private members is considered as bad programming practice.
* Now if we don't specify any access modifier type then it is **package private** which is also default access modifier and that means this field is public anywhere in this package but private outside this package. Even Classes on other packages will not be able to inherit this field, it's private everywhere outside the package.

```java
boolean isEnabled = true;
```

**Refer This:**

```
______________________________________________________________
|           │ Class │ Package │ Subclass │ Subclass │ World  |
|           │       │         │(same pkg)│(diff pkg)│        |
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|public     │   +   │    +    │    +     │     +    │   +    | 
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|protected  │   +   │    +    │    +     │     +    │        | 
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|no modifier│   +   │    +    │    +     │          │        | 
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|private    │   +   │         │          │          │        |
|___________|_______|_________|__________|__________|________|
```

## [6] Overriding Methods

* Method overriding means modifying the method defined in the base class from the derived class.
* Method overloading is declaring a method multiple times with different signatures and different parameters.
* Consider an example of overriding the toString() method declared in the base Object() class.
* Before overriding any method we write an annotation. Read below.

```java
    @Override // This is called annotation. An annotation is a label that we attach to a class member. And with this we give extra information to Java Compiler.
    // With this we are telling Java Compiler that we are overriding toString() method of the object class. And with this the Java compiler will check the signature of this method. It will make sure that this class has exact same signature.
    public String toString() {
        return (text);
```

Main Class

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var textbox = new TextBox();
        System.out.println(textbox.toString()); // calling toString method which is inherited from the base class
       // System.out.println(textbox); // we don't have to explicitly call toString method because the print line method automatically calls the toString method on any object passed to it.
    }
}
```

UIControl Class

```java
package com.google;

public class UIControl {
    protected boolean isEnabled = true;


    public UIControl() {
        System.out.println("UI Control");
    }

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
        }
}
```

TextBox Class

```java
package com.google;

public class TextBox extends UIControl{
    private String text = "Hello World"; // Field

    public TextBox() {
        System.out.println("Text Box");
    }

    @Override // This is called annotation. An annotation is a label that we attach to a class member. And with this we give extra information to Java Compiler.
    // With this we are telling Java Compiler that we are overriding toString() method of the object class. And with this the Java compiler will check the signature of this method. It will make sure that this class has exact same signature.
    public String toString() {
        return (text);

    }

    public void setText(String text) {
        this.text = text;
    }

    public void clear() {
        text = "";
    }

}
```

## [7] Upcasting and Downcasting

Upcasting - Casting an object to one of its super types or parent.

Downcasting - Casting an object to one of its sub types.

Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var control= new UIControl(true);
        var textbox= new TextBox();
        System.out.println(textbox);
        //show(control); // This statement is valid as textbox object inherits all the members of the UIControl object hence we can say that textbox object isA UIControl object ane hence inheritance represents an isA relationship
    }

    /*
    public static void show (UIControl control){ // notice how textbox object is automatically casted to UIControl object. This is called as Upcasting.

        // public static void show (Object control){ // This is also upcasting as every textbox is also an object.
           System.out.println(control); // Notice that when we print control object then the toString method of the textbox gets executed. This is known as here it is executing the overridden method.


        // But note that even though at runtime we are passing textbox object at the compile time when we are coding this method we don't have access to any of the methods in our textbox.
        // during coding this method only the members of the base class (UIControl class) will be visible here.
        // but what if we want to work with one of the methods of the textbox class. Well you need to explicitly cast this control to textbox
        // This is what we call as downcasting.

//
//        if (control instanceof TextBox) { // This operator will return true if the object that we pass here at runtime is an instance of the textbox class. Then we can safely cast it to textbox and call its method.
//            var textbox = (TextBox) control;
//            textbox.setText("Hello World");
//        }
//
//        System.out.println(control);
        // But notice that when a control object (Base class object) is passed to this method and it is downcasted to textbox the code will fail with an exception thrown.
        // This is because every textbox is a control object but vise versa is not true. That is every derived class is a base class but not vise versa.

        // To prevent this error before casting we need to make sure that the object passed at the runtime is an instance of the textbox class. Then we can sefely cast it as textbox.


    }

     */
}

```

UIControl

```java
package com.google;

public class UIControl {
    protected boolean isEnabled = true;


    public UIControl() {
        System.out.println("UI Control");
    }

    public UIControl(boolean isEnabled) {
        this.isEnabled = isEnabled;
        System.out.println("UI Parameterized Control");
    }

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
        }
}

```

TextBox

```java
package com.google;

public class TextBox extends UIControl{
    private String text = ""; // Field

    public TextBox() {
        System.out.println("Text Box");
    }


   @Override
   public String toString() {
   return text;
   }


    public void setText(String text) {
        this.text = text;
    }

    public void clear() {
        text = "";
    }

}
```

## [8] Comparing Objects

* When you compare two objects, the result will be false as the variable declared stores the address in the memory where the objects are stored, this is because objects are of reference types.
* Even when you use the equals method to compare objects you will get false as the default implementation of this method in the object class compares two objects based on their references. So here we have to override the equals method to compare two objects.
* Also by convention we have to also overwrite the hashcode generation method because hash code generated here should be based on the contents of this objects. In contrast, the default implementation of the hashCode method generates a hash based on the address of an object in memory.

Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var point1 = new Point(1,2);
        var point2 = new Point(1,2);
        System.out.println(point1 == point2);
        System.out.println(point1.equals(point2));
    }
}

```

Point

```java
package com.google;

public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

Consider the updated codes:

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        var point1 = new Point(1,2);
        var point2 = new Point(1,2);
        //System.out.println(point1 == point2);
        //System.out.println(point1.equals(point2));
        //System.out.println(point1.equals(new TextBox())); // program will crash throwing exception at runtime if objects other then point is passed.
        //System.out.println(point1.equals(point1)); //special check should be added in the equals method
        System.out.println(point1.hashCode());
        System.out.println(point2.hashCode());
        // The hash code received here is based on the contents of this objects.
        // In contrast, the default implementation of the hashCode method generates a hash based on the address of an object in memory.

    }
}
```

```java
package com.google;

import java.util.Objects;

public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }


        @Override
    public boolean equals(Object obj) { // notice here we cannot change the passed parameter of object type because then signature will defer and it won't be overwritten
        if (this == obj) // checking if object is compared to itself
            return true;

        if (!(obj instanceof Point)) return false; // As discussed in the earlier section we need to make sure that the object is of point type or else an exception will be raised during runtime

        var other = (Point) obj; // downcasting the object to point type as the object we will be receiving will be of point type
        return (this.x == x && this.y == y);
    }

   // As a best practice whenever we overwrite the equals method we should also overwrite hashCode method


    @Override
    public int hashCode() {
        //return super.hashCode(); It is calling hashcode() based on the implementation in the base class but instead what we want is to generate hashcode based on the value of this field x and y
        // To generate hashcode we will use class "Objects" and method in it called hash.
        // We can give this method bunch of values and it will generate a hash value.
        // A hash value in theory uniquely identifies objects.
        // one or more arguments can be given to hash method
        return Objects.hash(x,y);

    }
}
```

## [9] Polymorphism

* Poly means many and morphism means form.
* Polymorphism allows our objects to take many forms.
* Observe in the code below how we are able to iterate over the same method overwritten in different classes using polymorphism.

Main :

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        UIControl[] controls = {new TextBox(), new CheckBox()};
        for(var control: controls)
            control.render();
            // if control is TextBox
            // render TextBox
            // else if it is a checkBox
            // render checkBox
    }
}
```

CheckBox :

```java
package com.google;

public class CheckBox extends UIControl {

    @Override
    public void render() {
        System.out.println("Render CheckBox");
    }
}
```

TextBox:

```java
package com.google;

public class TextBox extends UIControl{
    private String text = ""; // Field

    public TextBox() {
        System.out.println("Text Box");
    }

    @Override
    public String toString() {
        return text;
    }

    @Override
    public void render() {
        System.out.println("Render TextBox");
    }

    public void setText(String text) {
        this.text = text;
    }

    public void clear() {
        text = "";
    }

}
```

## [10] Abstract Classes and Methods

* Abstract Classes are used in the situation where we will declare the class but we don't want to instantiate it.
* In the last example the whole purpose of the UICOntrol class is to provide some common code for it's subclasses like textBox and checkBox. We know what a textBox is we know, what checkBox is but we don't know what UIControl is. It's an **ABSTRACT** concept.
* In situations like this we can declare the UIControl class as abstract and we cannot instantiate it we can only extend and create new classes that derive from the UIControl.

```java
public abstract class UIControl {
```

* If we declare it as abstract we won't be able to instantiate UIControl like this in the main class.

```java
UIControl[] controls = {new UIControl(), new TextBox(), new CheckBox()};
```

* Also we can declare the **render method in UIControl as abstract and this will force the derived classes to implement this method.**

```java
public abstract void render(); // Notice that there is no body here as it will be overwritten in the derived class. // Just declaration and not the implementation.
```

* Hence Java allows two possibilities if the abstract method is declared.
  1. Derived classes must override the abstract method.
  2. If Derived classes does not override the abstract method then the derived class itself must be declared as abstract.
* **Also note that abstract method can only exist within abstract class.**

Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
        UIControl[] controls = {new TextBox(), new CheckBox()};
        //UIControl[] controls = {new UIControl(), new TextBox(), new CheckBox()}; This is not possible after the class is declared abstract
        for(var control: controls)
            control.render();
            // if control is TextBox
            // render TextBox
            // else if it is a checkBox
            // render checkBox
    }
}
```

UIControl

```java
package com.google;

public abstract class UIControl {
    protected boolean isEnabled = true;


    public UIControl() {
        System.out.println("UI Control");
    }

    public UIControl(boolean isEnabled) {
        this.isEnabled = isEnabled;
        System.out.println("UI Parameterized Control");
    }

    public abstract void render(); // Notice the abstract method

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
    }
}
```

CheckBox

```java
package com.google;

public class CheckBox extends UIControl {
//public abstract class CheckBox extends UIControl { // If method is not overridden then class should be declared as abstract

    @Override
    public void render() {
        System.out.println("Render CheckBox");
    }
}

//    @Override
//    public void render() {
//        System.out.println("Render CheckBox");
//    }
//}
```

## [11] Final Classes and Methods

* Final is exactly opposite to abstract.
* **As abstract classes can only be extended and not instantiated, Final Classes can only be instantiated but not extended.**
* String Class in Java is declared as final because strings in Java are immutable, if we call any of the methods like toUpperCase(), etc it will create a new string. We always want to create new string when we call new methods like this. we never want to break this assumption.

```java
package com.google;

public final class CheckBox extends UIControl {
//public abstract class CheckBox extends UIControl { // If method is not overridden then class should be declared as abstract

    @Override
    public void render() {
        System.out.println("Render CheckBox");
    }
}

public class MyCheckBox extends CheckBox {} // This will give error.Cannot inherit from final class

```

* Similarly we can declare a method as final and it cannot be overridden.

```java
    public final void enable() {
        isEnabled = true;
    }
```

## [12] Deep Inheritance Hierarchies

* Don't create deep inheritance hierarchies.
* Inheritance should be of one or two levels but no more than 3 levels.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\8.PNG)

* Any change in the Entity here will need recompilation and re-deployment of each of the class in the hierarchy

   

## [13] Multiple Inheritance

* In languages like C++ and Java a class can have multiple parents, this is what we call multiple inheritance. Designer of java not to implement this feature because it brings a number of complexities.
* Ambiguity occurs when multiple parents have same field names or same method names.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\9.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\10.PNG)

**Extended Version of this problem is called Diamond Diagram.**

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\11.PNG)

## [14] Inheritance Quiz

* Refer the quiz in downloads. Very Important.



# 5. Interfaces

## [2] What are Interfaces

* Interfaces are used to build loosely-coupled, extensible, testable applications.
* Let us say B is derived from A then If there is any change in Class B, A will be affected and all the other classes dependent on A will also get affected. Hence recompilation of all the classes will be required.
* So to prevent these, we should try to keep the coupling or relationship between our classes as loose as possible.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\12.PNG)

* Abstraction is one of the ways to loosened details between the two classes. By hiding the implementation details and only exposing what is necessary we loosened the coupling between classes
* However, that is not enough hence interfaces are used which completely decouples classes hence if B is changed A is not affected at all.



![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\13.PNG)

* **Interface is a class which only has method declaration and No implementation.**
* Interface only defines the capabilities a class should have.
* To minimize the impact of changes between these two classes you put an interface between them and decouple them.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\14.PNG)

* If you change B, A will not be affected because it knows nothing about B. This is what we call programming against interfaces.
* Tomorrow we can change B and A will not be affected because it knows nothing about A.

![](C:\Users\1000249643\Desktop\Programming Langauages\Java Mosh Hamedani CodewithMosh\Part 2 OOP\Images\15.PNG)

* One example is a phone charger until the pin fits you can use any charger to charge your phone.
* Another example it tax rules, rules change each year but you should be still able to pay the tax.
* **We can independently test each part coupled to interface and make sure that it is working this is called as UNIT TESTING.**

## [3] Tightly coupled code

* In this example TaxReport() is tightly coupled to TaxCalculator2018() because

  1. If we extend the constructor in the TaxCalculator2018 from

  ```java
  public TaxCalculator2018(double taxableIncome) {
  ```

  to

  ```java
  public TaxCalculator2018(double taxableIncome, double ins) {
  ```

  then TaxReport and all the other classes dependent on TaxCalculator2018 has to be changed.

  2. Even if we change a calculateTax() method in TaxCalculator2018 from 0.3 to 0.4 then all the classes needs to be recompiled.

TaxCalculator2018()

```java
package com.google;

public class TaxCalculator2018 {
    private double taxableIncome;

    public TaxCalculator2018(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }

    public double calculateTax() {
        return taxableIncome * 0.3;
    }
}
```

TaxReport()

```java
package com.google;

public class TaxReport {
    private TaxCalculator2018 calculator;  // This is because we want calculator to be available throughout the class

    public TaxReport() {
       calculator = new TaxCalculator2018(100_000); // This is different from how it was defined earlier. Instead of initializing and declaring it in the same line like this TaxCalculator calculator = new TaxCalculator(100_000); here we are initializing and defining it in two lines. 
        
        // This is because we want calculator to be available throughout the class
        
    }

    public void show() {
        var tax = calculator.calculateTax();
        System.out.println(tax);
    }
}
```

## [4] Creating an Interface

* TaxCalculator.Java shown below is an interface class.

* In the interface we don't have any state or data. we don't have any fields only method declarations that determines what needs to be done.

* ```java
  public double calculateTax()
  ```

* This is an abstract class as we don't have any implementation.

* As public is grayed out we can delete it this is because every method we declare here has to be implemented by the class, and these methods should be public so they can be accessed by other classes because this interface determines the public interface of this class, the public contract.

* hence we can get rid of this public as it is already understood as public by JRE.

* ```java
  double calculateTax();
  ```

* Now we want our TaxCalculator() class to implement our new interface. This can be defined like this

* ```java
  public class TaxCalculator2018 implements TaxCalculator{
  //public class TaxCalculator2018 extends Object TaxCalculator{ // If this class has a base class we can define it like this.
  ```

* Even we don't have compilation error it is best practice to write Override annotation to our interface method because this gives extra information to Java Compiler that this method is the implementation of the calculateTax() method in our interface. In the future if we get rid of this method in the interface it will throw a compilation error here.

* ```java
      @Override // Even we don't have compilation error it is best practice to write Override annotation to our interface method because this gives extra information to Java Compiler that this method is the impelemntation of the calculateTax() method in our interface. In the future if we get rid of this method in the interface it will throw a compilation error here.
      public double calculateTax() { // this is implementation of the method that we declare in our interface.
          return taxableIncome * 0.3;
      }
  ```

* But still TaxReport.Java is tightly coupled to TaxCalculator2018().

TaxCalculator2018

```java
package com.google;

// we want this class to implement our new interface.
public class TaxCalculator2018 implements TaxCalculator{
//public class TaxCalculator2018 extends Object TaxCalculator{ // If this class has a base class we can define it like this.
    private double taxableIncome;

    public TaxCalculator2018(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }

    @Override // Even we don't have compilation error it is best practice to write Override annotation to our interface method because this gives extra information to Java Compiler that this method is the impelemntation of the calculateTax() method in our interface. In the future if we get rid of this method in the interface it will throw a compilation error here.
    public double calculateTax() { // this is implementation of the method that we declare in our interface.
        return taxableIncome * 0.3;
    }
}
```



TaxReport

```java
package com.google;

public class TaxReport {
    private TaxCalculator2018 calculator;

    public TaxReport() {
       calculator = new TaxCalculator2018(100_000); // This is different from how it was defined earlier. Instead of initializing and declaring it in the same line like this TaxCalculator calculator = new TaxCalculator(100_000); here we are initializing and defining it in two lines
    }

    public void show() {
        var tax = calculator.calculateTax();
        System.out.println(tax);
    }
}
```



TaxCalculator (Interface)

```java
package com.google;

public interface TaxCalculator { // In the interface we don't have any state or data. we don't have any fields only method declarations that determines what needs to be done.
    //public double calculateTax(); // This is an abstract class as we don't have any implementation. As public is grayed out we can delete it this is because every method we declare here has to be implemented by the class, and these methods should be public so they can be accessed by other classes.
    // Because this interface determines the public interface of this class, the public contract.
    // hence we can get rid of this public as it is already understood as public by JRE.

    double calculateTax();
}
```



Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
// We cannot instantiate an interface like a class. because this is interface a contract not a concrete implementation.
    }
}
```

## [5] Dependencies Injection

* In the last example we have seen that our TaxReport class is still instantiating TaxCalculator2018.
* According to Dependencies Injection principle, **Our Classes should not instantiate their dependencies.**
* Here the TaxReport class should not create the class it should only use it. Creating and using it are two different concerns and hence this is called separation of concerns.
* **Hence we want to take this responsibility of creating a class from our report class and give it to another class, we will have that class give our report class the calculator object. This is what we call dependency Injection.**
* So that other class will pass or inject a dependency.
* Dependency Injections can be done in various ways:
  * Constructor Injection (Passing Dependency by constructor of the class)
  * Setter Injection
  * Method Injection



## [6] Constructor Injection

* We don't want our TaxReport Class to be dependent on concrete implementation, we want it to be dependent on interface. hence we are going to change the type of the Object in TaxReport with the interface TaxCalculator.

* ```java
  private TaxCalculator2018 calculator;
  ```

* is changed to 

* ```java
  private TaxCalculator calculator;
  ```

* Also we don't want to TaxReport to create a TaxCalculator2018 object, Hence in this example we will use a constructor injection to set this field calculator

* ```java
  public TaxReport() {
    calculator = new TaxCalculator2018(100_000); 
  }
  ```

* is changed to 

* ```java
  public TaxReport (TaxCalculator calculator) {
      this.calculator = calculator;
  }
  ```

* This is what we call constructor Injection as we are injecting dependencies using constructor.

* Now we will create the object of the TaxCalculator2018 in the Main Class and pass it to the TaxReport.

* Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
// We cannot instantiate an interface like a class. because this is interface a contract not a concrete implementation.
       var calculator = new TaxCalculator2018(100_000);
       var report = new TaxReport(calculator);
    }
}
```

* In this case note that our TaxReport does not know anything about our concrete implementation. It is only interacting with our interface. This is what we call programming against interfaces. Tomorrow we can create another class TaxCalculator2019 and pass it to TaxReport class. TaxReport doesn't care and its not affected.
* Also if we change the implementation of calculateTax() method in TaxCalculator2018 then only TaxCalculator2018 needs to be recompiled. TaxReport() is not affected, this is called loose coupling in action.
* The way we have injected dependency here is called poor man's dependency injection. In the simple program we have only two classes so we can easily create and inject these dependencies by hand but in large applications you have hundreds of classes and these classes might have several dependencies, we don't want to create hundred of objects in the main method and pass them to the constructor of the classes. That's where we use dependencies injection framework. So there are frameworks out there that makes it really easy to pass these dependencies to our classes. **Spring is the most popular one.**

## [7] Setter Injection

* We have already seen how the constructor is defined in our Main class and passed to the TaxReport, now what if we want to change the object passed to TaxReport class ?.
* Hence we can define a setter in the TaxReport() and that can change the assignment of the field assigned in the constructor of TaxReport(), here `calculator` from our Main Class.

TaxReport

```java
package com.google;

public class TaxReport {

    private TaxCalculator calculator;

    public TaxReport(TaxCalculator calculator) {
       this.calculator = calculator;
    }

    public void show() {
        var tax = calculator.calculateTax();
        System.out.println(tax);
    }

    public void setCalculator(TaxCalculator calculator) {
        this.calculator = calculator;
    }
}
```



* The benefit of setter injection is that we can change these dependencies throughout the lifetime of our program.
* Now in this example lets say we have a new class TaxCalculator2019 and we want our TaxReport class to show reports for the object of this new class. 
* Hence in the TaxCalculator2019 we have to implement the interface. As the interface is abstract class we have to implement the methods defined in the TaxCalculator class (here calculateTax()).

TaxCalculator2019

```java
package com.google;

public class TaxCalculator2019 implements TaxCalculator {
    @Override
    public double calculateTax() {
        return 0;
    }
}
```

* Now we can use the setter and change these dependencies throughout the lifetime of our program.

Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
// We cannot instantiate an interface like a class. because this is interface a contract not a concrete implementation.
       var calculator = new TaxCalculator2018(100_000);
       var report = new TaxReport(calculator);
       report.show();

       report.setCalculator(new TaxCalculator2019());
       report.show();
    }
}
```

TaxCalculator2018

```java
package com.google;

// we want this class to implement our new interface.
public class TaxCalculator2018 implements TaxCalculator{
//public class TaxCalculator2018 extends Object TaxCalculator{ // If this class has a base class we can define it like this.
    private double taxableIncome;

    public TaxCalculator2018(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }

    @Override // Even we don't have compilation error it is best practice to write Override annotation to our interface method because this gives extra information to Java Compiler that this method is the impelemntation of the calculateTax() method in our interface. In the future if we get rid of this method in the interface it will throw a compilation error here.
    public double calculateTax() { // this is implementation of the method that we declare in our interface.
        return taxableIncome * 0.3;
    }
}
```

## [8] Method Injection

* Setter Injection is great but we have to call it each time in our main program.
* Instead of this we can pass our object to the TaxReport to the place where we use it that is to the method in the TaxReport which use the object. In this case it is `show()`.
* With this implementation we don't need a constructor or setter in our TaxReport() Class.

TaxReport

```java
package com.google;

public class TaxReport {

//    private TaxCalculator calculator;
//
//    public TaxReport(TaxCalculator calculator) {
//       this.calculator = calculator;
//    }

    public void show(TaxCalculator calculator) {
        var tax = calculator.calculateTax();
        System.out.println(tax);
    }


//    public void setCalculator(TaxCalculator calculator) {
//        this.calculator = calculator;
//    }
}
```

* This is called Method Injection that is pass the dependencies to the method that needs that dependency.

Main

```java
package com.google;

public class Main {

    public static void main(String[] args) {
// We cannot instantiate an interface like a class. because this is interface a contract not a concrete implementation.
       var calculator = new TaxCalculator2018(100_000);
       var report = new TaxReport();
       report.show(calculator);


       //report.setCalculator(new TaxCalculator2019());
       report.show(new TaxCalculator2019());
    }
}
```

* TaxCalculator2018 and TaxCalculator2019 is same as previous code.
* Notice that here our TaxReport class still have coupling but this coupling is with Interface and not with concrete implementation. Even if we change the concrete implementation our TaxReport isn unaffected.
* But if we change the contract by adding or removing one of the existing ones of course we have broken the contract and the classes that are dependent on the contract will be broken. Hence the interfaces should be defined carefully and as small as possible.

## [9] Interface Segregation Principle

* Divide big interfaces into smaller ones.
* With this we can reduce the impact of changes.
* Consider the example below

UIWidget. Java (Interface)

```java
package com.google;

public interface UIWidget {
    void drag();
    void resize();
    void render();
}
```

Dragger. Java

```java
package com.google;

public class Dragger {
    public void drag (UIWidget widget) {
        widget.drag();
        System.out.println("Dragging Done !!");
    }
}
```

* In this example even if we change the method resize which is not required by Dragger class, dragger class needs to be recompiled.
* Here even though we are dealing with small interface we are mixing different concerns or capabilities.
* Hence if we have a big interface every time we change the interface all the dependent classes and their dependencies will be affected. This is where Interface Segregation Principle comes to the rescue **it says that we should divide the interface into smaller ones each interface focusing on the single capability.**

UIInterface

```java
package com.google;

public interface UIWidget extends Draggable, Resizable { // here lets say we need all the capabilities in one place, hence we can use inheritance between the two interfaces.
    // note here that UIWidget is a child interface hence unlike classes Java Interface can have multiple parents
    // This is not a problem for Java interfaces which we say classes faces due to multiple inheritance because if this parents
    // declare the same method with the same signature this interface will inherit only one of them and also the imnplementation is defined
    // in a separate class hence there is no ambiguity

    void render();
}
```

Resizable

```java
package com.google;

public interface Resizable {
    void resize();
    void resize(int size);
    void resize(int x, int y);
    void resizeTo(UIWidget widget);

}
```

Draggable

```java
package com.google;

public interface Draggable {
    void drag();
    void resize(int size);
}
```

Dragger

* Here there is a confusion as the instance of the interface cannot be made.
* Maybe this is just an example or maybe this is the way to couple the other class to interface.

```java
package com.google;

public class Dragger {
    public void drag (UIWidget draggable) { // here we are not creating an instance of the UIWidget class instead we are coupling our
        // Dragger class to UIWidget or Draggable Interface or contract
        // working with UIWidget interface here will give us more classes
    //public void drag (Draggable draggable) {
        draggable.drag();// This interface here is very lightweight as it has only one coupling point.
        System.out.println("Dragging Done !!");

    }
}
```

## [10 & 11] MyTube Project

See the results in codes section

## [12] Fields

* There are some new features added in the recent releases of Java which has changed it's meaning.
* Over the next few chapters we will be looking at this new features.
* We can also define fields in the interface. This field is final meaning it cannot be changed.
* Also they are static hence we can use them without creating instance of it.
* **Hence we are dealing with public, static, final fields.**
* But we can only define the fields here if we are extremely sure that the value will remain same across all implementations. Like PI, number of months in a year.
* Even if we define the constant in the field, we are leaking the implementation details to all the classes.
* Also what if we don't need that field anytime in the future and if we delete it from the interface. Then all the connected classes will be affected.

```java
package com.google;

public interface TaxCalculator {
    double calculateTax();
    float minimumTax = 100; // Field
}
```

* And you can access it in the classes **using the . Operator with the className and not ObjectName.**

```java
package com.google;

public class Main {

    public static void main(String[] args) {

       System.out.println(TaxCalculator.minumumTax);
    }
}

```

## [13] Static Methods

* Static Methods can also be defined in the interface.
* Note here that unlike Fields defined in Interface we have to explicitly write `static` for the methods as the methods are not static.

```java
package com.google;

public interface TaxCalculator {
    double calculateTax();
    
    static double getTaxableIncome (double income, double expense);
    	return income - expense;
}
```

* Again we are providing implementation details in the interface which should never be the case. **Interface is only about What's and not How's.**
* **How's don't belong to interfaces, they belong to classes.**
* Then we may ask what if we are implementing a simple logic which will never change and also this logic is used across all the classes in use. **That's when we define an abstract class and move the logic there so it can be shared by all it's children's.**
* Also we will be implementing out interface TaxCalculator here in abstract class itself and then we don't need to implement it in it's child.

AbstractTaxCalculator:

```java
package com.google;

public abstract class AbstractTaxCalculator implements TaxCalculator {

    protected double getTaxableIncome (double income, double expense){ // here we are making it protected because we want to hide it from outside the package and only allow it to use it in the classes which inherits from this abstract class.
        return income - expense;
    }
}
```

TaxCalculator:

```java
package com.google;

public interface TaxCalculator { 
    double calculateTax();
    //float minimumTax = 100; // Field
}
```

TaxCalculator2018:

```java
package com.google;

public class TaxCalculator2018 extends AbstractTaxCalculator{ // here we are ignoring implements TaxCalculator because it is extending from AbstractTaxCalculator which has already implemented TaxCalculator

    private double taxableIncome;

    public TaxCalculator2018(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }


    @Override 
    public double calculateTax() { 
        getTaxableIncome(200, 100);

        return taxableIncome * 0.3;

    }
}
```

## [14] Private Methods

* Private Methods in interface are also allowed from JRE8 but this feature also blurs off the entire meaning of interface and is not recommended to use.
* 

## [15] Interfaces and Abstract Classes

![1571497232909](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1571497232909.png)

* Interfaces are contracts
* Abstract classes - To share code



* As we know that interface can have multiple parents while class can inherit only from one parent, lots of people are using interface as a hack to achieve multiple inheritance. but interfaces should not be confused with classes, we should only treat them like contracts to build loosely coupled applications.

## [16] When to use Interface

![1571499419261](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1571499419261.png)

