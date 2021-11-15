function [root,te,iter]=newtraph(func,dfunc,xr,et,maxit)
% newtraph: Newton-Raphson root location zeroes
% [root,ea,iter]=newtraph(func,dfunc,xr,es,maxit):
%   uses Newton-Raphson method to find the root of func

% input:
%   func = name of function
%   dfunc = name of derivative of function
%   xr = initial guess
%   et = desired true error (default = 0.00001)
%   maxit = maximum allowable iterations (default = 5)

% output:
%   root = real root
%   te = approximate true error
%   iter = number of iterations

if nargin<3,error('at least 3 input arguments required'),end
if nargin<4|isempty(et),et=0.0001;end
if nargin<5|isempty(maxit),maxit=5;end
iter = 0;

fprintf('Iteration#     xr          f(xr)\n');
fprintf('%5d %13.4f %11.4f \n', iter, xr, func(xr) );
while (1)
  xrold = xr;
  xr = xr - func(xr)/dfunc(xr);
  iter = iter + 1;
  
  fprintf('Iteration#     xr          f(xr)\n');
  fprintf('%5d %13.4f %11.4f \n', iter, xr, func(xr) );

  if xr ~= 0, te = xr - xrold; end
  if te <= et | iter >= maxit, break, end
end
root = xr;