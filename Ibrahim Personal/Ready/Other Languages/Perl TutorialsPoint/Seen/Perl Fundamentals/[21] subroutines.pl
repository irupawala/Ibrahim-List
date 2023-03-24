#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# Functions in perl are called subroutine

sub dosomething {			# the function can be declared before or even after the call
	say "Hi";
}

dosomething();		