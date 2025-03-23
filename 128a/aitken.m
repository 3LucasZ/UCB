function [A, p] = aitken(ps)
    A = [];
    for n = 1:size(ps, 2)-2
        p = ps(n) - (ps(n+1)-ps(n))^2/(ps(n+2)-2*ps(n+1)+ps(n));
        A = [A p];
    end
end