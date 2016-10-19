#!/usr/bin/env python
#### IMPLEMENT ALSO GRAPHICAL OUTPUT FOR SOME DNA SEQUENCE WHICH WILL ALSO TRANSLATE A CERTAIN LETTER TO CORRESPONDING SET OF NUCLEOTIDES

# I figured out that this is not the best way because it is hard to access the values stored in tuple
# dictionary for a codon and then tuple of variables will be probably better
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

# only for single letter amino acid code
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

def showSymbols():
    """Prints out the explanation for all the symbols of the codon degeneracy"""
    print """
    Symbol | Meaning | Origin of designation
    G       	G	        Guanine
    A       	A              	Adenine
    T	        T	        Thymine
    C	        C               Cytosine
    R  	     G or A         	puRine
    Y	     T or C           	pYrimidine
    M	     A or C           	aMino
    K	     G or T            	Keto
    S	     G or C	        Strong interaction (3 H bonds)
    W	     A or T	        Weak interaction (2 H bonds)
    H	  A or C or T	        not-G, H follows G in the alphabet
    B	  G or T or C	        not-A, B follows A
    V	  G or C or A	        not-T (not-U), V follows U
    D	  G or A or T	        not-C, D follows C
    N  	  G or A or T or C	aNy
    """

def showCodons():
    """Shows which degenrated codons correspond to which amino acid"""
    global aa_tuple
    print "%8s    %9s    %9s          %5s"%("1-Letter", "3-Letters", "Name", "Codon")
    for element in aa_tuple:
        out_line = "%8s    %9s    %14s    %5s"%(element[0][0], element[0][1], element[0][2], element[1])
        print out_line

def reverseTranscription(aa_seq, splitCodons=False):
    """Takes an amino acid sequence as an input and returns string of DNA sequence with taking into account the degenerated codons.
    In order to see what the allocation of symbols for certain codons are, check either 'showSymbols' function or go to http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html
    You may also print a list for codons with degeneracy taken into account with 'showCodons' function"""
    global aa_dict # import the dictionary of aminoacids and corresponding codons into the function
    dna_seq = ""
    for letter in aa_seq:
        dna_seq += aa_dict[letter]
        if splitCodons == True:
            dna_seq += "||"
    return dna_seq

# test sequence of protease from Human rhinovirus

aa_sequence = "AFRPCNVNTKIGNAKCCPFVCGKAVTFKDRSTCSTYNLSSSLHHILEEDKRRRQVVDVMSAIFQGPISLDAPPPPAIADLLQSVRTPRVIKYCQIIMGHPAECQVERDLNIANSIIAIIANIISIAGIIFVIYKLFCSLQGPYSGEPKPKTKVPERRVVAQGPEEEFGRSILKNNTCVITTGNGKFTGLGIHDRILIIPTHADPGREVQVNGVHTKVLDSYDLYNRDGVKLEITVIQLDRNEKFRDIRKYIPETEDDYPECNLALSANQDEPTIIKVGDVVSYGNILLSGNQTARMLKYNYPTKSGYCGGVLYKIGQILGIHVGGNGRDGFSAMLLRSYFTGQIKVNKHATECGLPDIQTIHTPSKTKLQPSVFYDVFPGSKEPAVLTDNDPRLEVNFKEA"

codons = reverseTranscription(aa_sequence)
codons_pretty = reverseTranscription(aa_sequence, True)
print codons_pretty
print len(aa_sequence)
print len(aa_sequence)*3
print len(codons)
print len(codons_pretty)
