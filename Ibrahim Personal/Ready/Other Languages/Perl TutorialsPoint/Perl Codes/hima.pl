#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

print "Enter the first word : ";
my $word1 = <STDIN>;
  chomp $word1;
 # print $word;
 
 print "Enter the second word : ";
my $word2 = <STDIN>;
  chomp $word2;
 
 

my $reverse = reverse $word1;


if ($word2 eq $reverse) {
	print "Hima \n";
}
else {
	print "F Hima \n";
}
