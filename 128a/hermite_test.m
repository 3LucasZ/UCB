x = [0 0 1 1];
f = @(x) x.^3;
disp(hermite(x, f));