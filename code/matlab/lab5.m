clc;
clear all;
close all;
c = 3*(10^8);                                                        % Velocity of light, c
f = 900*(10^6);
D = 1;                                                                   % Maximum Dimension, D
lemda = (c/f);                                                        % Wavelength,, lamda
df = 2*(D^2)/(lemda);                                          % Fraungofer distance, df
pl = -10*log10((lemda^2)/(((4*pi)^2)*(df^2)));  % Path loss, Pl(dB)
fprintf('Fraunhofer distance, Df: %.2f m\n',df)
fprintf('Path Loss PL(dB) : %.2f dB\n',pl);


