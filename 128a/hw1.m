% syms k
% f = (-1)^k * 5^k / factorial(k);
% V = subs(f, k, 0:9);
% s = double(sum(V));

syms k
f = 5^k / factorial(k);
V = subs(f, k, 0:9);
s = 1 / double(sum(V));