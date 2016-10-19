#!/usr/bin/env python

from sys import argv
from Bio.PDB import *
import textwrap

def makeFasta(header_list, sequence):
    header = " ; ".join(header_list)# maybe there is actually a more efficient way to do this
    fasta_sequence = ">%s\n%s\n"%(header, textwrap.fill(sequence, width = 80))
    return fasta_sequence

def checkIntegrity(fasta_sequence):
    position_list = []
    sequence = fasta_sequence.split("\n")[1]
    for index in range(0,len(sequence)):
        if sequence[index] == "-":
            position_list.append(str(index+1)) # index+1 because it starts counting from 0s

    if len(position_list) == 0:
        print "The structure probably has no gaps in chains"
    else:
        print "Structure probably has gaps in chains\nPositions which are lacking amino acids:\n%s"%" ".join(position_list)

# I should add here different format options also and some other utilities maybe
def saveFile(fasta_content): # change fasta_content to fasta_sequence ?
    out.write(fasta_content)

alignment_file = open(argv[1], "r").read().splitlines()

sequence1 = ""
sequence2 = ""
counter1 = 0
counter2 = 0

for line in alignment_file:
    if line.startswith("ATOM"):
        splitted_line = line.split()
        residue_name_1 = splitted_line[3]
        residue_nr_1 = splitted_line[4]
        residue_name_2 = splitted_line[-1]
        residue_nr_2 = splitted_line[-2]


        # if residue_nr_1 == residue_nr_2:
        #     sequence1 += Polypeptide.three_to_one(residue_name_1)
        #     sequence2 += Polypeptide.three_to_one(residue_name_2)
        # elif residue_nr_1 < residue_nr_2:
        #     aa_diff =

        sequence1 += Polypeptide.three_to_one(residue_name_1)
        sequence2 += Polypeptide.three_to_one(residue_name_2)

        print "%s   %s   %s   %s"%(residue_name_1, residue_nr_1, residue_name_2, residue_nr_2)

print textwrap.fill(sequence1, width = 80)
print textwrap.fill(sequence2, width = 80)
