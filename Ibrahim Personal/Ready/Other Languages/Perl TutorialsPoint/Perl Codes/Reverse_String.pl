#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

say "Enter the string";
my $input_string = <STDIN>;

chomp $input_string;
my $len = length($input_string);
my @string = split('', $input_string);
my $converted_string = "";

for (my $i = $len-1; $i >=0; $i--) {
	#say $string[$i];
	$converted_string = $converted_string.$string[$i];
}


say $converted_string;
	













