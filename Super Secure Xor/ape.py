import binascii
# flag = 'StormCTF{Crypto4:blah;blaghjhblah}'
# flag_rev = list(flag[::-1])
# stuff = zip(flag, flag_rev)
# x = lambda x,y: chr(ord(x) ^ ord(y))
# out = list()
# out += [x(s[0],s[1]) for s in stuff]
# print(out)
# final = [str(b, 'ascii') for b in [binascii.hexlify(bytes(x, 'utf-8')) for x in out]]
# print(''.join(final))
# print('2e1209315c05627148004b3b46160a565858560a16463b4b00487162055c3109122e')

# stuff = zip(flag, flag_rev)
# x = lambda x,y: ord(x) ^ ord(y)
# out = list()
# out += [x(s[0],s[1]) for s in stuff]
# print(list(stuff))
# print(out)

out = list(binascii.unhexlify('2e1209315c05627148004b3b46160a565858560a16463b4b00487162055c3109122e'))
out = [chr(val) for val in out]
print(out)
x = lambda x,y: chr(ord(x) ^ ord(y))

flag = 'StormCTF{Crypto4:blah;blaghjhblah}'
flag_rev = list(flag[::-1])

stuff = zip(flag_rev, out)
out = list()
out += [x(s[0],s[1]) for s in stuff]
print(''.join(out))
