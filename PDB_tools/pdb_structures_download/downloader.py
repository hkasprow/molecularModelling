#!/usr/bin/env python

from sys import argv, exit
import getopt
from subprocess import call
from Bio.PDB import PDBList

if len(argv) < 2:
    print """Usage:
    ./pdb_downloader.py options pdb_codes_separated_by_space
    """
    exit()

# the class already checks if the file exists, but it looks for *.ent file named like the class preferrs it, so I should probably add my function that checks if there is a certain file exisiting in that directory and then eventually check if it is the same file and add option to overwrite it

# this needs to be added later on
# shortop = "hdc"
# longop = ["help","directory","compress"]

# SET
# default folder
# specification of different directory
# compression option

codel = [x.upper() for x in argv[1:]]
pdirValue = "."

pdbl = PDBList()
for entry in codel:
    pdbl.retrieve_pdb_file(entry, pdir=pdirValue)
    path = pdirValue
    if path.endswith("/"):
        path = path[:-1]
    call(["mv","%s/pdb%s.ent"%(path, entry.lower()),"%s/%s.pdb"%(path, entry.lower())]) # renames from the weird name to more convenient and more known from pdb webpage
    # I should add here that it would specify the direct path to the file
