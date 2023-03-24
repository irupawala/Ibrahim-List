#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my @fruit = ("apples ", "oranges ", "banana ");

#push
#push @fruit, "cherry ";			# push adds the element to the end of the array
#say @fruit

# pop

# pop @fruit;			# removes the last character of an array
# say @fruit		

# shift

# shift @fruit;		# removes the first character of an array
# say @fruit;		

# unshift

# unshift @fruit, "grapes ";
# say @fruit;

	

# splice

=pod
say @fruit;
splice @fruit, 0, 1, "peach ";	# first value is the offset meaning the action will be done after this many positions, second value is used for either to insert value (use 0) or to replace value (use 1)
say @fruit;
splice @fruit, 1, 0, "peach ";
say @fruit;
=cut


# syntax from tutorialspoint
# splice @ARRAY, OFFSET [ , LENGTH [ , LIST ] ]
# my @nums = (1..20);
# print "Before - @nums\n";

# splice(@nums, 5, 1, 21..25); 
# print "After - @nums\n";

# slice 

# say @fruit;
# say @fruit[0,1];		# note that slice is not a keyword like push and splice	




# Split and Join

# my $var_string = "Rain-Drops-On-Roses-And-Whiskers-On-Kittens";
# my $var_names = "Larry,David,Roger,Ken,Michael,Tom";

# # transform above strings into arrays.
# my @string = split('-', $var_string);
# my @names  = split(',', $var_names);

# my $string1 = join( '-', @string );
# my $string2 = join( ',', @names );

# print "$string1\n";
# print "$string2\n";


# Sorting Arrays


# # define an array
# my @foods = qw(pizza steak chicken burgers);
# print "Before: @foods\n";

# # sort this array
# @foods = sort(@foods);
# print "After: @foods\n";


# Merging Arrays

my @odd = (1,3,5);
my @even = (2, 4, 6);

my @numbers = (@odd, @even);

print "numbers = @numbers\n";