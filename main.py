import hashlib
s='gammaomega'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
