#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

=pod
# my @fruit = ("apple", "orange", "banana");
# foreach my $i (@fruit) {
	# say $i;
# }

my @fruit = ("apple", "orange", "banana");
foreach (@fruit) {
	 say $_;
 }

# my @fruit = ("apple", "orange", "banana");

	# say @fruit;

# add element to array
=cut



my @fruit = ("apple ", "orange ", "banana ");
$fruit[3] = "kiwi ";
$fruit[0] = "grapes ";
say @fruit;
say scalar @fruit;					# scalar displays the number of elements in an array




