% f = @(x) x.^4 - 2*x.^3 - 12*x.^2 + 16*x - 40;
% p0 = -4;
% p1 = -3;
% p2 = -2;
% p0 = 4;
% p1 = 5;
% p2 = 6;

f = @(x) 16*x.^4 + 88*x.^3 + 159*x.^2 + 76*x - 240;
p0 = 0.5;
p1 = 0.6;
p2 = 0.7;

p = muller(f, p0, p1, p2, 1e-5);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;