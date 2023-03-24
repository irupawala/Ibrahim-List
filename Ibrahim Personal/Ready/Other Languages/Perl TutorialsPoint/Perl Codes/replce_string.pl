#!/usr/bin/perl;

use warnings;
use strict;
use 5.010;

my $str = "I am all the way up !! I am ";
$str =~ s/I/II/;
print $str, "\n";
