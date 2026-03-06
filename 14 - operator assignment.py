# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a =',a)

a += 1 
print('nilai a += 1 :',a)

a -= 2 
print('nilai a -= 1 :',a)

a *= 5 
print('nilai a *= 1 :',a)

a /= 2 
print('nilai a /= 1 :',a)

b = 10
print("\nnilai b =",b)

b %= 3
print('nilai b %= 3 :',b)

b = 10
print("\nnilai b =",b)

b //= 3
print('nilai b //= 3 :',b)

b = 5
print("\nnilai b =",b)

b **= 3
print('nilai b **= 3 :',b)

# operasi bitwise
# OR
c = True
print("\nnilai c =",c)
c |= False
print('nilai c |= False :',c)
c = False
print('nilai c =',c)
c |= False
print('nilai c |= False :',c)

# AND
c = True
print("\nnilai c =",c)
c &= False
print('nilai c &= False :',c)
c = True
print('nilai c =',c)
c &= True
print('nilai c &= True :',c)

# XOR
c = True
print("\nnilai c =",c)
c ^= False
print('nilai c ^= False :',c)
c = True
print('nilai c =',c)
c ^= True
print('nilai c ^= True :',c)

# geser geser
d = 0b0100
print('\nnilai d =',format(d,'04b'))
d >>= 2
print('nilai d >>= 2 :',format(d,'04b'))
d <<= 1
print('nilai d <<= 1 :',format(d,'04b'))