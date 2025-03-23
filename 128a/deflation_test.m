% a = [1 -2 -12 16 -40];
a = [16 88 159 76 -240];

r = deflation(a, 1e-5);


compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, poly2sym(a));
for i=1:length(r)
    [~, y, ~] = horner(a, r(i));
    plot(ax1, r(i), y, ".", 'MarkerSize', 30);
end

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;