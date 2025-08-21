#TASK1
'''
write a function check_even_odd(n) that takes an integer n and returns:
"Even" if the number is even,
"Odd" if the number is odd.
'''
def num():
    number= int(input("Enter number :"))
    if number % 2 == 0 :
        print(f'The number {number} is an even number')
    elif number % 2 == 1 :
        print(f'The number {number} is an odd number')
    else:
        print(f'{number} is not valid,please input a number')
num()
