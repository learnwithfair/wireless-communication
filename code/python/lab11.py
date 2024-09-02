from math import pow
bits = [3,3,26,8.25]
bandwidth = 270.833*pow(10,3)
print(f"A time slot has {sum(bits,2*58)} bits\n------------------------\n")
print(f"A. Number of overhead bits per frame is {int(sum(bits)*8)} bits\n")
print(f"B. Total number of bits per frame {int(sum(bits,2*58)*8)} bits/frame\n")
print(f"C. Frame rate is {round((bandwidth /(sum(bits,2*58)*8)),3) } frame/second\n")
print(f"D. Time duration of a slot {round((sum(bits,2*58))/bandwidth /pow(10,-6),3)} us\n")
print(f"E. Frame efficiency Eta {(1- (int(sum(bits)*8))/(sum(bits,2*58)*8)) *100} %") 

