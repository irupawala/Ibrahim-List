#!/usr/bin/perl

use 5.010;
use strict;				
use warnings;
use modules::emp;

my $addingemp = addemp modules_any::emp(123, "Cody", "Blackwell");

# Now everytime we call this module the info in the same gets replaced hence we want the case in which the information is stored and whenever we call the module the new info keeps on adding
my @emplist = ();	# array to store (add) new employees, empty array

# Store values for old employee

$emplist[0] = "$addingemp->{no}";
$emplist[1] = "$addingemp->{fn}";
$emplist[2] = "$addingemp->{ln}";

$addingemp = addemp modules_any::emp(456, "Raj", "Chawanda");

# Store values for new employee

$emplist[3] = "$addingemp->{no}";
$emplist[4] = "$addingemp->{fn}";
$emplist[5] = "$addingemp->{ln}";

# Iterate through each value of an array

say "Employees:";
foreach (@emplist) {
	say "$_";
}
