#!/usr/bin/perl

use 5.010;
use strict;				
use warnings;

=pod
my $directory = "modules";

opendir (my $dir,$directory) or die $!;		# here $dir is the new variable we have created, here or die halts the operation if there is any kind of error like if the files didn't exists

while (readdir ($dir)) {
	
	say "$_";
	}
	
# while (my $list = readdir ($dir)) {
	
	# say "$list";
	# }
	
 closedir ($dir)			
=cut




my $directory = "modules";

opendir (my $dir,$directory) or die $!;

while (readdir ($dir))
{
	say "$_";
}

closedir ($dir)

