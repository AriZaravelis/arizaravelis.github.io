% f(x) = x^3 - 7*x^2 + 8*x - 0.35


% Determine the three roots graphically
x = linspace(0,6);
y = x.^3 - 7*x.^2 + 8*x - 0.35;
plot(x,y)
title('Plot of y=x^3 - 7*x^2 + 8*x - 0.35')
xlabel('x')
ylabel('y')
grid
% The three roots I've determined from the graph are 0.060, 1.39, and 5.57


% Using the Bisection method
f = @(x) x.^3 - 7*x.^2 + 8*x - 0.35;


% Intial lower and upper guesses:
% xl = -20;
% xu = 20;

fprintf('\nBisection method for root:\n\n');
[cd, fx, et, iter] = bisection(f,-20,20);



% Using False Position method
a = [0,6];
tolerance = 10^-6;
f = @(x) x.^3 - 7*x.^2 + 8*x - 0.35;

fprintf('\nFalse Position method for root:\n\n');
regulaFalsi(f,a(1), a(2), tolerance)


% Using Secant method
a = [0,6];
tolerance = 10^-6;
f = @(x) x.^3 - 7*x.^2 + 8*x - 0.35;

fprintf('\nSecant method for root:\n\n');
secant(f,a(1), a(2), tolerance)


% Using Newton Raphson method
syms x
fm = x^3 - 7*x^2 + 8*x - 0.35;
dfm = diff(fm); %This gives me 3*x^2 - 14*x + 8 as the derivative of the function

% The function is x^3 - 7*x^2 + 8*x - 0.35
% The derivative of this function is 3*x^2 - 14*x + 8
% The initial guess I will use to find the lowest root is 0

fprintf('\nNewton-Raphson method for root:\n\n');
[root1Newton,et,iterNewton1] = newtraph(@(x) x^3 - 7*x^2 + 8*x - 0.35,@(x) 3*x^2 - 14*x + 8,0);

