import math
Total_BW = 30000     
Channel_BW = 25*2
Total_Available_Channel = Total_BW/Channel_BW
Allocated_Spectrum = 1000
Available_Control_Channel = Allocated_Spectrum/Channel_BW
N = [4, 7, 12]
j = 1
for i in N:   
    Channel_per_cell = Total_Available_Channel / i
    voice_channel_per_cell = (Total_Available_Channel - Available_Control_Channel)/i
    control_channel_per_cell = Channel_per_cell - voice_channel_per_cell
    print('For',i,'cell reuse pattern: \nTotal number of channels per cell: ',math.floor(Channel_per_cell), '\nVoice channel per cell: ',math.floor(voice_channel_per_cell), '\nControl channel per cell: ', math.ceil(control_channel_per_cell))

