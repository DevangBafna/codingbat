'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
'''

def first_half(string1):
    num = int(len(string1)/2)
    return string1[0:num]

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
