'''
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
'''

def without_end(string1):
    if len(string1) == 2:
        return string1
    else:
        return string1[1:int(len(string1)-1)]

print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))