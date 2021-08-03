import sys
import hashlib

input = str.encode(sys.argv[1]);
hash = hashlib.pbkdf2_hmac('sha512', input, b'Km5d5ivMy8iexuHcZrsD', 200000);
print(hash.hex());
