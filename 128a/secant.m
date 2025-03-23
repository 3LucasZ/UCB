function p = secant(f, p0, p1, tol)
    while 1
        p = p1 - f(p1)*(p1-p0)/(f(p1)-f(p0));
        disp(p);
        if abs(p-p1) < tol, break; end
        p0 = p1;
        p1 = p;
    end
end