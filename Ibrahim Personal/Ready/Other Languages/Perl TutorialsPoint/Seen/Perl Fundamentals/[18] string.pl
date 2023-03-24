#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my $var0 = "hello";
my $var1 = "world"; 
print $var0," ", $var1, "\n";		# combines two strings using a comma

# Escape characters:

# \n - newline
# \b - backspace
# \t - horizontal tab
# \v - vertical tab 

# To print a backslash you have to use the same two times


print $var0,"\\",$var1, "\n";	