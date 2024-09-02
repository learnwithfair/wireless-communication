clc;
clear all;
close all;
Am_signal_power = 400; %unit in KW
modulation_depth = 0.75;
carrier_power_pc = (Am_signal_power)/(1+((modulation_depth)^2)/2);
fprintf('Carrier power Pc: %.2f KW\n',carrier_power_pc);

total_power = (carrier_power_pc/Am_signal_power)*100;
fprintf('a) Total power in the carrier is: %.2f%%\n',total_power)

power_in_each_sideband = (Am_signal_power-carrier_power_pc)*0.5;
fprintf('b) Power in each sideband: %.2f KW\n',power_in_each_sideband)

percentage_power = (1-(power_in_each_sideband)/Am_signal_power)*100;
fprintf('c) Percentage power saving: %.2f%%\n',percentage_power)