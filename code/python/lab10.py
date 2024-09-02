from math import pow
bandwidth = 270833 # Hz unit
print(f"A. The time duration of a bit T_b is {round(((1/bandwidth )/pow(10,-6)),3)} us\n")
print(f"B. The time duration of a slot T_slot is {round((156.25*((1/bandwidth )/pow(10,-3))),3)} ms\n")
print(f"C. The time duration of a frame T_f is {round(((156.25*((1/bandwidth )))*8 / pow(10,-3)),3)} ms\n")
print(f"D. A single user has to wait 4.615 ms. The arrival time of new frame for its next transmission.") 







