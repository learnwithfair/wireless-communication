clc;
clear all;
close all;

% Solution (a)
Tn = 150;
N = 70;
delT = Tn/N;
fprintf('a) delT = %.2f micro_s\n\n',delT);

% Solution (b)
Tn = 4;
MBW = 2/delT;
fprintf('b)\nThe maximum bandwidth that the SMRCIM model can accurately represent = %.3f MHz\n',MBW);
Tn = 4;
delT = (Tn/N)*1000;
RFBW = (2/delT)*1000;
fprintf('delT for SMRCIM urban mircrocell model is %.3f ns\n',delT);
fprintf('The maximum RF bandwidth that can be represented is %.2f MHz\n\n',RFBW);

% Solution (c)
Exdel = 500;
delT = Exdel/N;
disp('c)')
fprintf('For indoor channel %f ns\n',delT);
RFBW = (2/delT)*1000;
fprintf('The maximum RF bandwidth for the indoor channel model is %.2f MHz\n',RFBW);

