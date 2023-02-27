format long;

epsilon = 1;

while (1+epsilon > 1)
    epsilon = epsilon/2;
end

epsilon = 2*epsilon; %machine epsilon

trueValue = eps; %true value of epsilon

ea = abs(trueValue - epsilon); %absolute error
er = abs(ea / trueValue); %relative error
ep = er * 100; % percentage error


display(epsilon);
display(trueValue);
display(ea);
display(er);
display(ep);