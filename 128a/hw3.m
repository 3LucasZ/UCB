% f = @(x) 600*x.^4 - 550*x.^3 + 200*x.^2 - 20*x - 1;
% df = @(x) 2400*x.^3 - 1650*x.^2 + 400*x - 20;
% a = 0.1;
% b = 1;
% tol = 1e-4;

% bisection(f, a, b, tol);

% [A, p] = newton(f, df, (a+b)/2, tol);
% disp(A);

% p = secant(f, a, (a+b)/2, tol);
% p = muller(f, 0.2, 0.4, 0.6, tol);

f = @(x) 2*pi*(x+0.25).^2 + 2*pi*(x+0.25)*(1000/(pi*x*x)+0.25);
p = fminbnd(f, 1, 10);
disp(p);
disp(f(p));

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;