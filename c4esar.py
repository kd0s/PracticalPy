import string

def caesar(text, shift, table=string.ascii_lowercase):
    cipher_table = table[shift:] + table[:shift]
    return text.translate(text.maketrans(table, cipher_table))

message = input("type message to encode:")
shift = int(input("Enter number to code:"))
print(caesar(message.lower(), shift))