'''
given n, return sum of squares of all +ve int smaller than n
'''
def sum_sqaure_int_below(n):
    return sum({n*n for n in range(1, n)})

if __name__ == "__main__":
    print('---Test Function---')
    print(sum_sqaure_int_below(3), 'should be 5.')
    print(sum_sqaure_int_below(5), 'should be 30.')