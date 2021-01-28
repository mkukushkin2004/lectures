# int
print(int('20', 3))
print(divmod(20, 3))
print(pow(5, 10))
print(10 | 100, 10 ^ 100, 10 & 100, 10 << 2, 10 >> 2, ~10)
print(bin(5))
print(oct(9))
print(hex(16))

# str
print(str(5), '5' * 3, len('123'))
x = '1234567'
print(x[2:100:2])

#list
A = [s ** 2 for s in range(0, 5)]
print(A)
A.insert(0, 5)
print(A)
print(list('abc'))


#tuple
a = tuple()
print(a)
a = ()
print(a)
a = tuple('Hello')
print(a)
a = '1', '2', 5, [1, 2, 3], ('1', '2'), 5.2
print(a)

#range
a = range(1, 10, 2)
print(a)
print(list(a))

#set
a = set()
print(a)
a = set('abcca')
print(a)
print('a' in a)

#dict
a = {}
print(a)
a = dict([('1', 2), (3, 4)])
print(a, a['1'], a[3])
a[3] = 5
a['long'] = '123'
print(a)
a = dict(short='dict', long='dictionary')
print(a)
a = {
    'dict': 1,
    'dictionary': 2
}
print(a)
a = {a: a ** 2 for a in range(7)}
print(a)
print(a.update({0: 100, 100: 2}))
print(a)
