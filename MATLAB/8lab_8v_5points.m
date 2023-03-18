%group name. Лабораторна робота №8. Варіант 8%

a = input("Enter the a vector: ")
c = input("Enter the c vector: ")

el_a = a(find(mod(a, 2)==0))
el_c = c(find(mod(c, 2)==0))

sel_a=sum(el_a)
sel_c=sum(el_c)

if sel_a==sel_c
    a_flip=flip(a)
    c_flip=flip(c)
end