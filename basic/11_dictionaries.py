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