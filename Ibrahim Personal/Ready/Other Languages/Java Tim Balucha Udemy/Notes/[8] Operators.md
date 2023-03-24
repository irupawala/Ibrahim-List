# [8.114] Operators Precedence

## Java Operator Precedence Table

| Precedence | Operator                 | Type                                                         | Associativity |
| ---------- | ------------------------ | ------------------------------------------------------------ | ------------- |
| 15         | () [] ·                  | Parentheses Array subscript Member selection                 | Left to Right |
| 14         | ++ --                    | Unary post-increment Unary post-decrement                    | Right to left |
| 13         | ++ -- + - ! ~ ( *type* ) | Unary pre-increment Unary pre-decrement Unary plus Unary minus Unary logical negation Unary bitwise complement Unary type cast | Right to left |
| 12         | * / %                    | Multiplication Division Modulus                              | Left to right |
| 11         | + -                      | Addition Subtraction                                         | Left to right |
| 10         | << >> >>>                | Bitwise left shift Bitwise right shift with sign extension Bitwise right shift with zero extension | Left to right |
| 9          | < <= > >= instanceof     | Relational less than Relational less than or equal Relational greater than Relational greater than or equal Type comparison (objects only) | Left to right |
| 8          | == !=                    | Relational is equal to Relational is not equal to            | Left to right |
| 7          | &                        | Bitwise AND                                                  | Left to right |
| 6          | ^                        | Bitwise exclusive OR                                         | Left to right |
| 5          | \|                       | Bitwise inclusive OR                                         | Left to right |
| 4          | &&                       | Logical AND                                                  | Left to right |
| 3          | \|\|                     | Logical OR                                                   | Left to right |
| 2          | ? :                      | Ternary conditional                                          | Right to left |
| 1          | = += -= *= /= %=         | Assignment Addition assignment Subtraction assignment Multiplication assignment Division assignment Modulus assignment | Right to left |

*Larger number means higher precedence*.

# [8.120] Short Circuit Evaluation

* Short circuit is the situation where the expression does not get evaluated from the second part of the expression when the result is clear from the first part alone.
* In the example below, if statement gets evaluated from the first part before && or || hence it never reaches the second part.

```java
package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        int a = 12;
        int b = 6;

//        if (b != 0) {
//            int c = divideTwoNumbers(a, b);
//
//            if (c == 2) {
//                System.out.println("We've found a 2.");
//            }
//        }

        if (b != 0 && divideTwoNumbers(a, b) == 2) {
            System.out.println("We've found a 2.");
        }

        if (b == 0 || divideTwoNumbers(a, b) == 2) {
            System.out.println("We've found a 2.");
        }

    }

    private static int divideTwoNumbers(int x, int y) {
        return x / y;
    }
}
```

