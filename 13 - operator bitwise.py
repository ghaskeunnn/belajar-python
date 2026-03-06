a = 9
b = 5

# bitwise OR (|)
c = a | b
print('nilai :',a,' , binary',format(a,'08b'))
print('nilai :',b,' , binary',format(b,'08b'))
print(5*'=','OR (|)')
print('nilai :',c,' , binary',format(c,'08b'))

# bitwise AND (&)
c = a & b
print(5*'=','AND (&)')
print('nilai :',c,' , binary',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print(5*'=','XOR (^)')
print('nilai :',c,' , binary',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print(5*'=','NOT (~)')
print('nilai :',a,' , binary',format(a,'08b'))
print(10*'=',"(^)")
print('nilai :',c,' , binary',format(c,'08b'))
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))

# shifting
# shift right (>>)
c = a >> 2
print('nilai :',a,' , binary',format(a,'08b'))
print(10*'=',">>")
print('nilai :',c,' , binary',format(c,'08b'))

# shift right (<<)
c = a << 2
print('nilai :',a,' , binary',format(a,'08b'))
print(10*'=',"<<")
print('nilai :',c,' , binary',format(c,'08b'))