#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# state variable 

	

sub mysub {
	
	state $y = 10;				# state is used to store the value of the variable in the memory
	#my $y = 10;
	$y += 10;
	say $y;
	
	}
	
	
mysub();
mysub();
mysub();
mysub();
mysub();
