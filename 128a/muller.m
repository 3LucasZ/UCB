% Find a root using Muller's method.
% Extended secant method -> using quadratic fit
% Unfortunately copied this from persson since it is too difficult

function p = muller(f, p0, p1, p2, tol)


h1 = p1 - p0;
h2 = p2 - p1;
d1 = (f(p1) - f(p0)) / h1;
d2 = (f(p2) - f(p1)) / h2;
d = (d2 - d1) / (h2 + h1);
while 1
    b = d2 + h2*d;
    D = sqrt(b^2 - 4*f(p2)*d);
    if abs(b - D) < abs(b + D)
        E = b + D;
    else
        E = b - D;
    end
    h = -2*f(p2)/E;
    p = p2 + h;
    disp(p);
    if abs(h) < tol, break; end
    p0 = p1;
    p1 = p2;
    p2 = p;
    h1 = p1 - p0;
    h2 = p2 - p1;
    d1 = (f(p1) - f(p0)) / h1;
    d2 = (f(p2) - f(p1)) / h2;
    d = (d2 - d1) / (h2 + h1);
end
