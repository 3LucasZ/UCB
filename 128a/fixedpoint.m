function p = fixedpoint(g, p0, tol)
    while 1
        p = g(p0);
        disp(p);
        if abs(p-p0) < tol, break; end
        p0 = p;
    end
end