#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# regular expressions

# escape sequence expressions
# \t tab
# \n newline
# \r return
# \xhh hex character

my $words = "the quick rbown fox jumped over the lazy dogs \n";


if ($words =~ /\n/) {
	say "match";
}
else
{
say "no match!";
}





# my @test = split(" ", $words);		# here note that function split is used to create the array @test splitting the $words whereever space is found

 # say scalar @test;
 # #say $test[0];

# foreach (@test) {
	# say "$_";			# $_ will pull out the result each time it loops through meaning it will show us the result of each of those 9 instances or 9 iterations
					# # note that in cpp we should use for loop for iterating through the array with an integer i
# }




