'''
    Dictionaries:
        - Known as mappings, are collections of objects storing a key
        for each of them.
        - Can grow and shrink on demand like lists.
'''

D = {'name': 'Raskolnikov', 'punishment': 8, 'crime': 'double murder'}
print(D['name'])
D['punishment'] -= 1
print(D)

E = {}
E['partner'] = 'Sonia'
E['studies'] = 'laws school'
E['age'] = 23
print(E)

raskolnikov = dict(name='raskolnikov', job='presidiary',age=24)
print(raskolnikov)

## zipping
rask = dict(zip(['A','B','C'],['a','b','c']))
print(rask)

rec = {
       'name': {'first': 'Rodia','last': 'raskolnikov'},
       'jobs': ['pres','stud'],
       'age': 24.5
       }
print(rec)
rec['jobs'].append('lawer')
print(rec)
if not 'born' in rec:
    print('missing key')
# or we can use a default value
print(D.get('born',0))
print(D['x'] if 'x' in D else 0)

## accessing a Dictionary with ordered keys
Ks = list(D.keys())
Ks.sort()
print(Ks)
for key in Ks:
    print(key, '=>', D[key])

print()
for key in sorted(E):
    print(key, '=>', E[key])


print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))
D2 = {'punishment': 6, 'sister':'Doria¿'}
D.update(D2)
print(D)
print(D.pop('sister'))
print(D)

table = {1975: 'Holy Grail',
        1979: 'Life of Brian',
        1983: 'The Meaning of Life'}

print(table[1979])
print(list(table.items()))

# Dictionaries for sparse data structrues
Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99
print(Matrix)

X = 2
Y = 3
Z = 4
print(Matrix[(X,Y,Z)])

if (2, 3, 6) in Matrix: 
    print(Matrix[(2, 3, 6)])
else: print(0)


# Zip together keys and values, and some extra comprehensions for dictios
L = list(zip(['a','b'],[1,2]))
print(L)
D = dict(zip(['a','b'],[1,2]))
print(D)

D = {k: v for (k,v) in zip(['a','b'],[1,2])} # equivalent using a comprehension
print(D)

# Sorting dictionaries
D = {'a': 1, 'b': 2, 'c': 3}

Ks = D.keys()
Ks.sort()
for k in Ks: print(k,D[k])

# DBM objets act very much like dictionaries
import dbm

file = dbm.open("./dbm_file",'c')
file['key'] = 'data'
print(file['key'])


## End of chapter 8: quiz
# two ways to build a list with 5 integer zeros
L = [0,0,0,0,0,0,0,0,0,0]
L2 = list((0,0,0,0,0,0,0,0,0,0))
L3 = [0]*10
print(L)
print(type(L))
print(L2)
print(type(L2))
print(L3)

## Name two ways to build a dictionary with two keys, 'a' and 'b', each having an associated value of 0.
D = dict(zip(['a','b'],[0,0]))
D = dict(zip(('a','b'),(0,0)))
D2 = {'a':0,'b':0}
D3 = dict(zip(['a','b'],[0,0]))
D4 = dict(a=0,b=0)
D5 = {}
D5['a'] = 0
D5['b'] = 0
print(D)
print(D2)
print(D3)
print(D4)
print(D5)

## Name 4 operations that change a list object in place.
L[0] = 1
print(L)
L.append(2)
print(L)
L.sort()
print(L)
L.extend([3,4])
print(L)
L.reverse()
print(L)
last = L.pop()
print('extracts %s and leaves the lists as %s' % (last,L))
L.reverse()
L.remove(0)
print(L)
del L[0:2]
print(L)

## Name 4 operations that change a dictionary object in place.
D['a'] = 1
print(D)
D['c'] = 10
del D['b']
print(D)
D.update(D2)
print(D)
c = D.pop('c')
print('extracts the value %s and leaves the dict as %s' % (c,D))

## Why might you use a dictionary instead of a list?
#   Dictionary are more human readible, better when the data is labeled. Lists are better suited to collections
#   of unlabeled data. Dictionary lookup is also usually quicker than searching a list.