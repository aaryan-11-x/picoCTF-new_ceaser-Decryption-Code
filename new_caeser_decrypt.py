import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def unshift(c, k):
    base16_alphabet = ''
    for x in c:
        base16_alphabet += ALPHABET[ALPHABET.index(x) - ALPHABET.index(k)]
    return base16_alphabet

def b16_decode(decrypt):
    l = ''.join(format(ALPHABET.index(x), '04b') for x in decrypt)
    char, start, stop = [], 0, 8
    for i in range(len(l)//8):
        char.append(l[start:stop])
        start += 8; stop += 8
    # print(char)
    return ''.join(chr(int(i, 2)) for i in char)

print("--------------------------------- picoCTF new_ceaser Decryption Code ----------------------------------------")
print("--------------------------------- Written By Aaryan Golatkar ------------------------------------------------")
enc = input("\n\n Enter The Encrypted Key : ")
for x in ALPHABET:
    decrypt = unshift(enc, x)
    print(f"\nDecrypted With Key {x}: {b16_decode(decrypt)}")