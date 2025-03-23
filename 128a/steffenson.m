function [A, p] = steffenson(g, p0, tol)
    A = [];
    while 1
        p1 = g(p0);
        p2 = g(p1);
        p = p0 - (p1-p0)^2/(p2-2*p1+p0);
        A = [A p];
        if abs(p-p0) < tol, break; end
        p0 = p;
    end
end