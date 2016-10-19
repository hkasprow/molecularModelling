#!/usr/bin/env python

from sys import argv

def openFasta(fasta_filename):
    inp = open(fasta_filename, "r").read().splitlines()
    header = inp[0]
    sequence = "".join(inp[1:])
    fasta_dict = {"header":header, "sequence":sequence}
    return fasta_dict

def convertFastaToPir(fasta_entry, seq_type = "", name = "", first_residue = "", start_chain = "", last_residue = "", end_chain = "", protein_name = "", protein_source = "", xray_resolution = "", xray_rfactor = "", interactivePrompt = False, fillLater = False):
    # fillLater is supposed to leave fields signed so the user will know what to write there ( I need to think how to implement it efficiently)
    header = fasta_entry["header"].split()
    sequence = fasta_entry["sequence"]
    sequence_types = {"X":"structureX", "N":"structureN", "M":"structureM", "S":"sequence"}
    if interactivePrompt == False:
        if name == "":
            name = header[0][1:]
        if seq_type == "":
            seq_type_Prompt = raw_input("You need to specify the type of the sequence (X for Xray, N for NMR, M for model, S for target sequence\n").upper()
            seq_type = sequence_types[seq_type_Prompt]
    else:
        name = raw_input("Provide a name:")
        seq_type_Prompt = raw_input("Provide the sequence type (X for Xray, N for NMR, M for model, S for target sequence\n)").upper()
        seq_type = sequence_types[seq_type_Prompt]
        first_residue = raw_input("Provide first residue from the sequence\n")
        start_chain = raw_input("Provide a start chain\n")
        last_residue = raw_input("Provide last residue from the sequence\n")
        end_chain = raw_input("Provide the end chain\n")
        protein_name = raw_input("Provide a name for the protein (optional)\n")
        protein_source = raw_input("Provide the protein source (optional)\n")
        xray_resolution = raw_input("Provide the xray resolution (optional)\n")
        xray_rfactor = raw_input("Provide the xray rfactor (optional) \n")
    header_first_line = ">P1;%s"%name
    if fillLater == False:
        header_second_line = "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s"%(seq_type, name, first_residue, start_chain, last_residue, end_chain, protein_name, protein_source, xray_resolution, xray_rfactor)
    else:
        header_second_line = "sequence type:%s:first residue:start chain:last_residue:end chain:protein name:protein source:xray resoultion:xray factor"%name # this is implemented not in the way I would like it to be
    # print header_first_line
    # print header_second_line
    # print sequence
    return header_first_line, header_second_line, sequence

def savePirFile(header_first_line, header_second_line, sequence, filename):
    out = open(filename, "w")
    print >> out, header_first_line
    print >> out, header_second_line
    print >> out, sequence

fasta_entry = openFasta(argv[1])
# convertFastaToPir(fasta_entry, seq_type="sequence", interactivePrompt = True)
hfl, hsl, seq = convertFastaToPir(fasta_entry, interactivePrompt = True)
savePirFile(hfl, hsl, seq, "new_pir_alignment.pir")
