% This is a script that calls upon the velocity funtion to generate a plot
% of v versus t for t=-5 to 50.


t = -5:50;
vel = [];

for i=1:length(t)
    vel(i) = velocity(t(i));
end

plot(t, vel)
title('Plot of v versus t')
xlabel('time')
ylabel('velocity')
grid