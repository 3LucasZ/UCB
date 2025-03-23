a = [1 -2 -12 16 -40];
x0 = 6;

[b, y, d] = horner(a, x0);
disp(b);
disp(y);
disp(d);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, poly2sym(a));
plot(ax1, x0, y, ".", 'MarkerSize', 30);
secantline = @(x) d*(x - x0) + y;
fplot(ax1, secantline);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;