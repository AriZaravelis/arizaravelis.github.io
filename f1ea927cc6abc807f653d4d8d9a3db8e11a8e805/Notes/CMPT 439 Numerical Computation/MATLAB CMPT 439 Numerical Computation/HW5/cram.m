function [solution] = cram(augMatrix)

% Input:
% augMatrix = augmented matrix of the system.

% Output:
% solution = vector containing the solutions.


A = augMatrix(:,1:end-1);
b = augMatrix(:,end);
D = det(A);


D1 = A;
D1(:,1)=b;
D1 = det(D1);
x1 = D1/D;


D2 = A;
D2(:,2)=b;
D2 = det(D2);
x2 = D2/D;


D3 = A;
D3(:,3)=b;
D3 = det(D3);
x3 = D3/D;


if(D == 0)
    solution = [];
    fprintf('The system is singular\n')
else
    solution = [x1;x2;x3];


end