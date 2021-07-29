import sys
import hashlib
import string
import secrets

alphabet = string.ascii_letters + string.digits
passwd = ''.join(secrets.choice(alphabet) for i in range(20))
salt = str.encode(passwd);
input = str.encode(sys.argv[1]);
hash = hashlib.sha512(salt+input);
print(hash.hexdigest());
