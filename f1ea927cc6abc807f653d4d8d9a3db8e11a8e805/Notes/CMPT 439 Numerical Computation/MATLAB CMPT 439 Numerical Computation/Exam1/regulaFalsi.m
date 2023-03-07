function [root, fx]=regulaFalsi(func,x0,x1,tolerance)

% input:
% func = name of function
% x0, x1 = initial guesses
% tolerance = tolerance threshold


% output:
% root = real root
% fx = function value at root


if nargin<4,error('at least 4 input arguments required'),end
if func(x0)*func(x1)>0,error('no sign change'),end


% initialization
iter = 0;

fprintf('Iteration#     x0          x1          f(x0)          f(x1)\n');
fprintf('%5d %13.4f %11.4f %13.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
while(1)
    
iter = iter + 1;
    
x2 = x1 - func(x1) * (x0-x1)/(func(x0)-func(x1));


if (func(x0)*func(x2)<0)
    x1 = x2;
else
    x0 = x2;
end


fprintf('%5d %13.4f %11.4f %13.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
if (abs(func(x2)) <= tolerance)
    break;
end
   
end
root = x2;
fx = func(x2);
end