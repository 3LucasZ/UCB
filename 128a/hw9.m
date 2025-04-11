format long

real_y = @(t) exp(-10*t);
f = @(t, y) -10*y;
a = 0;
b = 2;
h = 0.1;
w1 = 1;

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, real_y);
euler(f, a, b, h, w1, ax1);

% ax = gca;
% ax.XAxisLocation = 'origin';
% ax.YAxisLocation = 'origin';
grid on;