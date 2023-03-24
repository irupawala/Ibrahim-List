#!/usr/bin/perl

use 5.010;
use strict;				
use warnings;
use modules::emp;

my $addingemp = addemp modules_any::emp(123, "Cody", "Blackwell");

# Display values for new employee
say "$addingemp->{no}";
say "$addingemp->{fn}";
say "$addingemp->{ln}";

say $addingemp;			# the result obtained from this will be object references that we have created

use Data::Dumper;		# To retrieve the information in the object we use something called data dumper, all this does is access the module called dumper and we're going to use that to dump the data from the variable $addemp
say Dumper (\$addingemp);