% Evaluate the polynomial y = ?x^3 + 9x^2 ? 11x + 0.75
p = [-1 9 -11 0.75];
true = polyval(p,1.36);

x3 = round(-1.36^3,3,'significant');
x2 = round(9*1.36^2,3,'significant');
x1 = round(11*1.36,3,'significant');
x0 = 0.75;

approx = x3 + x2 - x1 + x0;

re = abs((true-approx)/true)*100;


% Evaluate the polynomial y = ((?x + 9)x ? 11)x + 0.75
% I simplified to this: y = -x^3 + 9x^2 - 11x + 0.75
p = [-1 9 -11 0.75];
true = polyval(p,1.36);

x3 = round(-1.36^3,3,'significant');
x2 = round(9*1.36^2,3,'significant');
x1 = round(11*1.36,3,'significant');
x0 = 0.75;

approx = x3 + x2 - x1 + x0;

re = abs((true-approx)/true)*100;