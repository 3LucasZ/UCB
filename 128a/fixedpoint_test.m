% g = @(x) cos(x);
g = @(x) (x+1)^(1/3);

format long
p = fixedpoint(g, 1, 1e-5);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, g);
plot(ax1, p, g(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;