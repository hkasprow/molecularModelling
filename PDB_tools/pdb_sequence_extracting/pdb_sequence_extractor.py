#!/usr/bin/env python

from sys import argv
from Bio.PDB import *
from subprocess import call
import re
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

# this thing here does not make sense because it will open file constantly and overwrite it
# def saveFasta(filename, fasta_sequence):
#     out = open(filename, "w")
#     out.write(fasta_sequence)

out_filename = argv[1][:-3]+"fasta"
out = open(out_filename, "w")
p = PDBParser(PERMISSIVE = 1)

filename = argv[1]
structure_id = argv[1][:-4]

structure = p.get_structure(structure_id, filename)
model = structure[0] # this is valid for Xray structure that has no disordered regions, for NMR structure it gives more models, thus it will take the very first one

for chain in model.get_chains():
    # chain_id = chain.get_id()
    residues = chain.get_residues()
    chain_sequence = ""
    res_counter = 0
    for residue in residues: #THIS WHOLE LOOP IS PROBABLY SPAGHETTI AND I SHOULD ALSO MANAGE TO MAKE A FUNCTION OUT OF IT
        restype = residue.get_id()[0]
        resnum = residue.get_id()[1]
        if restype == " ": # probably it would work without this logical conditions because Polypeptide from Bio module would not recognize a residue name (but it could raise an error)
            if res_counter == 0:
                res_counter = resnum
                chain_sequence += Polypeptide.three_to_one(residue.get_resname())
            elif res_counter == resnum:
                chain_sequence += Polypeptide.three_to_one(residue.get_resname())
            elif res_counter != resnum:
                difference = abs(resnum - res_counter) # arbitrary counting from 0 may cause problems here
                chain_sequence += "-"*difference
                res_counter = resnum
            res_counter += 1
    fasta_seq = makeFasta([structure.header["name"], structure.header["structure_method"], structure.get_id(), "chain " + chain.get_id()], chain_sequence)
    saveFile(fasta_seq) # proably I should do this otherwise, so it would create a global variable with whole fasta entry and then save whole fasta entry to file

print "\nSequence saved to file %s\n"%out_filename
out.close()



# to get certain child elements you need to use parent.get_child()
# to get an access id of this child you need to use child.get_id()
# to get an access id of parent you need to use parent.get_id()
# to get key to access given thing, you need to use parent[child.get_id()]
# for example model["A"]
# thus if there is such a loop:
# for chain in model.get_chains(): # this iterates over every element of the model, thus over every chain that is availablae in the model, but returns only values
# chain_id = chain.get_id() # this gets the key for every element of the model
# print model[chain_id] # this allows you to access the value through the key you obtained before

# counter = 1
