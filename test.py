from base64 import b85decode, b85encode
from codecs import decode

uri = b"https://licensing.sr.flipr.ai/api/actions/validate/"
ct = b"Content-Type"
appjson = b"application/json"
email = b"email"
key = b"key"
acc = b"Accept"
sus = b"SUSPENDED"
inv = b"INVALID"
exp = b"EXPIRED"
usm = b"USER_SCOPE_MISMATCH"

ex1 = b"License is suspended. Please contact the library administrator.\n"
ex2 = b"Invalid License Key. Please recheck license_key.\n"
ex3 = b"License Key has been expired.\n"
ex4 = b"Incorrect email id. Verify email id.\n"
ex5 = b"License validation request could not be made. Please make sure you are connected to the internet.\n"

print(decode(uri), " | ", (b85encode(uri)))
print(ct, " | ", (b85encode(ct)))
print(appjson, " | ", (b85encode(appjson)))
print(email, " | ", (b85encode(email)))
print(key, " | ", (b85encode(key)))
print(acc, " | ", (b85encode(acc)))

print(sus, " | ", (b85encode(sus)))
print(inv, " | ", (b85encode(inv)))
print(exp, " | ", (b85encode(exp)))
print(usm, " | ", (b85encode(usm)))
print(ex1, " | ", (b85encode(ex1)))
print(ex2, " | ", (b85encode(ex2)))
print(ex3, " | ", (b85encode(ex3)))
print(ex4, " | ", (b85encode(ex4)))
print(ex5, " | ", (b85encode(ex5)))