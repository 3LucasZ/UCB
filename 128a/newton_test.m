% f = @(x) cos(x);
% df = @(x) -sin(x);
% f = @(x) 2*x*cos(2*x) - (x-2)^2;
% df = @(x) -4*x*sin(2*x)+2*cos(2*x)-2*x+4;
% f = @(x) x^2 - 10*cos(x);
% df = @(x) 2*x + 10*sin(x);
% p0 = 25;
f = @(x) sin(3*x) + 3*exp(-2)*sin(x) - 3*exp(-x)*sin(2*x) - exp(-3*x);
df = @(x) 3*cos(3*x) + 3*exp(-2)*cos(x) - 6*exp(-x)*cos(2*x) + 3*exp(-x)*sin(2*x) + 3*exp(-3*x);
p0 = 3.5;

format short
[A, p] = newton(f, df, p0, 1e-5);
disp(A)

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;