format long
params.root_tol = 1e-7;
params.func_tol = 1e-7;

f = @(x) x*exp(-x) - 2*x + 1;
Int.a = 0; Int.b = 3;
[root, info] = modifiedzeroin3040268988(f, Int, params);
% 0.671553094250269

f = @(x) x*cos(x) - 2*x.^2 + 3*x - 1;
Int.a = 1; Int.b = 3;
[root, info] = modifiedzeroin3040268988(f, Int, params);
% 1.256623322505569

f = @(x) x.^3 - 7*x.^2 + 14*x - 6;
Int.a = 0;
Int.b = 1;
% fplot(f, Int);
[root, info] = modifiedzeroin3040268988(f, Int, params);
% 0.585786437626905

f = @(x) sqrt(x) - cos(x);
Int.a = 0;
Int.b = 1;
[root, info] = modifiedzeroin3040268988(f, Int, params);
% 0.641714370872883

f = @(x) 2*x*cos(2*x) - (x+1).^2;
Int.a = -4;
Int.b = -2;
[root, info] = modifiedzeroin3040268988(f, Int, params);
% −2.191308011797247