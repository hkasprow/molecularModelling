#!/usr/bin/env python

from sys import argv, exit
from Bio.Blast import NCBIWWW as nw
from Bio import SeqIO
import time
from os.path import isfile
# from subprocess import call
# from multiprocessing import Process

def checkOutputFilename(filename):
    if isfile(filename) == True:
        answer = raw_input("\n\t File '%s' already exists. Overwrite? (y/n)\n"%filename).lower()
        if answer == "n":
            filename = raw_input("\n\t Provide new filename:\n")
        elif answer != "n" and answer != "y":
            print "\n\tProgram did not recognize the answer. Program will shut down.\n" # add while loop and wait for correct response
            exit()
    return filename

if len(argv) < 3:
    print """Usage:
    ./blast_sender.py GI_number file_name_for_results
    """
    exit()

output_filename = checkOutputFilename(argv[2])

# add receiving CDD webpage link
# and counting time from start

print "\n\tBLAST runs now:\n"
result_handle = nw.qblast("blastn", "nt", argv[1])

save_file = open(output_filename, "w")
save_file.write(result_handle.read()) # it will save it in xml, this is the default format for BioPython

save_file.close()
result_handle.close()
