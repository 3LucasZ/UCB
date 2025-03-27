% Credits: Adapted from SIMPSONDOUBLE Algorithm 4.4 in Burden/Faires
% J = SIMPSONDOUBLE(F, A, B, C, D, M, N) 
% F is the function,
% A, B are endpoints (x)
% C, D are endpoints (y), that are functions constrained by x
% M, N are the # of intervals (x, y)

function J = simpson_double(f, a, b, c, d, m, n)


h = (b-a) / n;
J1 = 0; J2 = 0; J3 = 0;
for i = 0:n
    x = a + i*h;
    HX = (d(x)-c(x)) / m;
    K1 = f(x,c(x)) + f(x,d(x));
    K2 = 0;
    K3 = 0;
    for j = 1:m-1
        y = c(x) + j*HX;
        Q = f(x,y);
        if mod(j,2) == 0    % j even
            K2 = K2 + Q;
        else                % j odd
            K3 = K3 + Q;
        end
    end
    L = (K1 + 2*K2 + 4*K3) * HX/3;
    if i == 0 || i == n     % end points
        J1 = J1 + L;
    elseif mod(i,2) == 0    % i even
        J2 = J2 + L;
    else                    % i odd
        J3 = J3 + L;        
    end
end
J = h*(J1 + 2*J2 + 4*J3) / 3;


end