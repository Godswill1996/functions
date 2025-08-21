# TASK2
'''
Write a function count_vowels(text, vowels='aeiou')that counts how many vowels appear in a given text.
example: count_vowels('python is fun') should return 3.
'''

def count_vowels():
    vowels = 'aeiouAEIOU'
    word= input("Enter word :")
    aph= []
    for i in vowels:
        if i in word:
            aph.append(i)
    print(len(aph))
count_vowels()


