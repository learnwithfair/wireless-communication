
Au = 0.1
GOS = 0.005
A = [0.005, 1.13, 3.96, 11.10, 80.9]
T = [1, 5, 10, 20, 100]
j = 0
for i in A:
    U = round(i/Au)
    if(U<1):
        U=1
    print('For trunked channel',T[j],', total number of user/s: ',U)
    j += 1
