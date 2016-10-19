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

def clearSequenceEntrance(entry_dictionary):
    identifier = entry_dictionary[0]
    header = entry_dictionary[1]
    sequence = entry_dictionary[2][:-1]
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
    cleared_entry = [identifier, header, protein]
    return cleared_entry

# this decision abbout chain splitting should be done for all sequences detected in the file
# so it probably should appear at the beginnign of the file or there should be some loop that will work
# on all the extracted and cleaned sequences

def orderIdentifier(identifier):
    splitted_identifier = identifier.split(";")
    ordered_identifier = {"protein code":splitted_identifier[0], "name":splitted_identifier[1]}
    return ordered_identifier

def orderHeader(header):
    splitted_header = header.split(":")
    ordered_header = {"seq_type":splitted_header[0], "name":splitted_header[1], "first residue":splitted_header[2],\
     "start chain":splitted_header[3], "last residue":splitted_header[4],\
     "end chain":splitted_header[5], "protein name":splitted_header[6],\
     "protein source":splitted_header[7], "xray resolution":splitted_header[8],\
     "xray rfactor":splitted_header[9]}
    return ordered_header

def introduceMutation(entry_dictionary):
    # print "Choose mutation for "
    identifier = entry_dictionary[0]
    header = entry_dictionary[1]
    sequence = entry_dictionary[2] # it will be most probably a dictionary mostly
    new_sequence = {}
    for key in sequence.iterkeys():
        operating_sequence = list(sequence[key]) # now we can operate on list and easily exchange residues
        switch = True
        position = input("Enter position of residue to mutate or press Enter to finish: \n")-1 # because otherwise it will count from 0
        mutated_residue = raw_input("Enter the residue to mutate (one letter code) or press Enter to finish: \n").upper()
        while position != "" or mutated_residue != "":
            if operating_sequence[position] == mutated_residue:
                print "This position already has this residue: %s"%mutated_residue
            else:
                operating_sequence[position] = mutated_residue
            position = input("Enter position of residue to mutate or press Enter to finish: \n")-1
            mutated_residue = raw_input("Enter the residue to mutate (one letter code) or press Enter to finish: \n").upper() # introduce reading of one letter and three letter codes
        new_sequence[key] = "".join(operating_sequence)

def showResidue(entry_dictionary, positions_list):
    """
    This function shows residues which are corresponding to given positions.
    Entry of variables into the functions should be performed in such way:
    showResidue(entry_dictionary, [list, of, positions])
    """
    identifier = entry_dictionary[0]
    header = entry_dictionary[1]
    sequence = entry_dictionary[2]
    counter = len(sequence)
    if counter > 1:
        print "More than one chain detected. From which chain you want to obtain the residue for given position?\n"
        print "Possible chains: \n"
        possible_chains = ""
        for i in sequence.iterkeys(): possible_chains += i; print i,
        chain = raw_input("\n").upper()
        while chain not in possible_chains:
                print "Not a valid entry, please provide a valid chain name\n"
                chain = raw_input("\n").upper()
    else:
        chain = "A"
    print
    print header
    for position in positions_list:
        print "%4d     -    %s"%(position, sequence[chain][position-1]) # position -1 here in order to have correct numbering, not the one starting from 0

def openFasta(fasta_filename):
    inp = open(fasta_filename, "r").read().splitlines()
    header = inp[0]
    sequence = "".join(inp[1:])
    fasta_dict = {"header":header, "sequence":sequence}
    return fasta_dict

def convertFastaToPir(fasta_entry):
    # header = fasta_entry["header"]
    # sequence = fasta_entry["sequence"]
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

cleared_entrance = clearSequenceEntrance(entrance)
print cleared_entrance

showResidue(cleared_entrance, [3,4,5,6,7,8,9,10])

# mutations = introduceMutation(cleared_entrance)
    # probably should be stored as a dictioary with indicators of chains or something
    # header should be also stored as a dictionary with all the fields and indicators
