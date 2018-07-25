import hashlib

key = '8sJ55t5!'
hashlen = 12

def sha_it(s):
    b = hashlib.sha256()
    b.update(s.encode())
    return b.hexdigest().upper()

der = sum([ord(i) for i in key])
prekey = sha_it(key[::-1])[:4]

hashstart = der % 64
asciichar = chr(der % 128)
asciimult = der % 13

x = []
for i in range(1000):
    for j in range(1000):
        subjid = str(i).zfill(3) + '-' + str(j).zfill(3)
        
        a = '13' + prekey + subjid + asciichar * asciimult + key
        x.append((sha_it(a) * 2)[hashstart:][:hashlen])

print('Key: ' + key)
print('Hash Start: ' + str(hashstart))
print(len(set(x)))
print(len(set(x)) == len(x))


'''
SAS CODE:
==================
data a;
  do i=0 to 20;
    SUBJID = '000-'||put(i,z3.);
    output;
  end;
run;
data a(keep=subjid hash);
  set a;
  key='8sJ55t5!';
  keylen = 12;
  prekey = substr(put(sha256(compress(reverse(key))), $hex64.),1,4);
  s=0;
  do i =1 to length(key);
    s = s+rank(substr(key,i,1));
  end;
  start=mod(s,64);
  asc = byte(mod(s,128));
  ascn = mod(s,13);
  sha=repeat(put(sha256('13'||compress(prekey)||compress(SUBJID)||repeat(asc,ascn-1)||compress(key)), $hex64.),1);
  hash = substr(sha,start+1,keylen);
run;
'''
