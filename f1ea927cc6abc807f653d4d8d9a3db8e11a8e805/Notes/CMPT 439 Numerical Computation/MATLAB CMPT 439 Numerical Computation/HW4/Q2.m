% Find the two positive roots of f(x)=7*sin(x)*exp(-x)-1


% Graphically
x = linspace(0,3);
y = 7*sin(x).*exp(-x)-1;
plot(x,y)
title('Plot of y=7*sin(x)*exp(-x)-1;')
xlabel('x')
ylabel('y')
grid


% Using the Newton-Raphson method
syms x
fm = 7*sin(x)*exp(-x)-1;
dfm = diff(fm); %This gives me 7*exp(-x)*cos(x) - 7*exp(-x)*sin(x) as the derivative of the function

% The function is 7*sin(x)*exp(-x)-1
% The derivative of this function is 7*exp(-x)*cos(x) - 7*exp(-x)*sin(x)
% The initial guess I will use to find the first positive root is 0.1
% The initial guess I will use to find the second positive root is 1.8

fprintf('\nNewton-Raphson method for root#1\n\n');
[root1Newton,ea1,iterNewton1] = newtraph(@(x) 7*sin(x)*exp(-x)-1,@(x) 7*exp(-x)*cos(x) - 7*exp(-x)*sin(x),0.1);

fprintf('\nNewton-Raphson method for root#2\n\n');
[root2Newton,ea2,iterNewton2] = newtraph(@(x) 7*sin(x)*exp(-x)-1,@(x) 7*exp(-x)*cos(x) - 7*exp(-x)*sin(x),1.8);

% Using the secant method
% The inital two guesses for the first root is 0.3 and 0.4
% The inital two guesses for the second root is 2 and 2.1

fprintf('\nSecant method for root#1\n\n');
[root1Secant]=secant(@(x) 7*sin(x)*exp(-x)-1,0.3,0.4,10^-6,1);


fprintf('\nSecant method for root#2\n\n');
[root2Secant]=secant(@(x) 7*sin(x)*exp(-x)-1,2,2.1,10^-6,1);