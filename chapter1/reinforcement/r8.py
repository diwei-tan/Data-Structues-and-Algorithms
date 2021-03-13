'''
for string s length n, find expression s[k] where -n <= k <= 0 and s[j] where j >= 0
such that s[k] and s[j] are the same element?
'''

if __name__ == "__main__":
    string = 'abcdefghijklmnopqrstuvwxyz'
    n = len(string)
    k = -5
    j = n + k
    print('s[k]: {} is same element as s[j]: {}'.format(string[k], string[j]))
