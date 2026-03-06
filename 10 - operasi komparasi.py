# setiap hasil dari komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 8
b = 6

# lebih besar dari >
print(">")
hasil = a > b
print(a,'>',b,'=',hasil)

# Kurang dari <
print("<")
hasil = a < b
print(a,'<',b,'=',hasil)

# lebih dari sama dengan >=
print(">=")
hasil = a >= 8
print(a,'>=',8,'=',hasil)
hasil = b >= 8
print(b,'>=',8,'=',hasil)

# kurang dari sama dengan <=
print("<=")
hasil = a <= 8
print(a,'<=',8,'=',hasil)
hasil = b <= 8
print(b,'<=',8,'=',hasil)

# sama dengan ==
print("==")
hasil = a == 8
print(a,'==',8,'=',hasil)
hasil = b == 8
print(b,'==',8,'=',hasil)

# tidak sama dengan !=
print("!=")
hasil = a != 8
print(a,'!=',8,'=',hasil)
hasil = b != 8
print(b,'!=',8,'=',hasil)

# 'is' sebagai komparasi object identity
print("is")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print("is not")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)