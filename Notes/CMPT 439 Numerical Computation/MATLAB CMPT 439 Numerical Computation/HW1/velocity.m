function vel = velocity(t)
% This function computes v as a function of t.


if(t >= 0 && t <=8)
    vel = 10*t^2 - 5*t;
    
elseif(t >= 8 && t <=16)
    vel = 624 - 3*t;

elseif(t >= 16 && t <= 26)
    vel = 36*t + 12*(t-16)^2;
    
elseif(t > 26)
    vel = 2136*exp(-0.1*(t-26));

else
    vel = 0;

end


end