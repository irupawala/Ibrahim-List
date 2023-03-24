#!/usr/bin/perl

use strict;				
use warnings;
use 5.010;

# objects in Perl

# Perl is not an Object Oriented Programming Language

# object = data structures
# class = package
# method = subroutine

# call a method using $ objectname->methodname;

sub addobj{				# created subroutine or a method

my $class = shift;			# here class is the variable/object, shift is used to shift everything in the string to left, In OOO classes are meant to contain all sort of different information which can be referenced through different means			
return bless {}, $class;		# bless is used to put the object in the class package, bless here is used as a constructor in c++
	}
	
my $newobj = addobj("Phil");		# call the method or sub-routine here, here we added the object "Phil" to the class using shift and bless
say $newobj;	

# here the result obtained means that we are getting the reference value for the hash value passed to the object, each time we are running $newobj we are adding a newobject which is shifted and then added to the class