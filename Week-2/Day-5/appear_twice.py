
def find_repeat(arr):

    counter = [0] * (len(arr) + 1)

    for item in arr:
        counter[item] += 1

    return counter.index(2)