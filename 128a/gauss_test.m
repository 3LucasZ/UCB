format long

g = @(t) 1/4 * ((t+13)/4) / sqrt(((t+13)/4)^2-4);

[x, c] = gauss(2, g);
disp(x); disp(c);

[x, c] = gauss(4, g);
disp(x); disp(c);