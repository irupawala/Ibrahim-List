#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# anaonymous subroutines - the feature of anonymous subroutines is that it gets stored inside different perl variables: scalars, arrays and hashes 

my $mysub = sub {
	say "hello world";
};

$mysub->();
