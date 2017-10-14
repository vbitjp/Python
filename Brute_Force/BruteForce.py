import multiprocessing
from hashlib import sha256

def HashGen(hex1):
    divisor = 456976
    letterList = []
    for i in range(5):
        letter, hex1 = divmod(hex1, divisor)
        divisor /= 26
        letterList.append( int(letter) + 97)
    return (letterList, sha256(bytes(letterList)).digest())

h1 = bytes().fromhex("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b")
numpassword = int(26 ** 5)
chunk = int(numpassword / multiprocessing.cpu_count())
with multiprocessing.Pool() as p:
	for (letters, digest) in p.imap_unordered(HashGen, range(numpassword), chunk):
		if digest == h1:
			password = "".join(chr(x) for x in letters)
			print(password + " => " + digest.hex())