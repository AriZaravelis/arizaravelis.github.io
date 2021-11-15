% Part a
AugMatA = [3 1 -4 7;-2 3 1 -5;2 0 5 10];
x = [0;0;0];
tolerance = 0.0001;
choiceA = input('Enter 1 for MAE. Enter 2 for RMSE. Choose a stopping criterion(MAE or RMSE) for part a: ');

fprintf('Gauss-Seidel Method for part a:\n');
GaussSeidel(AugMatA,x,tolerance,choiceA)

fprintf('Jacobi Method for part a:\n');
Jacobi(AugMatA,x,tolerance,choiceA)



% Part b
AugMatB = [1 -2 4 6;8 -3 2 2;-1 10 2 4];
% Since the Augmented matrix is not diagonally dominant, I reordered it to
% make it diagonally dominant.
AugMatB = [8 -3 2 2;-1 10 2 4;1 -2 4 6];
x = [0;0;0];
tolerance = 0.0001;
choiceB = input('Enter 1 for MAE. Enter 2 for RMSE. Choose a stopping criterion(MAE or RMSE) for part b: ');

fprintf('Gauss-Seidel Method for part b:\n');
GaussSeidel(AugMatB,x,tolerance,choiceB)

fprintf('Jacobi Method for part b:\n');
Jacobi(AugMatB,x,tolerance,choiceB)