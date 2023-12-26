text = 'Hello Zaira'
shift = 3

def caesar(message, offset, direction = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append space to the message
        if not char.isalpha():
            final_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return caesar(message, key)
    
def decrypt(message, key):
    return caesar(message, key, -1)

encode = encrypt(text, shift)
decode = decrypt(encode, shift)

print(encode, decode)