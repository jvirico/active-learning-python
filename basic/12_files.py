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