# Caesar Cipher challenge 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

# Enter command to either encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Enter message to be encoded or decoded
text = input("Type your message:\n").lower()

# Enter no. of letters to shift 
shift = int(input("Type the shift number:\n"))

# Function to encrypt message using shift value
def encrypt(plain_text, shift_value):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_value
    cipher_text += alphabet[new_position]  
  print(f"The encoded text is {cipher_text}")

# Function to decrypt message using shift value
def decrypt(cipher_text, shift_value):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_value  
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_value=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_value=shift)
