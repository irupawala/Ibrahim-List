#!/usr/bin/perl

use strict;
use warnings;
use 5.12.3;

sub sum {
	
	my $x = 0;
	# foreach my $y (@_)
	# {
		# $x = $x + $y;
	# }
	
	$x = $_[0] + $_[1] + $_[2];
	return $x;
	
}


say sum(5, 10, 20);