from itertools import combinations 
ops = {'/':lambda x,y:float(x)/y, '+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}

# numbers is a list of integer
# this function returns all possible expressions with numbers as leaves
# each expression is expressed by a dict containning type, val, left, right.
# type is: 'leaf', '+', '-', '*', '/'
# left and right are also expressions.
def get_sub_exp(numbers):
	if len(numbers) == 1:
		return [{'type':'leaf', 'val':numbers[0]}]
	# divide numbers into 2 sets. generate all such pairs.
	pairs = get_pairs(numbers)
	exps = list()	
	for pair in pairs:
		exps1 = get_sub_exp(pair[0])
		exps2 = get_sub_exp(pair[1])
		for exp1 in exps1:
			for exp2 in exps2:
				for key in ops:
					if key != '/' or exp2['val']!=0:
						exps.append(gen_exp(key, exp1, exp2))
					if key != '/' or exp1['val']!=0:
						exps.append(gen_exp(key, exp2, exp1))
	return exps

# generate an expression dict with key, left and right operands
def gen_exp(key, exp1, exp2):
	val = ops[key](exp1['val'],exp2['val'])
	exp = {'type':key, 'val':val, 'left':exp1, 'right':exp2}
	return exp


# divide numbers into 2 parts. generate all divisions.
def get_pairs(numbers):
	#print "get pairs", numbers
	indices = range(len(numbers))
	pairs = list()
	max_comb = len(numbers)/2+1
	for i in range(1, max_comb):
		combs = combinations(indices, i)
		for c in combs:
			left = list()
			right = list()
			for index in range(len(numbers)):
				if index in c:
					left.append(numbers[index])
				else:
					right.append(numbers[index])
			pairs.append((left, right))
	#print pairs
	return pairs

def show_exp(expression):
	if expression['type'] != 'leaf':
		print('('),
		show_exp(expression['left'])
		print(expression['type']),
		show_exp(expression['right']) 
		print(')'),
	else:
		print(expression['val']),

def main():
	exps = get_sub_exp([3,5,13,9,11])
	target = 72

	for exp in exps:
		result = exp['val']
		if abs(target-result)<0.001:
			show_exp(exp)
			print ' = ', result

if __name__== "__main__":
  main()
