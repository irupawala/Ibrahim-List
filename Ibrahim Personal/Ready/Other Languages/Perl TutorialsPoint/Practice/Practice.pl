#!/usr/bin/perl

use 5.12.3;
use strict;
use warnings;

# my @array = (1, 2, 'Hello');
# my @array = qw/This is an array/;
my @array = ("This", "is", "an", "array");

foreach my $i (@array) {
	say $i;
}