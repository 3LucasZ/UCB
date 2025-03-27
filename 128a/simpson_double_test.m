% Test: the exact answer is 0.25
f = @(x, y) x*y;
a = 0; b = 1; c = @(x) 0; d = @(x) 1;
m = 6; n = 6;
area = simpson_double(f, a, b, c, d, m, n);
disp(area);