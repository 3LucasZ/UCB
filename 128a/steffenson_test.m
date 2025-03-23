% g = @(x) 1 + sin(x)^2;
% p0 = 1;

g = @(x) (x+1)^(1/3);
p0 = 1.5;
[A, p] = steffenson(g,p0,1e-8);
disp(A);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, g);
plot(ax1, p, g(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;