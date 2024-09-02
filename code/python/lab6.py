Carrier_fre = 900*1000000
Velocity_of_light = 3*100000000
Wavelength = round((Velocity_of_light / Carrier_fre), 2)
Vehicle_speed = round((70000/3600), 2)
Fd = round((Vehicle_speed / Wavelength), 2)
Fa = (Carrier_fre + Fd)/1000000
Fb = (Carrier_fre - Fd)/1000000
print("The received carrier frequency for 'a':\n", Fa, 'MHz')
print("The received carrier frequency for 'b':\n", Fb, 'MHz')
print("The received carrier frequency for 'c':  \nSince the vehicle is moving perpendicular to the angle of arrival to the transmitted signal, there is no doppler effect. \nSo, the received signal's frequency is the same as the transmitted signal's frequency.\nSo, the received carrier frequency for 'c': 900 MHz")