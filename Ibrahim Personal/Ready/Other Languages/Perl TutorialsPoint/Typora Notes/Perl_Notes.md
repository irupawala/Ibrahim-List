# Perl Notes from Tutorial Point

## [1] Single Quote Vs Double Quotes

There is an important difference in single and double quotes. Only double quotes **interpolate** variables and special characters such as newlines \n, whereas single quote does not interpolate any variable or special character. Check below example where we are using $a as a variable to store a value and later printing that value - 

```perl
#!/usr/bin/perl

$a = 10;
print "Value of a = $a\n";
print 'Value of a = $a\n';
```

This will produce the following result −

```perl
Value of a = 10
Value of a = $a\n$
```

## [2] Escaping Characters

```perl
#!/usr/bin/perl

$result = "This is \"number\"";
print "$result\n";
print "\$result\n";
```

## [3] Perl DataTypes

Perl is a loosely typed language and there is no need to specify a type for your data while using in your program. The Perl interpreter will choose the type based on the context of the data itself.

Perl has three basic data types: scalars, arrays of scalars, and hashes of scalars, also known as associative arrays. Here is a little detail about these data types.

| Sr.No. |                     Types & Description                      |
| :----: | :----------------------------------------------------------: |
|   1    | **Scalar**Scalars are simple variables. They are preceded by a dollar sign ($). A scalar is either a number, a string, or a reference. A reference is actually an address of a variable, which we will see in the upcoming chapters. |
|   2    | **Arrays**Arrays are ordered lists of scalars that you access with a numeric index, which starts with 0. They are preceded by an "at" sign (@). |
|   3    | **Hashes**Hashes are unordered sets of key/value pairs that you access using the keys as subscripts. They are preceded by a percent sign (%). |

## [4] Separate Namespace for each Data Type

**Perl maintains every variable type in a separate namespace. So you can, without fear of conflict, use the same name for a scalar variable, an array, or a hash. This means that $foo and @foo are two different variables.**

## [5] String Literals

| Escape sequence |                       Meaning                       |
| :-------------: | :-------------------------------------------------: |
|       \\        |                      Backslash                      |
|       \'        |                    Single quote                     |
|       \"        |                    Double quote                     |
|       \a        |                    Alert or bell                    |
|       \b        |                      Backspace                      |
|       \f        |                      Form feed                      |
|       \n        |                       Newline                       |
|       \r        |                   Carriage return                   |
|       \t        |                   Horizontal tab                    |
|       \v        |                    Vertical tab                     |
|      \0nn       |           Creates Octal formatted numbers           |
|      \xnn       |       Creates Hexideciamal formatted numbers        |
|       \cX       |     Controls characters, x may be any character     |
|       \u        |         Forces next character to uppercase          |
|       \l        |         Forces next character to lowercase          |
|       \U        |    Forces all following characters to uppercase     |
|       \L        |    Forces all following characters to lowercase     |
|       \Q        | Backslash all following non-alphanumeric characters |
|       \E        |                  End \U, \L, or \Q                  |

## [6] Array Variables

An array is a variable that stores an ordered list of scalar values. Array variables are preceded by an "at" (@) sign. To refer to a single element of an array, you will use the dollar sign ($) with the variable name followed by the index of the element in square brackets.

Here is a simple example of using array variables −

```perl
#!/usr/bin/perl

@ages = (25, 30, 40);             
@names = ("John Paul", "Lisa", "Kumar");

print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";
```

## [7] Hash Variables

A hash is a set of **key/value** pairs. Hash variables are preceded by a percent (%) sign. To refer to a single element of a hash, you will use the hash variable name followed by the "key" associated with the value in curly brackets.

Here is a simple example of using hash variables −

```perl
#!/usr/bin/perl

%data = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);

print "\$data{'John Paul'} = $data{'John Paul'}\n";
print "\$data{'Lisa'} = $data{'Lisa'}\n";
print "\$data{'Kumar'} = $data{'Kumar'}\n";
```

## [8] Variable Context

Perl treats same variable differently based on Context, i.e., situation where a variable is being used. Let's check the following example −

