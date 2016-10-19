#!/usr/bin/env python

# this code contains the alphabet of changing nucleotide codons (ambiguous and unambiguous) to amino acids

unam_dna_symbol = {"N":["A","G","C","T"],
"B":["C","G","T"],
"D":["A","G","T"],
"H":["A","C","T"],
"V":["A","C","G"],
"K":["G","T"],
"M":["A","C"],
"R":["A","G"],
"Y":["C","T"],
"S":["C","G"],
"W":["T","A"]}

unam_dna_aa = {"GGN":["G","Gly"],
"GCN":["A","Ala"],
"GTN":["V","Val"],
"YTN":["L","Leu"],
"ATH":["I","Ile"],
"CCN":["P","Pro"],
"TTY":["F","Phe"],
"TAY":["Y","Tyr"],
"TGY":["C","Cys"],
"ATG":["M","Met"],
"CAY":["H","His"],
"AAR":["K","Lys"],
"MGN":["R","Arg"],
"TGG":["W","Trp"],
"WSN":["S","Ser"],
"ACN":["T","Thr"],
"GAY":["D","Asp"],
"GAR":["E","Glu"],
"AAY":["N","Asn"],
"CAR":["Q","Gln"]}


aa_tuple = ((("G","Gly","Glycine"),"GGN"),
(("A","Ala","Alanine"),"GCN"),
(("V","Val","Valine"),"GTN"),
(("L","Leu","Leucine"),"YTN"),
(("I","Ile","Isoleucine"),"ATH"),
(("P","Pro","Proline"),"CCN"),
(("F","Phe","Phenylalanine"),"TTY"),
(("Y","Tyr","Tyrosine"),"TAY"),
(("C","Cys","Cysteine"),"TGY"),
(("M","Met","Methionine"),"ATG"),
(("H","His","Histidine"),"CAY"),
(("K","Lys","Lysine"),"AAR"),
(("R","Arg","Arginine"),"MGN"),
(("W","Trp","Tryptophan"),"TGG"),
(("S","Ser","Serine"),"WSN"),
(("T","Thr","Threonine"),"ACN"),
(("D","Asp","Aspartate"),"GAY"),
(("E","Glu","Glutamate"),"GAR"),
(("N","Asn","Asparagine"),"AAY"),
(("Q","Gln","Glutamine"),"CAR"))

nucleotides = "ACGT"
