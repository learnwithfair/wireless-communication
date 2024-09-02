Max_excess_delay_Tn = 150
N = 70
Delta_T = round((Max_excess_delay_Tn / N),2)
print('(a):\nDelta Tao =',Delta_T,'us.')
print('\n(b):')
MBW = round((2/Delta_T), 3)
print('The maximum bandwidth that the SMRCIM model can accurately represent =', MBW,'MHz')
Tn = 4
New_Delta_T = Tn/N
RFBW = 2/New_Delta_T
print('The maximum RF bandwidth  = ', RFBW,'MHz')
print('\n(c):')
Excess_delay = 500
Indoor_Channel_DT = round((Excess_delay / N),2)
print('Indoor channel Delta Tao =', Indoor_Channel_DT,'ns')
RFBW_for_c = 1000*round((2 / Indoor_Channel_DT), 2)
print('The maximum RF bandwidth for the indoor channel model =', RFBW_for_c,'MHz')

