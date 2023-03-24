#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

foreach my $i (0..10) {

	if ($i == 5){
	next; # skips the iteration of 5, that is capable of skipping one iteration
	#last; # terminates the loop at 5
	#continue;
}

	print $i, "\n";
}
