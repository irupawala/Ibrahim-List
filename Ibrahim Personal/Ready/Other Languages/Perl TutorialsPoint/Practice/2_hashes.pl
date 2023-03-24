#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my %my_hash = (1, "Ibrahim", 2, "works", 3, "at", 4, "apple");

#say $my_hash{1};

foreach my $i (keys %my_hash) {
say $i, " ",$my_hash{$i};	
	}



