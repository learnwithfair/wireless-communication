import math
Operating_frequency = 900 * pow(10,6)
Velocity_of_light = 3*pow(10,8)
Wavelength = round((Velocity_of_light / Operating_frequency), 2)
Max_dimension = 1
Fraunhoffer_distance = round(((2 * pow(Max_dimension, 2)) / Wavelength), 0)
Path_loss = round((-10*math.log10(pow(Wavelength,2)/pow((4*math.pi * Fraunhoffer_distance),2))), 2)

print('Wavelength: ', Wavelength, 'm')
print('Fraunhoffer distance: ', Fraunhoffer_distance, 'm')
print('Path Loss: ', Path_loss,'dB')