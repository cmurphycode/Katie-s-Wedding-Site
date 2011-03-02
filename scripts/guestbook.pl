#!/usr/bin/perl
use strict;
use warnings;
use CGI;
my $q = CGI->new();
my $info = "Server: ". $ENV{'SERVER_NAME'} . " Script name: ". $ENV{'SCRIPT_NAME'};
# need to send header otherwise sky will fall on you
print $q->header();
# always get back to user after perl code
print "document.write('Hello world  I am called from HTML page $ENV{'HTTP_REFERER'}');";
print "document.write('$info');";