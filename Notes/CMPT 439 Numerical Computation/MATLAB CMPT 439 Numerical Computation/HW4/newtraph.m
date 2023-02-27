function [root,ea,iter]=newtraph(func,dfunc,xr,es,maxit)
% newtraph: Newton-Raphson root location zeroes
% [root,ea,iter]=newtraph(func,dfunc,xr,es,maxit):
%   uses Newton-Raphson method to find the root of func

% input:
%   func = name of function
%   dfunc = name of derivative of function
%   xr = initial guess
%   es = desired relative error (default = 0.0001%)
%   maxit = maximum allowable iterations (default = 5)

% output:
%   root = real root
%   ea = approximate relative error (%)
%   iter = number of iterations

if nargin<3,error('at least 3 input arguments required'),end
if nargin<4|isempty(es),es=0.0001;end
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

  if xr ~= 0, ea = abs((xr - xrold)/xr) * 100; end
  if ea <= es | iter >= maxit, break, end
end
root = xr;