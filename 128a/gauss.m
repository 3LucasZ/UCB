%% Compute Gaussian quadrature points and coefficients
%% If f is provided (optional), will compute the integral approximation
%% Credits: Adapted from Persson

function [x, c] = gauss(n, f)

% nth degree Legendre Polynomial (P)
% calculated with recursive formula
% P_0(x) = 1
% P_1(x) = x
% (n+1)P_{n+1}(x) = (2n+1)xP_{n}(x) - nP_{n-1}(x)
% integral(P(x)*P_n(x)) = 0 evaluated [-1, 1], P(x) is any poly deg < n
P = zeros(n+1,n+1);
P([1,2],1) = 1;
for k = 1:n-1
    P(k+2,1:k+2) = ((2*k+1)*[P(k+1,1:k+1) 0] - ...
                    k*[0 0 P(k,1:k)]) / (k+1);
end

% zeros of P (x)
x = sort(roots(P(n+1,1:n+1)));

% coefficients (c)
A = zeros(n,n);
for i = 1:n
    A(i,:) = polyval(P(i,1:i),x)';
end
c = A \ [2; zeros(n-1,1)];

% approximate the integral
if (exist('f', 'var'))
   ans = 0;
   for i = 1:n
       ans = ans + c(i)*f(x(i));
   end
   disp(ans);
end

end