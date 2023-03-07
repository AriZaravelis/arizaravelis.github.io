function [root]=secant(func,x0,x1,tolerance,choice)

% input:
% func = name of function
% x0, x1 = initial guesses
% tolerance = tolerance threshold

% choice = one of the three stopping criterias. 
% If user input 1, true error is used to stop the process.
% If user input 2, absolute approximate error is used to stop the process.
% If user input 3, relative approximate error is used to stop the process.


% output:
% root = real root


if nargin<5,error('at least 5 input arguments required'),end

% initialization
iter = 0;

if (abs(func(x0)) < abs(func(x1))) %if true swap x0 and x1
    temp = x0;
    x0 = x1;
    x1 = temp;
end
    

fprintf('Iteration#     x0          x1          f(x0)          f(x1)\n');
fprintf('%5d %13.4f %11.4f %13.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
while(1)
    
iter = iter + 1;
    
x2 = x1 - func(x1) * (x0-x1)/(func(x0)-func(x1));
x0 = x1;
x1 = x2;

    
if (choice == 1)
    fprintf('%5d %13.4f %11.4f %13.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if (abs(func(x2)) <= tolerance)
        break;
    end
end

if (choice == 2)
    fprintf('%5d %13.4f %11.4f %11.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if (abs(x0-x1) <= tolerance)
        break;
    end
end

if (choice ==3)
    fprintf('%5d %13.4f %11.4f %11.4f %13.4f \n', iter, x0, x1, func(x0), func(x1) );
    if(abs(x0-x1)/abs(x1) <= tolerance)
        break;
    end
end
    

end
root = x2;

end