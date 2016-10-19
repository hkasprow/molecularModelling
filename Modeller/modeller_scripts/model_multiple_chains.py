#!/usr/bin/env python

from modeller import *
from modeller.automodel import *
from sys import argv

log.verbose()

class Model(automodel):
    def special_restraints(self, aln):
        s1 = selection(self.chains['A']).only_atom_types('CA')
        s2 = selection(self.chains['C']).only_atom_types('CA')
        self.restraints.symmetry.append(symmetry(s1, s2, 1.0))
    def user_after_single_model(self):
        self.restraints.symmetry.report(1.0)

env = environ()

mdl = automodel(env, alnfile='alignment.ali', knowns='4ah3', sequence=argv[1], assess_methods=(assess.DOPE, assess.GA341))

mdl.starting_model = 1
mdl.ending_model = 1
mdl.make()
