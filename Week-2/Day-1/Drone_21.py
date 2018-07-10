def find_unique_delivery_id(arr):
    histogram = {}

    # O(n) runtime
    for item in arr:
        key = str(item)
        if key in histogram:
            histogram[key] += 1
        else: 
            histogram[key] = 1

    # O(n) runtime
    for k, val in histogram.iteritems():
        if val == 1:
            return int(k)