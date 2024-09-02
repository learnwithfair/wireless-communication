Am,Fm,Ko,Gain = 8,4,10,10    #all parameters ans with Khz so not include 10^3 part
print(f"A. The peak frequency deviation is Deltaf equal to {Am*Gain} KHz\n")
print(f"B. The modulating index is Betaf equal to {int((Am*Gain)/Fm)}\n")
print(f"C. The phase modulating index is Betaf equal to  {Am*Ko} radians") 

