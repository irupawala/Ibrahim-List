#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# array references
# Internal reference used to point to a variable
# can be scalars, arrays or hashes
# saves memory - a reference rather than a copy
# can contain complex data

# referencing
my $array = ["pencil", "pen", "paper"];		# note here that for the array we are using sigil $ and not @, Also we are using [] brackets instead of ().
say $array;

my @normal_array = ("pencil", "pen", "paper");	

# dereferencing

say $array->[2];

say $normal_array[2];



