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