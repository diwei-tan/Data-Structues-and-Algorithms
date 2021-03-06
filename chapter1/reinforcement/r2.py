'''
Function is_even(k) that returns True if k is even, otherwise, false.
Cannot use multiplication, divison, or modulo.
'''

def is_even(k):
    if k == 0:
        return True
    elif k < 0:
        return False
    else:
        return is_even(k-2)

if __name__ == "__main__":
    print('---Test Function---')
    print(is_even(40), 'should be True.')
    print(is_even(51), 'should be False.')