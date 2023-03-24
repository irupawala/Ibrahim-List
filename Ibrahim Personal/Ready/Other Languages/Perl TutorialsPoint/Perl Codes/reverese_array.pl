#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

print "Enter the number of elements in an array: ";
my $no = <STDIN>;
my @ary;
my @out;

print "Enter the elements of an array: \n";
foreach my $i (0..($no-1)) {
	 $ary[$i] = <STDIN>;
}

print "The input array is: \n\n";
foreach my $i (0..($no-1)) {
	print "Value at index ", $i, " is ", $ary[$i];
}

for (my $i = 0; $i < $no; $i++) {
	$out[$no-($i+1)] = $ary[$i];
}

print "\nThe output array is: \n\n";
foreach my $i (0..($no-1)) {
	print "Value at index ", $i, " is ", $out[$i];
}