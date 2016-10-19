#!/usr/bin/env python

from sys import argv
from Bio.Blast import NCBIWWW as nw
from Bio import SeqIO
import time
from subprocess import call
from multiprocessing import Process

def countBLASTtime():
    global p1
    counter = 0
    while p1 == "":
        call(["clear"])
        print "BLAST is currently running for %d seconds"%counter
        time.sleep(1)
        counter += 1
    print "BLAST search done in %d seconds"%counter

# should I do this function in such way or should I think about redirecting it somehow or doing it another way around?

def runBLAST():
# def runBLAST(sequence):
    results = nw.qblast("blastn", "nt", "8332116")
    return results

# I can do this counting time in a tricky way in a while loop

# uncomment it in non-test version
# input_handle = SeqIO.read(argv[1], format="fasta") # here I should make automatic recognition of the file format, probably with regular expression


if __name__ == '__main__':
    p1 = Process(target=runBLAST)
    p2 = Process(target=countBLASTtime)
    p1.start()
    p2.start()
