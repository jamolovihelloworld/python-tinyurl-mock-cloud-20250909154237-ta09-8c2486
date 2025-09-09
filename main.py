import hashlib
s='clouddelta'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
