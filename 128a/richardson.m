% Example:
% Line one is the input (in this order) as row vector
% N1(h), N1(h/2), N1(h/4), N1(h/8)
% N2(h), N2(h/2), N2(h/4)
% N3(h), N3(h/2)
% N4(h)
function F = richardson(x)
n = length(x);
A = zeros(n, n);
A(1,:) = x;
for i = 2:n
    for j=1:n-i+1
        A(i,j) = A(i-1,j+1) + (A(i-1,j+1)-A(i-1,j))/(2^(i-1) - 1);
    end
end
F = A