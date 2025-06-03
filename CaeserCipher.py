def encryption(simplexp, d):
    soln = ""
    for char in simplexp:
        if not char.isalpha():
            soln += char
        elif char == " ":
            soln += " "
        elif char.isupper():
            soln += chr((ord(char) + d - 65) % 26 + 65)
        else:
            soln += chr((ord(char) + d - 97) % 26 + 97)  
    return soln.upper()  # Convert the entire string to uppercase

d = int(input())
simplexp = input()
print (encryption(simplexp,d))
