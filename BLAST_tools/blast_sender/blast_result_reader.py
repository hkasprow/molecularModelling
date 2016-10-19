#!/usr/bin/env python

# reading xml blast results handle

from sys import argv
from Bio.Blast import NCBIWWW as nwww
from Bio.Blast import NCBIXML as nxml
from Bio import SeqIO

result_handle = open(argv[1])
blast_records = nxml.parse(result_handle)

for i in result_handle:
	print i
