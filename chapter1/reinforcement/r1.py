# takes in two integer n, m and returns True if n is multiple of m, n = mi
# for some integer i, and False otherwise

def is_multiple(n, m):
    return True if m % n == 0 else False

if __name__ == "__main__":
    print('---Test Function---')
    print(is_multiple(2, 10), 'should be True.')
    print(is_multiple(3, 10), 'should be False.')