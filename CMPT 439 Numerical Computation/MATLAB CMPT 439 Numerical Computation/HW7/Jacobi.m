function finalX = Jacobi(AugMat,x,tolerance,choice)

% Input:
% AugMat = An augmented matrix of the system.
% x = A vector of initial approximations for all unknowns.
% tolerance = A tolerance threshold.
% choice = A parameter for choosing a stopping criterion (MAE=1 or RMSE=2).


% Output:
% finalX = Solution vector.


if nargin<4,error('at least 4 input arguments required'),end

A=AugMat(:,1:end-1);
b=AugMat(:,end);

[m,n]=size(A);

if m~=n,error('Matrix A must be square'); end

if (choice~=1 && choice~=2)
    error('Choice must either be 1 for MAE or 2 for RMSE');
end



for i=1:n
    b(i)=b(i)/A(i,i);
    newX(i)=x(i);
    for j=1:n
        if(i~=j)
            A(i,j)=A(i,j)/A(i,i);
        end
    end
end

er=10; %error
iter=0; %iterations

if(choice==1)
    fprintf('Iteration#     x1          x2          x3          MAE\n');
end
if(choice==2)
    fprintf('Iteration#     x1          x2          x3          RMSE\n');
end

while(er>tolerance)
    er=0;
    for i=1:n
        oldX(i)=newX(i);
        newX(i)=b(i);
    end
    for i=1:n
        for j=1:n
            if(i~=j)
                newX(i)=newX(i)-A(i,j)*oldX(j);
            end
        end
        if(choice==1)
            er=er+abs(newX(i)-oldX(i)); % mean absolute error (MAE)
        end
        
        if(choice==2)
            er=er+(newX(i)-oldX(i))^2; % root mean square error (RMSE)
        end
        
    end
    iter=iter+1;
    
    if(choice==1)
        er=er/n; % mean absolute error (MAE)
    end
    
    if(choice==2)
        er=sqrt(er/n); % root mean squaare error (RMSE)
    end
    
    fprintf('%5d %13.4f %11.4f %11.4f %11.4f \n', iter, newX(1), newX(2), newX(3), er);
    
end

newX = newX';
finalX=newX;


end