#!/usr/bin/env python

# POVme configuration file creator

import math
from Tkinter import *
import Pmw
from pymol import cmd
import sys


def __init__(self):
    self.menuBar.addmenuitem("Plugin", "command",\
    "POVme 2.0 PyMol Plugin",\
    command = lambda s=self : PovConfSet(s))


class PovConfSet:

    def pop_error(self, msg):
        error_dialog = Pmw.MessageDialog(self.parent, title = "Error", message_text = msg)

    def showCrisscross(self):
        startpoint = (float(self.xlocvar.get()), float(self.ylocvar.get()), float(self.zlocvar.get()))
        cmd.delete("crisscross")
        self.crisscross(startpoint[0], startpoint[1], startpoint[2], 0.5, "crisscross")

    def getAtoms(self, selection="(all)"):
        return cmd.identify(selection, 0)

    def getResids(self, selection="(all)"):
        stored.list=[]
        cmd.iterate(selection, "stored.list.append((resi, chain))")
        return set(stored.list)

    def getObjectName(self, selection="(all)"):
        pairs = cmd.identify(selection, 1)
        name = None
        names = set([])
        for p in pairs:
            names.add(p[0])
        if len(names) == 0:
            self.pop_error("Selection is empty")
        elif len(names) == 1:
            name = names.pop()
        else:
            s = "Active site selection needs to be limited to one object!"
            for n in names:
                s += n + " "
            self.pop_error(s)
        return name

    def compute_center(self, selection="(all)"):
        if not selection in cmd.get_names("selections") and not selection in cmd.get_names("objects"):
            self.pop_error("Selection '%s' does not exist, using all atoms."%selection)
            selection = "all"
        object = self.getObjectName(selection)
        if object == None:
            return None
        Ts = []
        residues = self.getResids(selection)
        atoms = self.getAtoms(selection)
        for residue in residues:
            r_sele = "resi %s and chain %s and object %s"%(str(r[0]), r[1], object)
            residue_atoms = self.getAtoms(r_sel)
            all = []
            for atom in residue_atoms:
                if atom in atoms:
                    all = all + [atom]
            if len(all) == len(residue_atoms):
                Ts = Ts + [self.computecenterRA(r_sel)]
            else:
                for atom in all:
                    Ts = Ts + [self.computecenterRA("id %s and object %s"%(str(a), object))]

        sumx = 0
        sumy = 0
        sumz = 0
        if len(Ts) == 0:
            return (0, 0, 0)
        l = len(Ts)
        for center in Ts:
            sumx += center[0]
            sumy += center[1]
            sumz += center[2]
        return (sumx/l, sumy/l, sumz/l)

    def computecenterRA(self, selection="(all)"):
        stored.xyz = []
        cmd.iterate_state(1, selection, "stored.xyz.append([x, y, z])")
        centx = 0
        centy = 0
        centz = 0
        cnt = 0
        for atom in stored.xyz:
            centx += atom[0]
            centy += atom[1]
            centz += atom[2]
            cnt += 1
        centx/=cnt
        centy/=cnt
        centz/=cnt
        return (centx, centy, centz)

    def computecenter(self, selection="(all)"):
        gcentx = 0
        gcenty = 0
        gcentz = 0
        gcnt = 0
        for selstr in selection.split():
            sel = cmd.get_model(selstr)

            centx = 0
            centy = 0
            centz = 0
            cnt = len(sel.atom)
            if (cnt == 0):
                print "Selection used to compute center of active site is empty"
                return (0, 0, 0)
            for atom in sel.atom:
                centx += atom.coord[0]
                centy += atom.coord[1]
                centz += atom.coord[2]
            centx/=cnt
            centy/=cnt
            centz/=cnt

            gcentx += centx
            gcenty += centy
            gcentz += centz
            gcnt += 1

        gcentx/=gcnt
        gcenty/=gcnt
        gcentz/=gcnt

        return (gcentx, gcenty, gcentz)

    def crisscross(self, x, y, z, d, name="crisscross"):

        obj = [
        LINEWIDTH, 3,

        BEGIN, LINE_STRIP,
        VERTEX, float(x-d), float(y), float(z),
        VERTEX, float(x+d), flaot(y), float(z),
        END,

        BEGIN, LINE_STRIP,
        VERTEX, float(x), float(y-d), float(z),
        VERTEX, float(x), float(y+d), float(z),
        END,

        BEGIN, LINE_STRIP,
        VERTEX, float(x), float(y), float(z-d),
        VERTEX, float(x), float(y), float(z+d),
        END

        ]
        view = cmd.get_view()
        cmd.load_cgo(obj, name)
        cmd.set_view(view)
