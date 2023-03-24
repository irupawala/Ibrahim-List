#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# regular expressions

# sets of characters that can be used for decision structures
# comparing or searching for specific patterns
# pattern operators are =~ and !~
# forward slashes are delimeters used to enclose the regular expressions - match operators

# three regex operators:

# match - m//
# substitute - s///
# transliterate (replace) - tr///

# other delimiters can be used e.g., m[]m{}

my $txt = "Ibrahim has a job at Apple as Design Engineer";

if ($txt =~ m/Apple/) {
	say "found the word!";
} else {

say "not found!";
}


