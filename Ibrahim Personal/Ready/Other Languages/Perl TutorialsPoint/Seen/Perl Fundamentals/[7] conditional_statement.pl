#!/usr/bin/perl

use strict;
use warnings;
use 5.010;




# conditional statement
my $age = 64;

# if ($age >= 65) {
	# print "you are retired \n";
# }
# else
# {
	# print "you are young \n";
# }


# Unless statement

unless ($age >= 65) 
{
	print "you are young \n";
}


# # ternaty operator

# $age >= 65 ? print "you are retired \n" :  print "you are young \n";