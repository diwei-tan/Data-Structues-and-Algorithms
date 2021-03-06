# take +ve integer > 2 and output no. of time one must repeatedly
# divide by 2 before getting a value < 2

def num_of_halves(num):
    if num < 2:
        return 0
    else:
        return 1 + num_of_halves(num/2)

if __name__ == "__main__":
    print('---Test Function---')
    print(num_of_halves(2), 'should be 1.')
    print(num_of_halves(16), 'should be 4.')
    print(num_of_halves(21), 'should be 4.')