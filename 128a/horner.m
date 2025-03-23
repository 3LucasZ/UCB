% input: poly p coef a [an ... a0], evaluate x0
% output: poly q coef b, p(x0), and p'(x0)

function [b, y, d] = horner(a, x0)

n = length(a)-1;

b = [a(1)];
y = a(1);
for j = 2:n
    y = x0*y + a(j);
    b = [b y];
end
y = x0*y + a(n+1);

d = b(1);
for j = 2:n
    d = x0*d + b(j);
end


    