a = [-7,-5];
b = [-5,-3];
tolerance = 10^-6;

f=@(x) 2*sin(x)-exp(x)/4-1;

choice = input('Enter 1 to use true error. Enter 2 to use absolute approximate error. Enter 3 to use relative approximate error:');

regulaFalsi(f,a(1), a(2), tolerance, choice)
regulaFalsi(f,b(1), b(2), tolerance, choice)