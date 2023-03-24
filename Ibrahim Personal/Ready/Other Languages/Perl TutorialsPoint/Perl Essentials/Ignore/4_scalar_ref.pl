#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# scalar references - Internal reference used to point to a variable
# meaning just creating alias you are not actually creating any other variable but are pointing to original reference
# can be scalars, arrays or hashes
# saves memory - a reference rather than a copy
# can contain complex data

my $var = 100;
my $ref = \$var;

say $var, "\n", $ref; # note here that the output obtained will be SCALAR <0X2090b1C>, which is the reference we just created but
# we should be able to dereference it to pull the value out this can be done by putting extra sigil, see eg below


say $var, ": ", $$ref; 