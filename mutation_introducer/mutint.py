#!/usr/bin/env python

from sys import argv, exit

def convertNumbers(seq):
    residue_numbers = {}
    counter_dash = 0
    counter_aa = 0
    for letter in seq:
        counter_dash += 1
        if letter != "-":
            counter_aa += 1
            residue_numbers[counter_aa] = counter_dash
    return residue_numbers

def clearSequenceEntrance(sequence):
    sequence = sequence[:-1]
    protein = {}
    if "/" in sequence:
        nr_of_chains = sequence.count("/") +1
        split_chains = raw_input("%s chain detected. Would you like to split them? (y/n)\n" % nr_of_chains).upper()
        if split_chains == "Y":
            splitted_sequence = sequence.split("/")
            counter = 1 # counter of chains detected in the protein working on a loop
            for chain_sequence in splitted_sequence:
                chain = raw_input("What name to ascribe to chain number %s?\n" %counter).upper()
                protein[chain] = chain_sequence
                counter += 1
        else:
            protein["A"] = sequence
    return protein

# this decision abbout chain splitting should be done for all sequences detected in the file
# so it probably should appear at the beginnign of the file or there should be some loop that will work
# on all the extracted and cleaned sequences

def orderIdentifier(identifier):
    splitted_identifier = identifier.split(";")
    ordered_identifier = {"protein code":splitted_identifier[0], "name":splitted_identifier[1]}
    return ordered_identifier

def orderHeader(header):
    splitted_header = header.split(":")
    ordered_header = {"type":splitted_header[0], "name":splitted_header[1], "first residue":splitted_header[2],\
     "start chain":splitted_header[3], "last residue":splitted_header[4],\
     "end chain":splitted_header[5], "protein name":splitted_header[6],\
     "protein source":splitted_header[7], "xray resolution":splitted_header[8],\
     "xray rfactor":splitted_header[9]}
    return ordered_header

def introduceMutation(entry_dictionary):
    # print "Choose mutation for "
    pass

# reading pir alignment file with every sequence as single entrance

input_handle = open(argv[1], "r").read().split("\n\n")

for sequence in input_handle:
    splitted_sequence = sequence.split("\n")
    raw_sequence = "".join(splitted_sequence[2:])
    # raw_sequence.replace("*","") # replace last end of the sequence character # I WILL HANDLE THIS LATER IN FUNCTION clearSequenceEntrance
    if len(splitted_sequence) > 3:
        entrance = [orderIdentifier(splitted_sequence[0]), orderHeader(splitted_sequence[1]), raw_sequence]
        print entrance # [line identifier dictionary, header dictionary, sequence]

print entrance[0]
print entrance[1]
print entrance[2][:-1]

cleared_entrance = clearSequenceEntrance(entrance[2])
print cleared_entrance

    # probably should be stored as a dictioary with indicators of chains or something
    # header should be also stored as a dictionary with all the fields and indicators
