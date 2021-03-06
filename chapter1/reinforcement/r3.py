'''
Write minmax(data), that takes seq of 1 or more num and return (min, max) tuple
'''

def minmax(data):
    min_num = float('inf')
    max_num = float('-inf')
    for num in data:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return min_num, max_num

if __name__ == "__main__":
    print('---Test Function---')
    print(minmax([1]), 'should be (1, 1).')
    print(minmax([1, 2, 3, 4, 5, 15, 17]), 'should be (1, 17).')