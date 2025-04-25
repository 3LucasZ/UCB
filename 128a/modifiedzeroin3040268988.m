function [root,info] = modifiedzeroin3040268988(f, Int, params)


% unpack input fields
[a, b] = deal(Int.a, Int.b);
[root_tol, func_tol] = deal(params.root_tol, params.func_tol);
vrb = false;
% [left bound, right bound, current best guess]
[x0, x1, x2] = deal(a, b, (a+b)/2);
[f0, f1, f2] = deal(f(x0), f(x1), f(x2));
% keep track of function calls and past errors
calls = 3;
E = [];
% run algorithm
while 1
    if vrb, fprintf('%-15d %-15d %-15d %-15d \n', [x0 x1 x2 f2]); end
    % IQI to estimate zero
    L0 = f1*f2*x0 / ((f0 - f1)*(f0 - f2));
    L1 = f0*f2*x1 / ((f1 - f0)*(f1 - f2));
    L2 = f0*f1*x2 / ((f2 - f0)*(f2 - f1));
    x3 = L0 + L1 + L2;
    f3 = f(x3);
    calls = calls + 1;
    % [x0, x2] are new bounds
    if (f0*f2 < 0)
        x1 = x2;
        f1 = f2;
    % [x2, x1] are new bounds
    else
        x0 = x2;
        f0 = f2;
    end
    % IQI failed, x3 out of range or trouble converging
    if x3 < a || x3 > b || (length(E) >= 3 && abs(f3) > abs(E(3))/2)
        % use bisection since its reliable
        x2 = (x0+x1)/2;
        f2 = f(x2);
        calls = calls+1;
    % IQI success
    else
        x2 = x3;
        f2 = f3;
    end
    E = [f2 E];
    % terminate on convergence
    if ((x1 - x0) <= root_tol || abs(f2) <= func_tol)
        root = x2;
        info = 1;
        break;
    end
    % emergency termination
    if (calls >= 30) 
        if vrb, disp("Program Terminated"); end
        root = -1;
        info = 0;
        return;
    end
end
if vrb
    fprintf('Function calls: %d \n', calls);
    fprintf('Root: %.15f \n', root);
    fprintf('Error: %.5e \n', f2);
end


end