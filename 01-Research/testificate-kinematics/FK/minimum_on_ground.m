%% Find Equadistance Point on Ground Between Two Poles %%
syms L d theta mu ;
left_pole = 9.985;
right_pole = 21;
between = 34.6564 ; 


eq1 = L*cos(theta) + L*cos(mu) == between;
eq2 = L*sin(theta) == right_pole;
eq3 = L*sin(mu) == left_pole;
eq4 = d == L*cos(mu)-12*cos(deg2rad(56.31));
eq5 = 2*L*L == left_pole^2+right_pole^2+(L*cos(mu))^2+(L*cos(theta))^2;

S = vpasolve([eq1 eq2 eq3 eq4],[L d theta mu]);

S.L
S.d