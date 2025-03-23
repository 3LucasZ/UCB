f = @(x) exp(6*x) + 3*log(2)^2*exp(2*x) - log(8)*exp(4*x) - log(2)^3;
df = @(x) 6*exp(6*x) + 6*log(2)^2*exp(2*x) - 4*log(8)*exp(4*x);
p0 = 0;
tol = 0.0002;

format short
[A, p] = newton(f, df, p0, tol);
disp(A);
[A, p] = aitken(A);
disp(A);

compPlot = figure();
ax1 = axes('Parent', compPlot);
hold(ax1, 'on');

fplot(ax1, f);
plot(ax1, p, f(p), ".", 'MarkerSize', 30);

ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
grid on;
