#usr/bin/env python
# script for modeler to to perform searching for possible templates for homology
# modelling

from modeller import *
from sys import argv, exit

### CHECK IF CORRECT NUMBER OF ARGUMENTS WERE PASSED TO THE SCRIPT

if len(argv) < 2:
    print """Usage:
    ./build_profile.py target_sequence sequence_set
    """
    exit()

### SET THE ENVIRONMENT

env = environ()

### VARIABLES SECTION

target_sequence = argv[1].split(".") # the file with the target sequence
sequence_set = argv[2].split(".") # the file with sequence set from pdb database
# these files are splitted because it will be easier to access certain data type
# by just getting into the extension
min_seq_len = 30
max_seq_len = 4000

sdb = sequence_db(env)
sdb.read(seq_database_file=argv[2]), seq_database_format=sequence_set[1].upper(),\
chains_list="ALL", minmax_db_seq_len=(min_seq_len,max_seq_len), clean_sequences=True)

sdb.write(seq_database_file=sequence_set[0]+"bin", seq_database_format="BINARY",\
chains_list="ALL")

sdb.read(seq_database_file=sequence_set[0]+".bin", seq_database_format="BINARY",\
chains_list="ALL")

aln = alignment(env)
aln.append(file=argv[1], alignment_format=target_sequence[1], align_codes="ALL")

prf = aln.to_profile()

prf.build(sdb, matrix_offset=-450, rr_file="${LIB}/blosum62.sim.mat",\
gap_penalties_1d=(-500,-50), n_prof_iterations=1, check_profile=False, max_aln_evalue=0.01)

prf.write(file="build_profile.prf", profile_format="TEXT")

aln = prf.to_alignment()
aln.write(file="build_profil.ali", alignment_format="PIR")
