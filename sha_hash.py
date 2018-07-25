import hashlib

class sha_hash():
    def __init__(self, key, hashlen):
        self.key = key
        
        der = sum([ord(i) for i in self.key])
        self.hashstart = der % 64
        self.hashlen = hashlen
        
        asciichar = chr(33 + (der % 93))
        asciimult = der % 13

        self.keyx1 = self.sha_it(self.key[::-1])[:4]
        self.keyx2 = asciichar * asciimult
        self.keyx3 = key

    @staticmethod
    def sha_it(s):
        b = hashlib.sha256()
        b.update(s.encode())
        return b.hexdigest().upper()
        
    def hashid(self, id):
        a = '13' + self.keyx1 + id + self.keyx2 + self.keyx3
        return (self.sha_it(a) * 2)[self.hashstart:][:self.hashlen]
        
    def test_key(self):
        x = []
        for i in range(1000):
            for j in range(1000):
                subjid = str(i).zfill(3) + '-' + str(j).zfill(3)

                x.append(self.hashid(subjid))

        return len(set(x)) == len(x)


h = sha_hash("4klfgh6*", 12)
print(h.hashid('101-017'))
print(h.hashid('101-002'))
