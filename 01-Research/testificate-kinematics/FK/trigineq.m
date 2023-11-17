%% Triangle Inequality Functions %%

clc
clear
%%

syms a b c alpha beta theta;

fcn = b^2 == a^2 + c^2 - 2*a*c*cos(beta);

S = solve(fcn, c);

S = simplify(S(2))


%%

fcn2 = c == b/sin(beta)*sin(pi-beta-(asin(sin(beta)*a/b)));

S2 = solve(fcn2,c);

S2 = simplify(S2)


%%


a = 15.61;
b = 21.8;
beta = 2.5536;

c =triIneq(a,b,beta)
c =triIneq1(a,b,beta)

%%
% function to evaluate the unknown side of a triangle
% given the other two sides

function [c] = triIneq(a,b,beta)
c = b*(-(a^2*sin(beta)^2 - b^2)/b^2)^(1/2) + a*cos(beta);
end

function [c] = triIneq1(a,b,beta)
c = (a^2*cos(beta)^2 - a^2 + b^2)^(1/2) + a*cos(beta);
end


 



