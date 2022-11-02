print('Welcome to the tip calculator')
total = float(input('What was the total bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
newTotal = total * (tip / 100)
tipTotal = total + newTotal
people = int(input('How many people to split the bill? '))
final = tipTotal / people
newFinal = round(final, 2)
print('each person should pay: $',newFinal)