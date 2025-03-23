function F = hermite(x, f)

n = length(x)-1;
F = zeros(n+1,n+1);
F(:,1) = f(x(:));

syms c;
f_sym = sym(f(c));
df_sym = diff(f_sym, c);


for i = 1:n
    for j = 1:i
        if j+1==2 && mod(i+1,2)==0
            F(i+1,j+1) = subs(df_sym, c, x(i+1));
        else
            F(i+1,j+1) = (F(i+1,j) - F(i,j)) / (x(i+1) - x(i-j+1));
        end 
    end
end
