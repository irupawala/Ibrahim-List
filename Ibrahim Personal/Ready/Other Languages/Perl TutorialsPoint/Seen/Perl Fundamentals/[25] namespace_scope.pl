#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

# default namespace in perl is main

# To create a namespace we have to use command package

=pod
package main; 
say hello::sayit();             # say to call the sub-routine or to print something
say world::sayit();
=cut

# main namespace is optional
say hello::sayit();
say world::sayit();

# new namespace called hello
package hello;
sub sayit {			# sub to create a sub - routine
	return "hello";
}


# new namespace called hello	
package world;
sub sayit {
	return "world";
}

=pod
	
# main namespace can also be at the end	
package main;
say hello::sayit();
say world::sayit();	

=cut