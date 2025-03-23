% f = @(x) sin(x);
% f = @(x) x+1-2*sin(pi*x);
% f = @(x) tan(x)-x;

format long
p = bisection(f, 4, 4.5, 1e-5);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;