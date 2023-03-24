#!/usr/bin/perl

use strict;
use warnings;
use 5.010;


sub mysub {
	# my $x=0;
# #	say @_						# @_ will have the value passed to the subroutine
	# foreach my $y (@_) {
	# $x += $y;
# }

my $x = $_[0] + $_[1] + $_[2];
say $x;	
return;
		
}

		
my $z = 10;
mysub(15,10, $z);			# note here that both 15, 10 are passed at the same time and not one by one
