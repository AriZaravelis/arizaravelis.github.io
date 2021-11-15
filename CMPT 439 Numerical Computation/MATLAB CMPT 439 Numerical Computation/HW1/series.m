function series(x, orderTerm)
% computes and displays the values of sin x as each term in the series is added. 

% input:
%   x = value of your choosing
%   orderTerm = order term of your choosing


% testing: invoke the function in the command window: 
%   e.g., >> series(0.9, 8)



trueValue = sin(x);
sign = -1;
approximation = 0;
order = 0;

fprintf('order   true value      approximation      error\n');

for i=1:2:(orderTerm*2-1)
    sign = (sign) * (-1);
    order = order + 1;
    
    approximation = approximation + ((sign)*((x^i)/(factorial(i))));
    
    error = ((trueValue - approximation) / (trueValue)) * (100);
    
    
    fprintf('%3d %16.10f %16.10f %14.7f\n', order, trueValue, approximation, error);
end


end