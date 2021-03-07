'''
Write function that takes a +ve integer n and returns
sums of squares of all odd integers smaller than n
'''

def sum_square_odd_int_below(n):
    if n <= 1:
        return 0
    sum = 0
    for i in range(n-1, 0, -1):
        print(i)
        if i % 2 == 0:
            continue
        else:
            sum += i * i
    return sum

if __name__ == "__main__":
    print('---Test Function---')
    print(sum_square_odd_int_below(3), 'should be 1.')
    print(sum_square_odd_int_below(5), 'should be 10.')