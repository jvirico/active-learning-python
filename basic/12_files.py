'''
    FILES
'''

# file creation
f = open('./files/data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

# reading file
f = open('./files/data.txt')
text = f.read()
print(text)

print(text.split())

# using an iterator
for line in open('./files/data.txt'): print(line)

## Binary files

import struct

packed = struct.pack('>i4sh', 7, b'spam',8)
print(packed)

file = open('./files/data.bin','wb')
file.write(packed)

file.close()

# reading back binary files
data = open('./files/data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))

d = struct.unpack('>i4sh',data)
print(d)

## Unicode text files
S = 'sp\xc4m'
print(S)
print(S[2])

file = open('./files/unidata.txt', 'w', encoding='utf-8') # encoding param does not work in 2.X pythons
file.write(S)
file.close()

text = open('./files/unidata.txt', encoding='utf-8').read()
print(text)

raw = open('./files/unidata.txt','rb').read()
print(raw)

print(text.encode('utf-8'))
print(raw.decode('utf-8'))
print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))


## More on Files
myfile = open('./files/myfile.txt','w')
myfile.write('this is an example line ;)\n')
myfile.write('and now I close the file\n')
myfile.close()

# now ways to read files
myfile = open('./files/myfile.txt','r')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close()
print(open('./files/myfile.txt','r').read()) # reading all content
# file iterator
for line in open('./files/myfile.txt'):
    print(line,end='')
    print('new line')

## Difference between Text files and Binary files
#       Text files perform Unicode encodings and enf-of-line translation by default.
#       Binary files allow programs to access file content unaltered.

### Pickle files
D = {'a':1,'b':2}
F = open('./files/datafile.pkl','wb')
import pickle
pickle.dump(D,F)
F.close()

#getting D back
F = open('./files/datafile.pkl','rb')
E = pickle.load(F)
print(E)

### Json files
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
# we need to translate dict format to json enconding
import json
rec = json.dumps(rec)
print(rec)
# saving it to file
F = open('./files/datafile.json','w')
json.dump(rec,F)

