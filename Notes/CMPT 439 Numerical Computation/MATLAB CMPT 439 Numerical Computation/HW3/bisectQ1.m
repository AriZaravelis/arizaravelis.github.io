function [root,fx,ea,iter]=bisectQ1(func,xl,xu,es,maxit)

% input:
% func = name of function
% xl, xu = lower and upper guesses
% es = desired relative error (default = 0.05%)
% maxit = maximum allowable iterations (default = 50)

% output:
% root = real root
% fx = function value at root
% ea = approximate relative error (%)
% iter = number of iterations


if nargin<3,error('at least 3 input arguments required'),end
test = func(xl)*func(xu);
if test>0,error('no sign change'),end
if nargin<4|isempty(es), es=0.05;end
if nargin<5|isempty(maxit), maxit=50;end

% initialization
iter = 0; xr = xl; ea = 100;

% iterative calculation
fprintf('Iteration#     xl          xu          xr          f(xl)          f(xu)          f(xr)          error_a%%\n');
fprintf('%5d %13.4f %11.4f %11.4f %13.4f %14.4f %14.4f %16.4f \n', iter, xl, xu, xr, func(xl), func(xu), func(xr), ea );
while (1)
  xrold = xr;
  xr = (xl + xu)/2;
  iter = iter + 1;
  if xr ~= 0,ea = abs((xr - xrold)/xr) * 100;end
  test = func(xl)*func(xr);
  if test < 0
   xu = xr;
  elseif test > 0
    xl = xr;
  else
  ea = 0;
  end
  fprintf('%5d %13.4f %11.4f %11.4f %13.4f %14.4f %14.4f %16.4f\n', iter, xl, xu, xr, func(xl), func(xu), func(xr), ea );
  if ea <= es | iter >= maxit,break,end
end
root = xr; fx = func(xr);
end