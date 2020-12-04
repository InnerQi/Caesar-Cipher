# Caesar Cipher challenge

import math

#simple greet function
def greet():
  print('Welcome!')
  print('Willkommen!')
  print('Bienvenido!')

#function with input
def greet_this_person(name):
  print(f'\nWelcome {name}!')
  print(f'How are you today {name}?')

# greet()
# greet_this_person('Grogu')

#function with 2 inputs using positional arguments
def greet_with(name,location):
  print(f'Hello {name}.')
  print(f'What is it like in {location}?')

greet_with('Grogu','Tattooine')

#function with 2 inputs using keyword arguments
greet_with(location='Tattooine', name='Grogu')

#Write your code below this line 👇

def paint_calc(height,width,cover):
  area = test_h * test_w

  #round math result to nearest whole number
  num_of_cans = math.ceil(area/coverage)
  print(f"You will need {num_of_cans} cans of paint to cover that area.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇

def prime_checker(number):
  for n in range(2, number):
    if (number % n == 0):
      print(f"n={n} The number {number} is not a prime")
     
    else:
      print(f"#{n} It is a prime number")
  
            

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
