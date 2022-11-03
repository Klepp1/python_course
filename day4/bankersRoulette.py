import random

names = input('Who is all in your party today? \n')

name_list = names.split(',')

print(f'{name_list[random.randint(0, len(name_list))]} is paying the bill today!')

