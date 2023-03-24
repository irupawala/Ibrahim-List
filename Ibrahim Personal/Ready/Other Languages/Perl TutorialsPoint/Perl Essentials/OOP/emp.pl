package modules_any::emp;
use 5.010;
use strict;

sub addemp {
	my $person = shift;						# shift all it does is take the information that's currently in an array and move everything to the left, So everytime we are going to use it 
									# its going to add one and move to the left
	my $newemp = {no => shift, fn => shift, ln => shift};		# $newemp is the array we are creating and inside the braces are the notations which allows one to add three different variables or 
									# three different pieces of information that we are adding to the array, Employee no, first name and last name.
	bless $newemp, $person;						# using bless create the object reference that will turn that into an object or create an object and then we can return an object back to the calling function
	
	return $newemp;
	
	}
	
	1;