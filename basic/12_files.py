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

file = open('./files/unidata.txt', 'w', encoding='utf-8')
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