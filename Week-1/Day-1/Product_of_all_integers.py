#2Ans Product of all integers

def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
                         
    products_of_all_ints_except_at_index = [None] * len(int_list)
    product_so_far = 1
    
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    product_so_far = 1
    
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index




