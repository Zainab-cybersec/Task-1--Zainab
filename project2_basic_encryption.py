text = input("Enter text: ")
shift = 3 
encrypted = ""
for char in text:
      if char .isalpha(): 
            encrypted +=    chr(ord(char) + shift)
      else :
          encrypted += char 
print("Encrypted Text:" , encrypted)
decrypted = ""
for char in encrypted:
     if char .isalpha():
      decrypted +=    chr(ord(char) -shift)  
     else: 
      decrypted += char 

print("Decrypted Text :" , decrypted)