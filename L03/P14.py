def energy():
    fuel = float(input('Fuel density (in kg/L): '))
    calorific = int(input('Calorific value (in MJ/kg): '))
    energy_value = fuel * calorific
    energy_value_msg = "This fuel has energy per volume of {:.2f} MJ/L.\nThat is {:.2f} MJ/bbl."
    energy_value_msg = energy_value_msg.format(energy_value, energy_value * 158.987)
    print(energy_value_msg)
    return

if __name__ == '__main__':
    energy()