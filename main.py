"""
Ascii caps_nums list[range A ascii num - Z ascii num]
Ascii low_nums lsit[range a ascii num - z ascii num]
def decrypt:
    make temp string
    read file
    convert to string
    for Strings in list
        for range string.length
            append temp string ascii - 3
    return temp
COMPLETED 4/11/22 NEXT:
def encrypt:
    read file
    put strings in list
    for strings in list
        for chr in strings
            append temp string ascii + 3
    return temp
"""

def decrypt(file):
    strings = []
    decrypt_strings = []
    decrypted = ""
    f = open(f'{file}', 'r')
    for lines in f:
        strings.append(lines.splitlines())
    for texts in strings:
        for letter in texts:
            for char in letter:
                ascii_num = ord(char)
                ascii_num = ascii_num - 3
                if(ascii_num < 65):
                    sub = 65 - ascii_num
                    ascii_num = 91 - sub
                elif(65 < ascii_num and ascii_num < 97):
                    sub = 97 - ascii_num
                    ascii_num = 123 - sub
                the_letter = chr(ascii_num)
                decrypted = decrypted + the_letter
            decrypt_strings.append(decrypted)
            decrypted = ""
    return decrypt_strings

def encrypt(file):
    strings = []
    encrypt_strings = []
    encrypted = ""
    f = open(f'{file}', 'r')
    for lines in f:
        strings.append(lines.splitlines())
    for texts in strings:
        for letter in texts:
            for char in letter:
                ascii_num = ord(char)
                ascii_num = ascii_num + 3
                if(ascii_num > 122):
                    sub = 122 - ascii_num
                    ascii_num = 96 - sub
                elif(90 <  ascii_num and ascii_num < 97):
                    sub = 90 - ascii_num
                    ascii_num = 64 - sub
                the_letter = chr(ascii_num)
                encrypted = encrypted + the_letter
            encrypt_strings.append(encrypted)
            encrypted = ""
    return encrypt_strings

#my_file = r"C:\Users\adamd\Downloads\TestFile.txt"

encrypt_file = r"C:\Users\adamd\Downloads\ThisTextFile.txt"

#messages = decrypt(my_file)

encrypt_messages = encrypt(encrypt_file)
print(encrypt_messages)