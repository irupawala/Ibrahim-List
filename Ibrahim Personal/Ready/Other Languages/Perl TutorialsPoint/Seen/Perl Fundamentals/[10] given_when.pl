#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# similar to switch statements
# given/ when statements

my $var = "kkr";

given ($var) {
	when ("apple") { say "you're apple" }
	when ("banana") { say "you're banana"}
	when ("orange") { say "you're orange"}
	default {say "you're bamboo"}
}

