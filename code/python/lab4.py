System = ['A','B','C']
Channel = [19, 57, 100]
Cell = [394, 98, 49]
A = [12, 45, 88]     #total carried traffic
Au = 2 *(3/60)       #traffic intensity per user
Total_subscriber = 0
for s, i, j, k in zip(System, A, Channel, Cell):
    print('For System:',s)
    User_per_cell = i/0.1
    Total_subscriber_per_system = User_per_cell * k
    Market_penetration_per_system = (Total_subscriber_per_system / 2000000)*100
    Total_subscriber = Total_subscriber + Total_subscriber_per_system 
    print("User Per Cell: ", User_per_cell,"\nTotal subscriber per system: ",Total_subscriber_per_system)
    print('Market penetration per system: ', round(Market_penetration_per_system, 3),'%')
print('---------------------------------------------')
Total_market_penetration = (Total_subscriber / 2000000)*100
print('Market penetration for total system:', round(Total_market_penetration, 3),'%')


