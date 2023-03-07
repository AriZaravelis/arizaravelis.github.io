function [root,fx,te,iter]=bisection(func,xl,xu,et,maxit)

% input:
% func = name of function
% xl, xu = lower and upper guesses
% et = desired true error (default = 0.00001)
% maxit = maximum allowable iterations (default = 50)

% output:
% root = real root
% fx = function value at root
% te = approximate true error
% iter = number of iterations


if nargin<3,error('at least 3 input arguments required'),end
test = func(xl)*func(xu);
if test>0,error('no sign change'),end
if nargin<4|isempty(et), et=0.00001;end
if nargin<5|isempty(maxit), maxit=50;end

% initialization
iter = 0; xr = xl; te = 100;

% iterative calculation
fprintf('Iteration#     xl          xu          xr          f(xl)          f(xu)          f(xr)          error_a%%\n');
fprintf('%5d %13.4f %11.4f %11.4f %13.4f %14.4f %14.4f %16.4f \n', iter, xl, xu, xr, func(xl), func(xu), func(xr), et );
while (1)
  xrold = xr;
  xr = (xl + xu)/2;
  iter = iter + 1;
  if xr ~= 0,te = xr - xrold;end
  test = func(xl)*func(xr);
  if test < 0
   xu = xr;
  elseif test > 0
    xl = xr;
  else
  te = 0;
  end
  fprintf('%5d %13.4f %11.4f %11.4f %13.4f %14.4f %14.4f %16.4f\n', iter, xl, xu, xr, func(xl), func(xu), func(xr), et );
  if te <= et | iter >= maxit,break,end
end
root = xr; fx = func(xr);
end