function [root, info] = modifiedzeroin3040268988(f, Int, params)



% unpack input fields
[a, b] = deal(Int.a, Int.b);
[root_tol, func_tol] = deal(params.root_tol, params.func_tol);
vrb = false;
maxCalls = 100;
window = 4;
% [left bound, right bound, current best guess]
[x0, x1, x2] = deal(a, b, (a+b)/2);
[f0, f1, f2] = deal(f(x0), f(x1), f(x2));
% keep track of function calls and past IQI errors
calls = 3;
E = [];
% run algorithm
while 1
    % IQI to estimate zero
    L0 = f1*f2*x0 / ((f0 - f1)*(f0 - f2));
    L1 = f0*f2*x1 / ((f1 - f0)*(f1 - f2));
    L2 = f0*f1*x2 / ((f2 - f0)*(f2 - f1));
    x3 = L0 + L1 + L2;
    % print status: x0, x1, x2 (lb, rb, root, IQI root), f2 (error)
    if vrb, fprintf('%-15d %-15d %-15d %-15d %-15d \n', [x0 x1 x2 x3 f2]); end
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
    fail = false;
    if (x3 < a || x3 > b)
        fail = true;
    else
        f3 = f(x3);
        E = [f3 E];
        calls = calls + 1;
        if (length(E) >= window && abs(min(E(1:window))) > abs(max(E(1:window)))/2)
            fail = true;
        end
    end
    if fail
        % IQI fail
        if vrb, fprintf('IQI failed \n'); end
            % use bisection since its reliable
            x2 = (x0+x1)/2;
            f2 = f(x2);
            calls = calls+1;
            E = [];
    else
        % IQI success
        x2 = x3;
        f2 = f3;
    end
    % terminate on convergence
    if ((x1 - x0) <= root_tol || abs(f2) <= func_tol)
        root = x2;
        info.flag = 1;
        break;
    end
    % emergency termination
    if (calls >= maxCalls) 
        if vrb, disp("Program Terminated \n"); end
        root = -1;
        info.flag = 0;
        return;
    end
end
if vrb
    fprintf('Function calls: %d \n', calls);
    fprintf('Root: %.15f \n', root);
    fprintf('Error: %.5e \n', f2);
end



end