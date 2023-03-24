#!usr/bin/perl

use strict;
use warnings;
use 5.010;
use autodie;

my $directory = "modules";

opendir (my $dir, $directory);

while (my $list = readdir ($dir)) {
	say "$list";
}

closedir($dir);