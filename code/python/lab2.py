import math
min_SNdB = 15
n = [4, 3]
N = [7, 12]
for j in N:
    for i in n:
        Q = math.sqrt(3*j)
        SI = 10*math.log10(pow(Q,i)/6)
        print('Signal to Interference ratio:',SI)
        if SI > min_SNdB:
            print('For n = ',i,', N =',j,'can be used.')
        else:
            print('For n = ',i,', N =',j,'can not be used.')
