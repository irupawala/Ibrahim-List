#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

#variable scope

package main;			# main package is the global package for any program
my $x = "hello";
say $x;
# say $x, " ", $y;

package new;
my $y = "world";
say $x, " ", $y; 		# The reason being the main package is the global package for any program




=pod
my $i = "hey";



sub mysub {
my $j = " you !";
say $i, $j;	
	}
	
	mysub();
=cut