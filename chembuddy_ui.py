#!/usr/bin/env python3

"""GUI Application"""

__author__ = 'Jake Hudson'
__date__ = '11/30/2023'

import tkinter as tk
from tkinter import ttk
from chembuddy_backend import Calculation


class ChemBuddyFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['padding'] = '10 10 10 10'
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        self.energy = tk.DoubleVar()
        self.mass = tk.DoubleVar()
        self.spec = tk.DoubleVar()
        self.temp_fin = tk.DoubleVar()
        self.temp_init = tk.DoubleVar()
        self.type = tk.StringVar()

        self.create_widgets()

    def __str__(self):
        return f'{self.energy}J'

    def calculate_heat(self):
        try:
            mass_val = float(self.mass.get())
            spec_val = float(self.spec.get())
            temp_init_val = float(self.temp_init.get())
            temp_fin_val = float(self.temp_fin.get())
            energy = float(self.energy.get())

            calc = Calculation(mass_val, spec_val, temp_init_val, temp_fin_val, energy)

            energy_result = calc.calc_heat()
            type_result = calc.rxn_type()

            self.energy.set(energy_result)
            self.type.set(type_result)

        except ValueError:
            self.type.set('Invalid input')

    def create_widgets(self):
        mass_label = ttk.Label(self)
        mass_label['text'] = 'Mass in Grams:'
        mass_label.grid(row=0, column=0, sticky=tk.E)

        mass_entry = ttk.Entry(self)
        mass_entry['width'] = 25
        mass_entry['textvariable'] = self.mass
        mass_entry.grid(row=0, column=1)

        spec_label = ttk.Label(self)
        spec_label['text'] = 'S.H.C in kJ/mol:'
        spec_label.grid(row=1, column=0, sticky=tk.E)

        spec_entry = ttk.Entry(self)
        spec_entry['width'] = 25
        spec_entry['textvariable'] = self.spec
        spec_entry.grid(row=1, column=1)

        temp_init_label = ttk.Label(self)
        temp_init_label['text'] = 'Initial Temp (C°/K):'
        temp_init_label.grid(row=2, column=0, sticky=tk.E)

        temp_init_entry = ttk.Entry(self)
        temp_init_entry['width'] = 25
        temp_init_entry['textvariable'] = self.temp_init
        temp_init_entry.grid(row=2, column=1)

        temp_fin_label = ttk.Label(self)
        temp_fin_label['text'] = 'Final Temp (C°/K):'
        temp_fin_label.grid(row=3, column=0, sticky=tk.E)

        temp_fin_entry = ttk.Entry(self)
        temp_fin_entry['width'] = 25
        temp_fin_entry['textvariable'] = self.temp_fin
        temp_fin_entry.grid(row=3, column=1)

        energy_label = ttk.Label(self)
        energy_label['text'] = 'Heat Energy in Joules:'
        energy_label.grid(row=4, column=0, sticky=tk.E)

        energy_output = ttk.Label(self)
        energy_output['width'] = 25
        energy_output['textvariable'] = self.energy
        energy_output['state'] = 'readonly'
        energy_output.grid(row=4, column=1)

        type_label = ttk.Label(self)
        type_label['text'] = 'Reaction Type:'
        type_label.grid(row=5, column=0, sticky=tk.E)

        type_output = ttk.Label(self)
        type_output['width'] = 25
        type_output['textvariable'] = self.type
        type_output['state'] = 'readonly'
        type_output.grid(row=5, column=1)

        button_frame = ttk.Frame(self)
        button_frame.grid(column=2, row=0, rowspan=3)

        calc_button = ttk.Button(button_frame)
        calc_button['text'] = 'Calculate'
        calc_button['command'] = self.calculate_heat
        calc_button.grid(row=0, column=0)

        exit_button = ttk.Button(button_frame)
        exit_button['text'] = 'Exit'
        exit_button['command'] = self.master.destroy
        exit_button.grid(row=2, column=0)

        clear_button = ttk.Button(button_frame)
        clear_button['text'] = 'Clear'
        clear_button['command'] = self.clear_fields
        clear_button.grid(row=1, column=0)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clear_fields(self):
        self.mass.set(0.0)
        self.spec.set(0.0)
        self.temp_init.set(0.0)
        self.temp_fin.set(0.0)
        self.energy.set(0.0)
        self.type.set('')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('ChemBuddy GUI Edition')
    root.geometry('450x180')
    ChemBuddyFrame(root)
    root.mainloop()
