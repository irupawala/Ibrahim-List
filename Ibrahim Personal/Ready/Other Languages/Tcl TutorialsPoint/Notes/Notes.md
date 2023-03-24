# [1] Basic Syntax

## First Program

```tcl
#!/usr/bin/tclsh

# This is comment

if 0 {
This is multiline comment in TCL
}

puts "Hello World";
puts stdout "Hello, world!" # Here, stdout makes the program to print in the standard output device.
```

## Whitespace in Tcl

Whitespace is the term used in Tcl to describe blanks, tabs, newline characters, and comments. Whitespace separates one part of a statement from another and enables the interpreter to identify where one element in a statement, such as puts, ends and the next element begins

```tcl
#!/usr/bin/tclsh

puts "Hello World!" 
```

## Command Substitution

In command substitutions, square brackets are used to evaluate the scripts inside the square brackets. A simple example to add two numbers is shown below −

```tcl
#!/usr/bin/tclsh

puts [expr 1 + 6 + 9]
```

## Variable Substitution

In variable substitutions, $ is used before the variable name and this returns the contents of the variable. A simple example to set a value to a variable and print it is shown below.

```tcl
#!/usr/bin/tclsh

set a 3
puts $a
```

The above statement will create a variable name a and stores it as a string even though, we have not used double quotations. Now, if we try to make an arithmetic on the variable, it is automatically turned to an integer. A simple example is shown below −

```tcl
#!/usr/bin/tclsh

set myVariable 18
puts [expr $myVariable + 6 + 9]
```

# [2] Data Types

## String Representations

The primitive data-type of Tcl is string and often we can find quotes on Tcl as string only language.

Unlike other languages, in Tcl, you need not include double quotes when it's only a single word. An example can be −

```tcl
#!/usr/bin/tclsh

set myVariable hello
puts $myVariable
```

When we want to represent multiple strings, we can use either double quotes or curly braces. It is shown below −

```tcl
#!/usr/bin/tclsh

set myVariable "hello world"
puts $myVariable
set myVariable {hello world}
puts $myVariable
```

## List

```tcl
#!/usr/bin/tclsh

set myVariable {red green blue}
puts [lindex $myVariable 2]
set myVariable "red green blue"
puts [lindex $myVariable 1]
```

## Associative Array

Associative arrays have an index (key) that is not necessarily an integer. It is generally a string that acts like key value pairs. A simple example is shown below −

```tcl
#!/usr/bin/tclsh

set  marks(english) 80
puts $marks(english)
set  marks(mathematics) 90
puts $marks(mathematics)
```

## Handles

Tcl handles are commonly used to represent files and graphics objects. These can include handles to network requests and also other channels like serial port communication, sockets, or I/O devices. The following is an example where a file handle is created.

```tcl
set myfile [open "filename" r]
```

# [3] Variables

## Dynamic Typing

Tcl is a dynamically typed language. The value of the variable can be dynamically converted to the required type when required. For example, a number 5 that is stored as string will be converted to number when doing an arithmetic operation. It is shown below −

```tcl
#!/usr/bin/tclsh

set variableA "10"
puts $variableA
set sum [expr $variableA +20];
puts $sum
```

## Mathematical Expressions

As you can see in the above example, expr is used for representing mathematical expression. The default precision of Tcl is 12 digits. In order to get floating point results, we should add at least a single decimal digit. A simple example explains the above.

```tcl
#!/usr/bin/tclsh

set variableA "10"
set result [expr $variableA / 9];
puts $result
set result [expr $variableA / 9.0];
puts $result
set variableA "10.0"
set result [expr $variableA / 9];
puts $result
```

# [4] Operators

https://www.tutorialspoint.com/tcl-tk/tcl_operators.htm

