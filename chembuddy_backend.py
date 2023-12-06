#!/usr/bin/env python3

"""Backend module for ChemBuddy GUI Edition"""

__author__ = 'Jake Hudson'
__date__ = '12/2/2023'


class Calculation:
    def __init__(self, mass, spec, temp_init, temp_fin, energy):
        self.mass = mass
        self.spec = spec
        self.temp_init = temp_init
        self.temp_fin = temp_fin
        self.energy = energy

    def calc_heat(self):
        self.energy = (self.mass * self.spec * (self.temp_fin - self.temp_init))
        return self.energy

    def rxn_type(self):
        if self.energy > 0:
            return 'Endothermic'
        elif self.energy < 0:
            return 'Exothermic'
        else:
            return 'Null'
