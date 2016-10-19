#!/usr/bin/env python

# this code contains mainly function for processing sequences
# UnAmb is a short form for unambiguous
# Amb is a short form for ambiguous
# and the type of alphabet specified in the names of funcitons is always telling which type should be given as an input

from dna_alphabet import *
from protein_alphabet import *

def ReverseTranscriptionUnAmbDNA(aa_seq, splitCodons=False, oneLetter=True): #(aa_seq, splitCodons=False, table=x)
    """Perform a Reverse Transcription of amino acid sequence into corresponding DNA strand, represented however by a set of Ambiguous Codons"""
    global one_aa_unam_dna, three_aa_unam_dna
    dna_seq = ""
    if oneLetter == True:
        for letter in aa_seq:
            dna_seq += one_aa_unam_dna[letter]
            if splitCodons == True:
                dna_seq += "||"
    else:
        for i in range(0, len(aa_seq)+1, 3):
            dna_seq += three_aa_unam_dna[aa_seq[i:i+3]]
    return dna_seq

def ReverseTranscriptionAmbDNA(aa_seq, splitCodons=False, oneLetter=True):
    """Perform a Reverse Transcription of amino acid sequence into set of possible corresponding DNA strands, represented by Unambiguous set of nucleotides"""
    # global one_letter_aa, three_letter_aa
    # dna_seq = ""
    # if oneLetter == True:
    #     for letter in aa_seq:
    #        dna_seq += one_letter_aa[letter]
    pass # I need to think about some convienient storing in this case and also for some conveenient output

def TranscriptionUnAmbDNA(dna_seq, oneLetter=True):
    global unam_dna_aa
    aa_seq = ""
    if oneLetter == True:
        for i in range(0, len(dna_seq)+1, 3):
            aa_seq += unam_dna_aa[dna_seq[i:i+3][0]]
    else:
        for i in range(0, len(dna_seq)+1, 3): # actually I think that we should be substracting here while we are calculating
            aa_seq += unam_dna_aa[dna_seq[i:i+3][1]]
    return aa_seq



def TranscriptionAmbsDNA():
    pass

def ConvertCodonUnAmb(unamCodon):
    """Converts UnAmbiguous type of codon into set of corresponding Ambiguous codons"""
    global unam_dna_symbol, nucleotides
    amCodon = []
    for i in range(0, len(unamCodon)): # iteration on sequence of nucleotides
        letter = unamCodon[i] # single nucleotide
        if letter not in nucleotides: # nucleotides - variable storing standard nucleotides
            amCodon.append(unam_dna_symbol[letter])
        else:
            amCodon.append([letter])
    return amCodon
# here also a better output method should be applied (something with creating like a matrix with 4 rows which will be wrapped)

def ConvertCodonAmb(amCodon):
    """Converts Ambiguous type of codon into a set of possible best matches of UnAmbiguous codons"""
    # this is a bit more complex function to write
    pass

def GetCodon(codon):
    """Let's say that it is an easy and convienient way to format list of lists with nucleoacids into some more readable format, more resembling usual sequence of nucleotides"""
    formatted = [] # first format it so every element has 4 items in it
    for item in codon:
        if len(item) < 4:
            item.extend(" " * (4 -len(item)))
            formatted.append(item)
        else:
            formatted.append(item)
    formatted = zip(*formatted)
    # for row in formatted:
        # print " ".join(row)
    return formatted

##### TESTING SECTION

peptide = "RTATR"
dna = ReverseTranscriptionUnAmbDNA(peptide)
converted = ConvertCodonUnAmb(dna)

# print peptide
# print
# print dna
# print
print converted

# aa_sequence = "AFRPCNVNTKIGNAKCCPFVCGKAVTFKDRSTCSTYNLSSSLHHILEEDKRRRQVVDVMSAIFQGPISLDAPPPPAIADLLQSVRTPRVIKYCQIIMGHPAECQVERDLNIANSIIAIIANIISIAGIIFVIYKLFCSLQGPYSGEPKPKTKVPERRVVAQGPEEEFGRSILKNNTCVITTGNGKFTGLGIHDRILIIPTHADPGREVQVNGVHTKVLDSYDLYNRDGVKLEITVIQLDRNEKFRDIRKYIPETEDDYPECNLALSANQDEPTIIKVGDVVSYGNILLSGNQTARMLKYNYPTKSGYCGGVLYKIGQILGIHVGGNGRDGFSAMLLRSYFTGQIKVNKHATECGLPDIQTIHTPSKTKLQPSVFYDVFPGSKEPAVLTDNDPRLEVNFKEA"
