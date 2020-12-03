# Caesar Cipher challenge

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
  num_cans = (test_h * test_w) / coverage
  new_num = round(num_cans)
  print(new_num)

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


