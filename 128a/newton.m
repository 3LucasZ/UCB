function [A, p] = newton(f, df, p0, tol)
    A = [];
    while 1
        p = p0 - f(p0)/df(p0);
        A = [A p];
        if abs(p-p0) < tol, break; end
        p0 = p;
    end
end