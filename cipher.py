import string

plain_text = "python is fun!"
shift = 5

alphabet_list = string.ascii_lowercase
shifted = alphabet_list[shift:] + alphabet_list[:shift]
table = str.maketrans(alphabet_list, shifted)

encrypted = plain_text.translate(table)

print(encrypted)


#EXAMPLE OF CREATING A DICTIONARY OF LETTERS AND NUMBERS
# # print(ord("a")) is number 97
# # print(ord("z")) is number 122 which means to 123 to include 122

# alphabet_list = []
# caesar_cipher = {}

# for i in range(97,123):
#     caesar_key = i
#     caesar_value = chr(i)
#     caesar_cipher[caesar_key] = caesar_value

# print(caesar_cipher)


