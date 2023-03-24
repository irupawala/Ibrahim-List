#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# hashes, a special kind of array
# hashes uses the sigil %

my %emp = (123, "Ibrahim", 456, "Rupawala", 789, "Firoz"); # First value is the key, followed by the value linked to the key
my %data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);

#say $emp{789};
#say $data{'John Paul'};

# say keys and values



=pod
 foreach my $i (keys %emp) {				# Note here that the keyword "keys" is to be used to access the keys from the hashes

 say $i," ",$emp{$i};					# curly braces are used to access the individual element of hashes and not the square braces as in the arrays
	 }
=cut

=pod
for my $i (values %emp) {
	say $i;
}
=cut

=pod
foreach (keys %emp) {				# Note here that the keyword "keys" is to be used to access the keys from the hashes

say $_," ",$emp{$_};					# curly braces are used to access the individual element of hashes and not the square braces as in the arrays
	}
=cut

# Checking for Existence

# if( exists($data{'Lisa'} ) ) {
   # print "Lisa is $data{'Lisa'} years old\n";
# } else {
   # print "I don't know age of Lisa\n";
# }

# Getting the hash size

# my @keys = keys %data;
# my $size = @keys;
# print "1 - Hash size:  is $size\n";



# Add/ delete element

# adding an element to the hash;
$data{'Ali'} = 55;
foreach (keys %data){
	say "$_: $data{$_}";
}
say "";

# delete the same element from the hash;
delete $data{'Ali'};
foreach (keys %data){
	say "$_: $data{$_}";
}
