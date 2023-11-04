# Straightforward Text Encryption and Decryption Utility

This code serves as a tool for encrypting and decrypting text using a simple binary encoding method. The program is divided into two parts.

In the first part (Text Encryption - P1), the code initiates by requesting the user to define a path for saving the encrypted text. It then proceeds to open a file at the specified path in write mode, prompting the user to input the text they wish to encrypt. Each character in the input text is converted into a binary representation, with 10 added to the binary value. Subsequently, the modified binary values are converted back into characters, and the resulting encrypted text is written to the designated file. This section of the code is tailored for text encryption and offers the flexibility to customize the output file's location.

The second part of the code assumes the role of text decryption and the potential addition of supplementary content. Initially, it prompts the user to specify the path to the file containing the encrypted text. It then opens the file in read mode, reverses the binary transformations applied during encryption, and displays the decrypted text. Users are given the option to append more details to the file or conclude the process by typing 'end.' If additional information is desired, the code opens the file in append mode, encrypts the new content, and appends it to the end of the file. This section of the code ensures the decryption of previously encrypted text and facilitates the expansion of content within the same file.

Both parts of the code have been enhanced to allow users the flexibility of specifying file paths, making it a versatile tool for text encryption, decryption, and content management.
