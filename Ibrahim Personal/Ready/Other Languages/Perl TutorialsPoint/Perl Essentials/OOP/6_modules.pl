#!/usr/bin/perl

use strict;				# strict and warnings are also modules
use warnings;
use 5.010;
use Digest::MD5 'md5_hex';		# MD5 algo is Encryption method to convert string into hex code

# Perl modules: Functions can be added which are not already present in perl interpretor
# functions from vast library
# reusable
# over 108,000 modules downloadable
# http://learn.perl.org/modules/

# some are already built-in modules

say md5_hex("hello world");