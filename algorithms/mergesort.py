def mergesort(inp):
	print inp
	if len(inp) <= 1:
		return inp
	else:
		left = inp[0:(len(inp)/2)]
		right=inp[(len(inp)/2):]
		
		mergesort(left)
		mergesort(right)
		l, r = 0, 0
		for i in range(0, len(inp)):
			lval = left[l] if l <len(left) else None
			rval = right[r] if r < len(right) else None
			"""if (lval and rval and lval < rval) or rval is None:
				inp[i] = lval
				l += 1
			elif (lval and rval and lval >= rval) or lval is None:
				inp[i] = rval
				r += 1"""
			if (lval and rval and lval<=rval )or rval is None:
				inp[i] = lval
				l+=1
			elif (lval and rval and lval>rval )or lval is None:
				inp[i] = rval
				r+=1
		return inp
print mergesort([4,1,5,2,8,9,4,2,6,8])

