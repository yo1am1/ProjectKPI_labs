%ФЕ-21 Трепалін Єгор. Лабораторна робота №8%

a = input("Enter the a matrix: ")
c = input("Enter the c matrix: ")

d = a*c

t=size(d);
m=d(1,1);
for i=1:t(1)
    for j=1:t(2)
        if d(i,j)>m
        m=d(i,j);
        end
    end
end

disp(m)
d(1,1)=m