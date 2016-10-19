#!/usr/bin/env python

from modeller import *
from modeller.automodel import *

env = environ()
# mdl is an abbreviation for model
mdl = automodel(env, alnfile='alignment.ali', knowns='4ah3', sequence='poly1', assess_methods=(assess.DOPE, assess.GA341))

mdl.starting_model = 1
mdl.ending_model = 1
mdl.make()

