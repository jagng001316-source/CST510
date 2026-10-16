'' '' ''
#Adition Quiz
'' '' ''

import random
while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = int(input(f"What is {num1} + {num2}? "))
    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Incorrect. Please try again.")
        

