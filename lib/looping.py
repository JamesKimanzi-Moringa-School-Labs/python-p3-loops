#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num-=1
    return 'Happy New Year!'

   

int_list1 = ([1, 2, 3, 4, 5])

def square_integers(int_list):
    square_list = [num**2 for num in int_list]
    return square_list
    # squared_ints = list()
    # for num in int_list:
    #     squared_ints.append(num**2)
    # return squared_ints
        

print(square_integers([1, 2, 3, 4, 5, 6]))

def fizzbuzz():
    for num in range(1, 101):
        if num%3 == 0 and num%5 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')    
        else:
            print(num)
print(fizzbuzz())


# for i in range(5, 10):
#     print('looping')
#     print (f'(i is {i})')

# char = 5
# while char < 10:
#     print(f'Character value of is {char}')
#     char = char + 1
#     print('Great looping class')

# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = list()

# for height in player_heights:
#     inch_height = height * 10
#     inch_heights.append (inch_height)

# print(inch_heights)
# print(player_heights)

# ln_cm = [10, 15, 25, 35, 155]

# ln_mm = [item * 10 for item in ln_cm] 
# length_mm = list()

# for item in ln_cm:
#     item = item*10
#     length_mm.append(item)
 
# print(ln_cm)
# print(length_mm)
# print(ln_mm)