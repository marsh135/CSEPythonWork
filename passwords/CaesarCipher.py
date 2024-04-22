#Caesar Cipher
#take an input string, shift the characters by three letters, 
#then output the resulting string

def encrypt(text, shift):
    result = ""
    
    for l in range(len(text)):
        char = text[l]
        if (char.isupper()):
            result += chr((ord(char)+shift -65) % 26 +65)
        else:
            result += chr((ord(char)+shift -97) % 26 +97)

    return result

def decrypt(text, shift):
    result = ""
    
    for l in range(len(text)):
        char = text[l]

        result += chr((ord(char)-shift))

    return result

print("What would you like to encrypt? :")

text =  input()
shift = 8
print("Original Text: " + text)

print("Shift factor: " + str(shift))
print("Encrypted Message: " + encrypt(text, shift))
result = encrypt(text, shift)
print("Decrypted: "  + decrypt(result, shift))