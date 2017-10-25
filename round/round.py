def round(x,d=0):
	p=10**d
	return (x*p*2+1)//2/p
print("10.5の小数点第1位で四捨五入:" + str(round(10.5, 1)))
print("10.5の小数点第0位で四捨五入:" + str(round(10.5, 0)))