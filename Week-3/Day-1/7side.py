def rand5():
    return random.randint(1, 5)


def rand7():

    while True:
		val = rand5()
		if val > 5:
			continue
		else:
			return val

    return 0


print 'Rolling 7-sided die...'
print rand7()