'''
Give a single commmand that computes the sum from exercise r6
'''

def sum_square_odd_int_below(n):
    return sum({k*k for k in range(n-1, 0, -1) if k % 2 != 0})

if __name__ == "__main__":
    print('---Test Function---')
    print(sum_square_odd_int_below(3), 'should be 1.')
    print(sum_square_odd_int_below(5), 'should be 10.')