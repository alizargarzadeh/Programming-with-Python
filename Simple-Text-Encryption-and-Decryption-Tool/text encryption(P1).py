#  text encryption(P1)
# Prompt the user to enter the path where they want to save the encrypted text
path = input("Enter the path where you want to save your text: ")
try:
      # Attempt to open the file at the specified path in write mode
      with open(path, "w") as f1:
            # Prompt the user to enter the text they want to encrypt
            content = input("Enter your text: ")
            word = list(content)
            bin = []
            # Iterate over each character in the input text
            for i in word:
            # Convert the character to binary and add 10 to the binary value
                  bin.append(str(int(format(ord(i), "b")) + 10 ** len(format(ord(i), "b"))))
            new = []
            # Iterate over the modified binary values and convert them back to characters
            for i in bin:
                  new.append(format(chr(int(i, 2))))
            # Write the encrypted text to the file
            f1.write("".join(new))
except IOError:
      pass