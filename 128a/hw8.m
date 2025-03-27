%% 4.7: Gaussian Quadrature
format long
g = @(t) 1/4 * ((t+13)/4) / sqrt(((t+13)/4)^2-4);

t = -1/sqrt(3);
ret = g(t);
disp(t);
disp(ret);

t = 1/sqrt(3);
ret = g(t);
disp(t);
disp(ret);

%% 4.8: Double Integration
%(1c, 2c)
f = @(x, y) exp(y-x);
[a, b, c, d] = deal(0, 0.5, @(x) 0, @(x) 0.5);
[m, n] = deal(2, 2);
approx = simpson_double(f, a, b, c, d, m, n);
disp(approx);
[m, n] = deal(40, 40);
real = simpson_double(f, a, b, c, d, m, n);
disp(real);
disp(abs(real-approx));

%(17)
f = @(x,y) exp(-(x*x+y*y));
xf = @(x,y) x*f(x,y);
yf = @(x,y) y*f(x,y);

[a, b] = deal(0, 1);
c = @(x) 0;
d = @(x) sqrt(1-x*x);
[n, m] = deal(14, 14);

r = simpson_double(f, a, b, c, d, n, m);
xr = simpson_double(xf, a, b, c, d, n, m);
yr = simpson_double(yf, a, b, c, d, n, m);

disp(xr/r);
disp(yr/r);