function [xmin,fmin] = minimizeCost(A,b,c,sense)
lb =  cell2mat(arrayfun(@(t){0}, c));
ub= [];
ctype= cell2mat(arrayfun(@(t){"U"}, b));
vartype= cell2mat(arrayfun(@(t){"C"}, c));

if ~exist('sense','var'), sense=1; end

param.msglev= 1;
param.itlim= 100;

[xmin, fmin, status, extra]= glpk (c, A, b, lb, ub, ctype, vartype, sense, param);

end
