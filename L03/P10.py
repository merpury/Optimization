"""
Write a function named fire.
The function takes 2 filenames:
one is for covalence bond energies and
another is for the reaction specifying amounts of reactant
and product bonds.
The function reads both files for necessary information,
then calculates activation energy, releasing energy,
and the different energy
and appends the result at the end of the second file
---the reaction-bond file.
"""

def fire(fbond, fcombust):

    # Write your code here!!

    #################################
    ## Get bond-energy information
    #################################

    bond_energy = {}
    with open(fbond, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            bond_energy[parts[0]] = int(parts[1])
            
    # Check if we get bond energy ok
    # hint: having energy as a number is more convenient later
    # print(bond_energy)

    #################################
    ## Get combustion information
    #################################
    reactant_dict = {}
    product_dict = {}
    temp_list = []
    with open(fcombust, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            temp_list.append(line.strip())
        
        # line = f.readlines()[1] 
        # reactants = line.strip().split('+ ')
        # reactant_dict = split_text(reactants)
        # line2 = f.readlines()[1] 
        # products = line2.strip().split('+ ')
        # product_dict = split_text(products)
    reactants = temp_list[0].split('+ ')
    products = temp_list[1].split('+ ')
    reactant_dict = split_text(reactants)
    product_dict = split_text(products)
    # print(reactant_dict)
    # print(product_dict)
    
    E1 = 0
    E2 = 0
    for bond in reactant_dict:
        if bond in bond_energy:
            E1 += reactant_dict.get(bond) * bond_energy.get(bond)
    
    for bond in product_dict:
        if bond in bond_energy:
            E2 += product_dict.get(bond) * bond_energy.get(bond)
            
    #     #################
    #     # Reactants
    #     #################

    #     ###################################################
    #     # 1. Get reactant part, e.g., ["4 C-H", "2 O=O"]
    #     ###################################################

    #     reactant = f.readline()         # read the reactant line (2nd line)
    #     if reactant[-1] == '\n':
    #         reactant = reactant[:-1]    # remove nuisance '\n'

    #     reactant = reactant.split('+')  # separate each pair of number-symbol

    #     # print(reactant)

    #     ###################################################
    #     # 2. Compute E1
    #     # E.g., E1 = 4 x energy['C-H'] + 2 x energy['O=O']
    #     ###################################################

    #     E1 = 0  # Initialize activation energy
    #     for b in reactant:
    #         pair = b.strip()            # remove extra space
    #         num_bonds, bond_symbol = pair.split()
    #         bond_symbol = bond_symbol.strip()  # clean the whitespace out

    #         # num_bonds, e.g., 4
    #         # bond_symbol, e.g., 'C-H'

    #         # Get bond energy
    #         energy = 0 # bond_energy[bond_symbol]

    #         # Check if we have everything
    #         print('* reactant:', num_bonds, bond_symbol, energy)

    #         E1 += energy * float(num_bonds)

    #     # Check if we are doing OK with E1 calculation
    #     # print('E1 = ', E1)

    #     #################
    #     # Products
    #     # This is similar to Reactants.
    #     # We can even put these into another function,
    #     # and re-use it.
    #     #################

    #     # Need working code here!!!

    #     # print(product)

    #     E2 = 0

    #     # Need working code here!!!

    #     # Check if we are doing OK with E2 calculation
    #     # print('E2 = ', E2)

    total_E = E1 - E2
    msg = '\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(E1, E2, total_E)

    #     print(msg)
    with open(fcombust, 'a') as file:
        file.write(msg)

def split_text(texts):
    empty_dict = {}
    for text in texts:
        part = text.split(' ')
        empty_dict[part[1]] = float(part[0])
    
    return empty_dict

if __name__ == '__main__':
    # fire('bond_energy.txt', 'methane.txt')
    fire('bond_energy.txt', 'octane.txt')