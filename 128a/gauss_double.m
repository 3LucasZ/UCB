%% Gaussian Quadrature for Double Integrals
%% Adapted from Persson

n = 7;
[x,c] = gauss(n);
y = x';
c = c * c';

%%% Integrate f(x,y) = exp(x+y) on [0,1]*[0,2] using Gaussian quadrature

x1 = (x + 1)/2;
y1 = y + 1;
c1 = c * 1 * 2 / 4;
J1 = sum(sum(exp(x1 + y1) .* c1))

% Compare with Simpson
J1s = simpsondouble(@(x,y) exp(x+y), @(x) 0, @(x) 2, 0, 1, 16, 16)

%%% Integrate f(x,y) = exp(x+y) on [0,1]*[x,1+.5*x] using Gaussian quadrature

x2 = x/2 + .5;
y2 = x2 + (y/2 + .5) .* (1 - .5*x2);
c2 = c * (1/2) .* (1 + 0.5*x2 - x2)/2;
J2 = sum(sum(exp(x2 + y2) .* c2))

% Compare with Simpson
J2s = simpsondouble(@(x,y) exp(x+y), @(x) x, @(x) 1 + 0.5*x, 0, 1, 16, 16)

% Plot domain and Gaussian integration nodes
plot(x2,y2,'.k')
line([0,1,1,0,0], [0,1,1.5,1,0])
axis equal
