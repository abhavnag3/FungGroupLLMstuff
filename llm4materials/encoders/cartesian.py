from ase import Atoms
from ase.cell import Cell
class Cartesian:
    def __init__(self):
        pass

    def encode(self, atoms):
        # TO-DO
        # given an Atoms object
        # return a Cartesian text representation of
        # the crystal

        # example output string:
        # 5.1 5.1 5.1
        # 60 60 60
        # Pm
        # 0.25 0.25 0.25
        # Pm
        # 0.75 0.75 0.75
        # Zn
        # 0.00 0.00 0.00
        # Rh
        # 0.50 0.50 0.50

        cif_string = ""
        # complete this function

        lattice_lengths = atoms.cell.cellpar()[:3]
        lattice_angles = atoms.cell.cellpar()[3:]

        cif_string += ' '.join(map(str, lattice_lengths))
        cif_string += '\n'
        cif_string += ' '.join(map(str, lattice_angles))
        cif_string += "\n"

        atom_symbols = atoms.get_chemical_symbols()
        atom_fc = atoms.get_scaled_positions()

        symb_and_coord = []

        for i in range(len(atom_symbols)):
            cif_string += atom_symbols[i]
            cif_string += "\n"
            cif_string += ' '.join(map(str, atom_fc[i]))
            cif_string += "\n"
        return cif_string
    
    def decode(self, string):
        # TO-DO
        # given a Cartesian string representation 
        # return an Atoms object
        lines = string.strip().split("\n") #seperate each line in the string
        lattice_lengths = list(map(float, lines[0].split())) #get lattice_lengths
        lattice_angles = list(map(float, lines[1].split()))

        cell = Cell.fromcellpar(lattice_lengths + lattice_angles)
        atom_symb = []
        atom_pos = []

        for i in range(2, len(lines), 2): #loop over string and seperate from symbols and positions
            symbol = lines[i]
            coords = list(map(float, lines[i + 1].split()))
            atom_symb.append(symbol)
            atom_pos.append(coords)
        
        atoms = Atoms(symbols = atom_symb, scaled_positions=atom_pos, cell=cell, pbc = True)
        return atoms #tested and works in notebook

        
    
    @property
    def prompt_header(self):
        return (
        "Below is a description of a bulk material. "
        "Generate a description of the lengths and angles of the lattice vectors "
        "and then the element type and coordinates for each atom within the lattice:\n"
    )