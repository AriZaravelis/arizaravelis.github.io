function [estValue,ea,iter] = iterCosFun(x,es,maxit)
% Maclaurin series of cosine function

% input:
%   x = value at which series evaluated
%   es = stopping criterion (default = 0.0001)
%   maxit = maximum iterations (default = 50)

% output:
%   estValue = estimated value
%   ea = approximate relative error (%)
%   iter = number of iterations


% defaults:
if nargin<2|isempty(es),es=0.0001;end
if nargin<3|isempty(maxit),maxit=50;end

% initialization
iter = 1;
sol = 1;
ea = 100;
trueval = cos(x);
er = abs((trueval - sol)/trueval)*100;

% iterative calculation
fprintf('Terms      Result             error_r%%          error_a%%\n');
fprintf('%5d %15.9f %15.9f%% %15.9f%%\n', iter, sol, er, ea );
while (1)
  solOld = sol;
  sol = sol + ((-1)^(iter) * (x)^(2*iter)) / (factorial(2*iter));
  er = abs((trueval - sol)/trueval)*100;
  iter = iter + 1;
  if sol~=0
    ea=abs((sol - solOld)/sol)*100;
  end
  fprintf('%5d %15.9f %15.9f%% %15.9f%%\n', iter, sol, er, ea );
  if ea<=es | iter>=maxit,break,end
end
estValue = sol;

end