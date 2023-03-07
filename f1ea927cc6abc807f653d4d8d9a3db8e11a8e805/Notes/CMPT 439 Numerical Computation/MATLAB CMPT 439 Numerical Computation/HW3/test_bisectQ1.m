% Example: employ the bisect function to solve the bungee-jumper problem
g = 9.81;
f = @(cd,m,v,t) sqrt(g*m/cd)*tanh(sqrt(g*cd/m)*t)-v;

% To determine the drag coefficient of the bungee jumper needed so that
% a 95-kg bungee jumper has a velocity of 46 m/s after 9s of free fall.

% Find the root of fm with m = 95, v = 46 and t = 9;

% Intial lower and upper guesses:
% xl = 0.2;
% xu = 0.5;


[cd, fx, ea, iter] = bisectQ1(@(cd) f(cd,95,46,9),0.2,0.5)