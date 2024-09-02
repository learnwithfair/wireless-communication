clc;
clear all;
close all;
trans_freq = 270.833; %unit in kbps
num_of_bit_in_each_time_slot = 6+(8.25)+26+(2*58);
fprintf('A time slot has: %.2f bits\n',num_of_bit_in_each_time_slot);

Boh= (8*6)+(8*8.25)+(8*26);
fprintf('a) Number of overhead bits Boh: %.2f bits\n',Boh)

num_of_bit_per_frame = (8*num_of_bit_in_each_time_slot);
fprintf('b) Number of bits per frame: %.2f bits/frame\n',num_of_bit_per_frame);

frame_rate = (trans_freq/num_of_bit_per_frame)*1000;
fprintf('c) Frame rate: %.2f frame/sec\n',frame_rate);

time_duration_of_a_slot = (num_of_bit_in_each_time_slot)*(1/trans_freq)*1000;
fprintf('d) Time duration of a slot: %.2f micro_second\n',time_duration_of_a_slot);

frame_efficiency = (1-(Boh)/num_of_bit_per_frame)*100;
fprintf('e) Frame Efficiency: %.2f%%\n',frame_efficiency);