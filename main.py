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

encrypt_file = r"C:\Users\adamd\Downloads\ThisTextFile.txt"

encrypt_messages = encrypt(encrypt_file)
print(encrypt_messages)
