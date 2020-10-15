def cal(i, length):
	if length==1:
		#print("%d %d return %d"%(i, length, 1))
		return 1
	a = 0
	for j in range(1,6):
		if abs(i-j)<=2:
			a = a+cal(j, length-1)
	return a

x=0
for i in range(1,6):
	x=x+cal(i, 4)
print(x)
