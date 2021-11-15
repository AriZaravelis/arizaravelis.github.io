x1 = linspace(0,6);

% 4x1 - 8x2 = -24
x2 = -(4/-8)*x1 + (-24/-8);
plot(x1,x2)

hold on

% x1 + 6x2 = 34
x2 = -(1/6)*x1 + (34/6);
plot(x1,x2)

xlabel('x1')
ylabel('x2')
grid