#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# string manipulation with regex


my $words = "the quick rbown fox jumped over the lazy dogs \n";

# $words =~ s/the/a/g;
 $words =~ s/the/a/; # Only first occurence will be replaced without g 
 say $words;




my $str = "ibu";
$str =~ s/^/hello there /;			# This ^ will search the word "world" and place the string in front of the same
say $str;
