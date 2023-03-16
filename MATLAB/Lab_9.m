x = [-2 : 0.3: 3.1];
y = abs(x.^3 - 4.2 .* x.^2) + cos(5.*x) .* sin(3.*x);
subplot(2, 2, 1)
plot(x, y, 'r'), grid on, xlabel('x'), ylabel('y'), title('y = |x^3 - 4.2x^2| + cos(5x)*sin(3x)');
z = [1 : 0.01: 3];
y1 = exp(-2*z).*sin(10*z);
subplot(2,2,2)
plot(z, y1, 'g'), grid on, xlabel('x'), ylabel('y'), title('y = exp(-2*x)*sin(10*x)');
y2 = sin(6*z).*cos(exp(z));
subplot(2, 2, 3)
plot(z, y2, 'c'), grid on, xlabel('x'), ylabel('y'), title('y = sin(6*x)*cos(exp(z))');
y3 = cos(6*z).^((3-z)/(5+z));
subplot(2, 2, 4)
plot(z, y3, 'm'), grid on, xlabel('x'), ylabel('y'), title('y = cos(6*z)^((3-z)/(5+z))');