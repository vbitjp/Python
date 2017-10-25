def factors(n):
	return [i for i in range(1, n + 1) if not n%i]
print("10の素因数=" + str(factors(10)))