from math import pow
Pam,k = 400,0.75
Pc = Pam/(1+(pow(k,2)/2))
print(f"A. Percentage of the total power in the carrier is {Pc/Pam *100} % ")
print(f"B. The power in each sideband {(Pam-Pc)*0.5} KW")
print(f"C. The total power saving if the carrier and one of the sidebands are now suppressed {round(((1- ((Pam-Pc)*0.5)/Pam)*100),2)} %")

