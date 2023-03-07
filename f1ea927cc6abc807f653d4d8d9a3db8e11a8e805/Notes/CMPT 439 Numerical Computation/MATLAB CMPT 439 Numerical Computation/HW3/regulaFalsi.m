function [root, fx]=regulaFalsi(func,x0,x1,tolerance,choice)

% input:
% func = name of function
% x0, x1 = initial guesses
% tolerance = tolerance threshold

% choice = 1 of the 3 stopping criterias. 
% If user input 1, true error is used to stop the process.
% If user input 2, absolute approximate error is used to stop the process.
% If user input 3, relative approximate error is used to stop the process.


% output:
% root = real root
% fx = function value at root


if nargin<5,error('at least 5 input arguments required'),end
if func(x0)*func(x1)>0,error('no sign change'),end


% initialization
iter = 0;
x = x1;

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
    
if (choice == 1)
    fprintf('%5d %13.4f %11.4f %13.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if (abs(func(x2)) <= tolerance)
        break;
    end
end

if (choice == 2)
    fprintf('%5d %13.4f %11.4f %11.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if (abs(x-x2) <= tolerance)
        break;
    else
        x = x2;
    end
end

if (choice ==3)
    fprintf('%5d %13.4f %11.4f %11.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if(abs(x-x2)/abs(x2) <= tolerance)
        break;
    else
        x = x2;
    end
end
    

end
root = x2;
fx = func(x2);
end