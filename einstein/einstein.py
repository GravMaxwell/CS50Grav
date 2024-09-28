# define speed of light "c" in m/s (3x10^8)
c = 3 * 10**8

# prompt user to input a mass in kg
mass = int(input("m: "))

# calculate the total energy in Joules (E = mass x c^2)
energy = mass * c**2

# output energy in joules
print(energy)
