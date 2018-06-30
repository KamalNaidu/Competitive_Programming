def fib(n):
    if n<2 : return n
    else: return fib(n-1) + fib(n-2)

#using dicts (optimized): we can reduce the complexity of recursive function
#call by remembering the results of each function call and thus reusing
#the value straight away with out function call
def fibonacci(n):
    if n<2 : return n
    elif n not in fib_dict :
            fib_dict[n]= fibonacci(n-1) + fibonacci(n-2)
    return fib_dict[n]