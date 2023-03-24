#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my $var0 = ""; # Empty string to create container to use it later 
print $var0, "\n";

my $var1 = "hello";
print $var1, "\n";

undef $var1;		# undefines the variable and makes it unknown, used for garbage collection
print $var1, "\n";

