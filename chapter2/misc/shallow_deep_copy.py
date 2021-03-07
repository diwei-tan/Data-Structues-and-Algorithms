'''
Demonstrates shallow and deep copying and cautions on python lists
Python lists are referential!!
'''
import copy

class Number:
    def __init__(self, a):
        self.num = a

if __name__ == "__main__":
    list_a = [Number(1), Number(2), Number(3), Number(4), Number(5), Number(6)]
    list_b = list_a # reference
    list_c = list(list_a) # does not seem like reference
    list_a[0].num = 10
    print('When changing value of element 0 from 1 to 10, see that ALL three lists change!')
    print([n.num for n in list_a])
    print([n.num for n in list_b])
    print([n.num for n in list_c])

    list_a[0] = Number(5)
    print('When changing element 0 object, see that a, b change but c remains as it is still referencing older object value 10!')
    print([n.num for n in list_a])
    print([n.num for n in list_b])
    print([n.num for n in list_c])

    list_d = copy.deepcopy(list_a)
    list_a[0].num = 25
    print('When change value of element 0 to 25, seel that ALL except deepcopy list_d change!')
    print([n.num for n in list_a])
    print([n.num for n in list_b])
    print([n.num for n in list_c])
    print([n.num for n in list_d])