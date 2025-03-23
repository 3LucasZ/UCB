% f = @(x) cos(x);
f = @(x) 2*x*cos(2*x) - (x-2)^2;

format long
p = secant(f, 2, 3, 1e-5);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;