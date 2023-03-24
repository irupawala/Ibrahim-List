#!/usr/bin/perl

use strict;
use warnings;
use 5.010;


# Example of Conversion

=pod
my $i = "hello";
say $i;

$i = 100;
say $i;
=cut

# Example of Coercion through comparison

# my $i = 100;
# my $k = "hello";
# if ($i > $k) {
	# say "greater than";
# }

# Example of Coercion of adding two values even though not of the same type

# say "50" + 2;


# Example of Coercion

my $i = "1";
my $k = "2";

say $i, $k;
my $l = $i + $k;
say $l;

