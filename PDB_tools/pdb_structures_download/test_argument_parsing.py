#!/usr/bin/env python

from sys import argv
import getopt

shortopt = "vhe:"
longopt = ["verbose", "help", "encoding="]

opts, args = getopt.getopt(argv[1:], shortopt, longopt)

print "opts = ", opts
print "args = ", args
