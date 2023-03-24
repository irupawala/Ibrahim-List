#!/usr/bin/perl

use strict;
use warnings;
use 5.010;
#use autodie;

print "Enter the direcotry/path: ";
my $directory = <STDIN>;  	# same as cout for prompting user;
chomp $directory; 		


opendir (my $dir, $directory) or die $!, "\n";		# file handler needed for opening directory as well

print "The contents of your current directory are: \n";

while (readdir ($dir) ) {
	say "$_";
}


print "Enter the filename alongwith extension: ";
my $filename = <STDIN>;
chomp $filename;
# my $fn = "$directory/$filename";
# chomp $fn;
my $fh;
my $existing_file;
my $exfh;
my $prompt;
my $prompt1;

if ( -e "$directory/$filename") {		# searches for a specific file in a directory
	$existing_file = "$directory/$filename";		
	print "File Exists, the contents of the same are: \n";
	open $exfh, "<",$existing_file or die $!, "\n";
	while (<$exfh>)				# used for accessing file handlers in perl
	{
	print "$_";
	}
close ($exfh);
	print "Do you want to delete the same (y/n)? \n";
	$prompt = <STDIN>;
	chomp $prompt;
			if ($prompt eq "y")
			{
			print "File has been deleted \n";
			unlink $existing_file;		# command used to delete a particular file
			}
			elsif($prompt eq "n") 
			{
			print "File is preserved \n";
			}
	
				} 

else
{
	print "File does not exist, do you want to create a newone (y/n)? \n";
	$prompt1 = <STDIN>;
	chomp $prompt1;
	if ($prompt1 eq "n")
	{
		print "OK \n"
	}
	elsif ($prompt1 eq "y")
	{
	open $fh, "+>", "$directory/$filename" or die $!, "\n";
	print "Enter the message to be typed in that file: \n";
	my $msg = <STDIN>;
			if ($msg eq "\n") {	
			exit;
			}
			else {
			print "Success, Entered your message in the file \n";
			print {$fh}$msg;		# way to write a code in a file
			}
	
	}
	
	closedir($dir);
	if ($fh) 
	{
	close ($fh);
	}
}