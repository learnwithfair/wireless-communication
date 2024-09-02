clc;
clear all;
close all
Fm = 4; %unit in kHz
mt_max_value = 8; %unit in V
womeca = 10; %unit in kHz/V

peak_deviation_delta_f = mt_max_value*womeca;
fprintf('a) Peak deviation delta_f: %d KHz\n',peak_deviation_delta_f)

fre_modu_index_Bf=(peak_deviation_delta_f/Fm);
fprintf('b) Frequency modulation index Bf: %d\n',fre_modu_index_Bf)

phase_modulation_index = womeca*mt_max_value;
fprintf('c) Phase modulation index: %d radians\n',phase_modulation_index)