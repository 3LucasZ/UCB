format long
params.root_tol = 1e-7;
params.func_tol = 1e-7;

f6 = @(x) x^3 - 32*x + 128; Int6.a = -8; Int6.b = 0;
% f = @(x) (x-5)^7 - 1e-1; 
% Int.a = 0; 
% Int.b = 10; 
% 
% [root, info] = modifiedzeroin3040268988(f, Int, params);

modifiedzeroin3040268988(f6, Int6, params);