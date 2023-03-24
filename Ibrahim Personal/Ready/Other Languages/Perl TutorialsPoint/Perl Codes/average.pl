
#!/usr/bin/perl

use strict;
use warnings;
#use 5.010;

print "Enter the number of Inputs: ";
my $no = <STDIN>;
my $in = 0;

print "Enter all the Inputs: ";
foreach (1..$no) {
$in += <STDIN>;
}


my $avg = $in / $no;
print "average = ", $avg, "\n";

=pod
#!/usr/bin/perl
use warnings;
use strict;

my $sum = 0;
my $n = 0;
while (<>) {
    $sum += $_;
    $n++;
}
print $sum/$n, "\n";
=cut