'''
Write code for function that reverses list of n int
'''
def reverse(num_list):
    length = len(num_list)
    if length == 0:
        return num_list
    else:
        return [num_list[length-1]] + reverse(num_list[:length-1])

if __name__ == "__main__":
    print('---Test Function---')
    print(reverse([1, 2, 3, 4]), 'should be [4, 3, 2, 1].')
    print(reverse([21, 31, 1, 2, 6]), 'should be [6, 2, 1, 31, 21].')