```perl
#!/usr/bin/perl

@names = ('John Paul', 'Lisa', 'Kumar');

@copy = @names;
$size = @names;

print "Given names are : @copy\n";
print "Number of names are : $size\n";
```

## [9] Conditional Statements

| Sr.No. |                   Statement & Description                    |
| :----: | :----------------------------------------------------------: |
|   1    | [if statement](https://www.tutorialspoint.com/perl/perl_if_statement.htm)An **if statement** consists of a boolean expression followed by one or more statements. |
|   2    | [if...else statement](https://www.tutorialspoint.com/perl/perl_if_else_statement.htm)An **if statement** can be followed by an optional **else statement**. |
|   3    | [if...elsif...else statement](https://www.tutorialspoint.com/perl/perl_if_elsif_statement.htm)An **if statement** can be followed by an optional **elsif statement** and then by an optional **else statement**. |
|   4    | [unless statement](https://www.tutorialspoint.com/perl/perl_unless_statement.htm)An **unless statement** consists of a boolean expression followed by one or more statements. |
|   5    | [unless...else statement](https://www.tutorialspoint.com/perl/perl_unless_else_statement.htm)An **unless statement** can be followed by an optional **else statement**. |
|   6    | [unless...elsif..else statement](https://www.tutorialspoint.com/perl/perl_unless_elsif_statement.htm)An **unless statement** can be followed by an optional **elsif statement** and then by an optional **else statement**. |
|   7    | [switch statement](https://www.tutorialspoint.com/perl/perl_switch_statement.htm)With the latest versions of Perl, you can make use of the **switch** statement. which allows a simple way of comparing a variable value against various conditions. |

## [10] Perl Loops

Perl programming language provides the following types of loop to handle the looping requirements.

| Sr.No. |                   Loop Type & Description                    |
| :----: | :----------------------------------------------------------: |
|   1    | [while loop](https://www.tutorialspoint.com/perl/perl_while_loop.htm)Repeats a statement or group of statements while a given condition is true. It tests the condition before executing the loop body. |
|   2    | [until loop](https://www.tutorialspoint.com/perl/perl_until_loop.htm)Repeats a statement or group of statements until a given condition becomes true. It tests the condition before executing the loop body. |
|   3    | [for loop](https://www.tutorialspoint.com/perl/perl_for_loop.htm)Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable. |
|   4    | [foreach loop](https://www.tutorialspoint.com/perl/perl_foreach_loop.htm)The foreach loop iterates over a normal list value and sets the variable VAR to be each element of the list in turn. |
|   5    | [do...while loop](https://www.tutorialspoint.com/perl/perl_do_while_loop.htm)Like a while statement, except that it tests the condition at the end of the loop body |
|   6    | [nested loops](https://www.tutorialspoint.com/perl/perl_nested_loops.htm)You can use one or more loop inside any another while, for or do..while loop. |

## [11] Loop Control Statements

Loop control statements change the execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.

Perl supports the following control statements. Click the following links to check their detail.

| Sr.No. | Control Statement & Description                              |
| :----: | :----------------------------------------------------------- |
|   1    | [next statement](https://www.tutorialspoint.com/perl/perl_next_statement.htm)Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating. |
|   2    | [last statement](https://www.tutorialspoint.com/perl/perl_last_statement.htm)Terminates the loop statement and transfers execution to the statement immediately following the loop. |
|   3    | [continue statement](https://www.tutorialspoint.com/perl/perl_continue_statement.htm)A continue BLOCK, it is always executed just before the conditional is about to be evaluated again. |
|   4    | [redo statement](https://www.tutorialspoint.com/perl/perl_redo_statement.htm)The redo command restarts the loop block without evaluating the conditional again. The continue block, if any, is not executed. |
|   5    | [goto statement](https://www.tutorialspoint.com/perl/perl_goto_statement.htm)Perl supports a goto command with three forms: goto label, goto expr, and goto &name. |

## [12] Escaping Characters

Perl uses the backslash (\) character to escape any type of character that might interfere with our code. Let's take one example where we want to print double quote and $ sign −

```perl
#!/usr/bin/perl

$result = "This is \"number\"";
print "$result\n";
print "\$result\n";
```

This will produce the following result −

```perl
This is "number"
$result
```

