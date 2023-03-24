#!/usr/bin/perl

use strict;
use warnings;
use 5.010;
# use 5.12.3;

my $ops = 0;
# arithmetic operators
say "Examples";
say "addition: ", $ops = 10+10;
say "subtraction: ", $ops = 100-10;
say "multiplication: ", $ops = 10*10;
say "division: ", $ops = 10/10;
say "exponenet: ", $ops = 10**2;				# ** is exponent here
say "modulo: ", $ops = 11 % 3, "\n\n"; 			

undef $ops;

# assignment operators
my $ops = 0;
say "+=: ", $ops+=5;
say "-=: ", $ops-=1;
say "*=: ", $ops*=2;
say "/=: ", $ops/=2;
say "**=: ", $ops**=2;
say "%=: ", $ops%=3, "\n\n"; 	

undef $ops;

# Unary operators
my $ops = 10;

say "++before: ", ++$ops; 
say "++after: ", $ops++; 		
say "--before: ", --$ops; 
say "--after: ", $ops--; 
say "final value: ", $ops;

undef $ops;