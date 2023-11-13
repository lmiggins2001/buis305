number = int(input('Enter a number: '))
if number % 3 == 0:
   print(number, 'Tic')




elif number % 5 == 0:
   print(number, 'Tac')




elif number % 3 == 0 and number % 5 == 0:
   print(number, 'Tic Tac')




else:
   print('The number is not divisible by 3 or 5')

current_number = 1


while current_number <= 20:
   if current_number % 3 == 0:
       print(current_number, 'Tic')


   elif current_number % 5 == 0:
       print(current_number, 'Tac')


   else:
       print(current_number)


   current_number += 1

import random
random_number = random.randint(1, 20)
print(random_number)

attempts = 0


while attempts < 5:
   user_input = input("Enter a value (greater than 0): ")


   try:
       value = int(user_input)
       if value > 0:
           print("You entered a valid value:", value)
           break
       else:
           print("Value must be greater than 0. Try again.")
   except ValueError:
       print("Invalid input. Please enter a valid integer.")


   attempts += 1


if attempts == 5:
   print("Exceeded maximum attempts. Please run the program again.")


import random


attempts = 0


while attempts < 5:
   user_input = input("Enter a value (greater than 0): ")


   try:
       value = int(user_input)
       if value > 0:
           print("You entered a valid value:", value)




           random_value = random.randint(1, 20)
           print("Randomly generated value:", random_value)


           #
           if value == random_value:
               print("Perfect match!")
           else:
               print("Numbers don't match.")


           break
       else:
           print("Value must be greater than 0. Try again.")
   except ValueError:
       print("Invalid input. Please enter a valid integer.")


   attempts += 1


if attempts == 5:
   print("Exceeded maximum attempts. Please run the program again.")