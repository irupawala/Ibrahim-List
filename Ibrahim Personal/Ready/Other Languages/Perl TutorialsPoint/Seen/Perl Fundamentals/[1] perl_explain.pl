#!/usr/bin/perl		# locates interpretor

use 5.010;		# version
use strict;		# To make sure that we adhere to strict perl programming rules
use warnings;		# return the warnings


my $name = "jamie";	# note here that we don't have to define here the data type like we do in c++ eg int, string, etc
my $num = 100;
my $pi = 3.14;



say $name;
say $num;
say $pi;

# Difference between print and say is say prints newline automatically
print $name, "\n";
print $num, "\n";
print $pi, "\n";
print "\n";