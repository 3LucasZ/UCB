real_y = @(t) log(exp(t)+exp(1)-1);
f = @(t, y) exp(t-y);
a = 0;
b = 5;
h = 0.05;
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