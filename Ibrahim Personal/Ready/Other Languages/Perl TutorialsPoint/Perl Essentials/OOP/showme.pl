package sub_directory::showme;		# here sub_directory is the name of the sub-directory whereas showme is the name of the module

use strict;				
use warnings;
use 5.010;

say "This is my module!";

1;		# The last part of any module must have positive value in it, that is a true value, as long as it is not 0 perl will see the same as true value and know that the module has been completed


"I'm done";	# This won't display anything but it represents a string which is a also a true value

