% input: poly p coef a [an ... a0], tol
% output: zeros [r1 ... rn]

function r = deflation(a, tol)

n = length(a);
disp(a);
if n <= 3
    disp("finding last 2 roots");
    r = roots(a)'; 
    disp(r);
    r = []
    return;
end
disp("finding root");
p0 = -4;
runs = 0;
while 1
    runs = runs + 1;
    [~, y, d] = horner(a, p0);
    p = p0 - y/d;
    disp(p);
    if abs(p0-p) < tol || runs > 20, break; end
    p0 = p;
end
[b, ~, ~] = horner(a, p);
r = cat(2, p, deflation(b, tol));

end