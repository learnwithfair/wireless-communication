clc;
clear all;
close all;

fc = 900*10^6;                                      % Carrier Frequency, fc
wavelength = (3*10^8)/(900*10^6);    % Wavelength
v = 70*(1000/(60*60));                        % Vehicle speed, v

%  Solution (a) 
The_received_frequency_of_A_is = (floor(fc)+(v/wavelength))/10^6;
fprintf('a) The received frequency of A is: %.6f MHz\n\n',The_received_frequency_of_A_is);

% Solution (b)
The_received_frequency_of_B_is = (floor(fc)-(v/wavelength))/10^6;
fprintf('b) The received frequency of B is: %f MHz\n\n',The_received_frequency_of_B_is);

% Solution (c)
disp('c) The received signal frequency is the same of the transmitted frequency 900 MHz');

