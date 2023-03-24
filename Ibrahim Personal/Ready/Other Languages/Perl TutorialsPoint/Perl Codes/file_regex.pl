#!/usr/bin/perl;

use warnings;
use strict;
use 5.010;

print "Enter the direcotry/path: ";
my $directory = <STDIN>;
chomp $directory; 

my $prompt1;
my $in_word;
opendir (my $dir, $directory) or die "No such directory exist $! \n";

print "Enter the filename: ";
my $file = <STDIN>;
chomp $file;
 
my $file_in = "$directory/$file";
my $fh;
open $fh, '+<', $file_in or die $!;


print "Enter the word to be searched : ";
my $word = <STDIN>;
chomp $word;

while (<$fh>)
{
if (m/$word/)
	{
	print "word found, do you want to change the same (y/n)? \n";
	$prompt1 = <STDIN>;
	chomp $prompt1;
	if ($prompt1 eq "y")
	{
		print "Enter the new word to be inputted: ";
		$in_word = <STDIN>;
		chomp $in_word;
		print $_ =~ s/$word/$in_word/g;
		#print "$_\n";
		print "Success \n";
		
	}
	elsif ($prompt1 eq "n")
	{
		print "Ok \n";
	}
else
	{
	print "word not found \n";
	}
}
}

closedir ($dir);
if ($fh)
{
	close($fh);
}

