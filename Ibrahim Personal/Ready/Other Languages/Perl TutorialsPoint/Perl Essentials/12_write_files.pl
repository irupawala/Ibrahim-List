#!/usr/bin/perl

use 5.010;
use strict;				
use warnings;
use autodie; # halt if there are problems reading or writing a file

# operators

# read only - <
# write only - >
# append - >>
# read/write - +<
# read/write - +>
# read/append - +>>

my $file = "txt files/employees.txt";
open my $empname, "+>>", $file;	#empname is the file handler
print {$empname}"---End of file---";			
close ($empname);




open empname, "<", $file;			# here empname is the file handler which is used to open this particular file
while (<empname>)				# left and right angle brackets are used to access the file handlers in perl
{
	print "$_";
}
close (empname);