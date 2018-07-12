def rand7():
	return random.choice([1,2,3,4,5,6,7])
def rand5():
	while True:
		val = rand7()
		if val > 5:
			continue
		else:
			return val



print 'Rolling 5-sided die...'
print rand5()