# text decryption(P2)
# Prompt the user to enter the path where the text has been encrypted
path = input("Enter the path where your text has been encrypted: ")
try:
    # Attempt to open the file at the specified path in read mode
    with open(path, "r") as f1:
        content = f1.read()
        word = list(content)
        bin = []
        # Iterate over each character in the encrypted text
        for i in word:
            # Remove the 10 added previously to decrypt the binary representation
            bin.append(format(ord(i), "b")[1:])
        new = []
        # Iterate over the decrypted binary values and convert them back to characters
        for i in bin:
            new.append(chr(int(i, 2)))
        # Print the decrypted text
        print("".join(new))
    
    # Prompt the user if they want to add more details or end the process
    write = input("If you want to add more details, write them; otherwise, type 'end': ")
    if write.lower() != "end":
        # Open the file again in append mode to add more details
        with open(path, "a") as f1:
            word = list(write)
            bin = []
            for i in word:
                # Encrypt the additional details
                bin.append(str(int(format(ord(i), "b")) + 10 ** len(format(ord(i), "b"))))
            new = []
            for i in bin:
                new.append(format(chr(int(i, 2))))
                txt = "".join(new)
            # Append the encrypted details to the end of the file
            f1.write("\b{}".format(txt))
except IOError:
    pass