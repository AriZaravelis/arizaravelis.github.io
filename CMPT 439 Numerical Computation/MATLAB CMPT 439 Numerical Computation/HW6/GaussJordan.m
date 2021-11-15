function x = GaussJordan(Aug)
% input:
%   Aug = Augmented matrix

% output:
%   x = solution vector

A = Aug(:,1:end-1);

[m,n] = size(A);
if m ~= n, error('Matrix A must be square'); end
nb=n+1;


for k = 1:n
    Aug(k,1:nb) = Aug(k,1:nb) * (1/Aug(k,k));
    for i = 1:n
        if(i == k)
            Aug(k,1:nb) = Aug(k,1:nb);
        else
            Aug(i,1:nb) = Aug(i,1:nb) - (Aug(k,1:nb)*Aug(i,k));
        end
    end
end


x = zeros(m,1);
for i = 1:n
    x(i,:) = Aug(i,nb);
end