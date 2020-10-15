data = [1,4, 9, 16, 25]

numbers = set()
for i in data:
	for j in data:
		for m in data:
			for n in data:
				s = i+j+m+n
				if not s in numbers:
					numbers.add(s)
					print("%d + %d + %d + %d = %d"%(i,j,m,n,s))

print(numbers)
