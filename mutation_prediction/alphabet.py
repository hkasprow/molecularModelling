#!/usr/bin/env python
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

aa_dict = {"G":"GGN","A":"GCN","V":"GTN","L":"YTN","I":"ATH","P":"CCN","F":"TTY","Y":"TAY","C":"TGY","M":"ATG","H":"CAY","K":"AAR","R":"MGN","W":"TGG","S":"WSN","T":"ACN","D":"GAY","E":"GAR","N":"AAY","Q":"CAR","B":"RAY","Z":"SAR",".":"TRR","X":"NNN"}

letter_dict = {"N":("A","G","C","T"),
"B":("C","G","T"),
"D":("A","G","T"),
"H":("A","C","T"),
"V":("A","C","G"),
"K":("G","T"),
"M":("A","C"),
"R":("A","G"),
"Y":("C","T"),
"S":("C","G"),
"W":("T","A")}

nucleotides = "ACGT"
