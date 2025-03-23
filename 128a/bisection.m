function p = bisection(f, a, b, tol)
    p = (a+b)/2;
    disp([a p b]);
    if p-a > tol
        if f(a)*f(p) < 0
            p = bisection(f, a, p, tol);
        else
            p = bisection(f, p, b, tol);
        end
    end
end
