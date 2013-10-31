#  3SAT problem
#  (x1 OR x2 OR ¬x3)← C1
#  (x1 OR x2 OR x3)← C2
#  (x1 OR ¬x2 OR ¬x3)← C3
#  (x1 OR ¬x2 OR x3)← 
#  C4(¬x1)← C5
#  
#  0-1 LP REDUCTION where x1,x2,x3 correspond to y1, y2 y3
#  
#  y1 +y2 +(1−y3)≥z1
#  y1+y2+y3≥z2
#  y1+(1−y2)+(1−y3)≥z3
#  y1+(1−y2)+y3≥z4
#  1−y1≥z5
#  y1,…,y3,z1,…,z5∈{0,1}


A = [1 1 0; 1 1 1; 1 0 0; 1 0 1; 0 0 0];
b = ones(5,1);
c = ones(3,1);
ctype= cell2mat(arrayfun(@(t){"L"}, b));
vartype= cell2mat(arrayfun(@(t){"I"}, c));
 
[xmin, fmin, status, extra]= glpk (c, A, b, [], [], ctype, vartype);
xmin
