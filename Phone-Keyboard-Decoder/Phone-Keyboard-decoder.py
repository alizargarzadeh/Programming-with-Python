## Prompt the user to enter a number
text = input("Enter your number: ") 
text = list(text)  
## Initialize an empty set to track unique characters
set = set()
## Add the first character to the set
set.add(text[0])
## Initialize a list to track consecutive character counts
count = []  
## Initialize a list to store characters from the same keyboard key
keyboard = []  
i = 1  
count.append(i) 
for j in range(1, len(text)):
    set.add(text[j]) 
    if len(set) == 1:  
        i += 1  
        if i >= 2:
            count.pop() 
    else:
        i = 1 
            ## Add the previous character to the keyboard list
        keyboard.append(text[j - 1]) 
        set.remove(text[j - 1]) 
    count.append(i)  
keyboard.append(text[j]) 

## Remove spaces from the keyboard list
for i in text:
    if " " in keyboard:
        count.pop(keyboard.index(" "))
        keyboard.remove(" ")

## Adjust counts for '7' and '9' characters
count = [(j - 5 if keyboard[i] == "7" or keyboard[i] == "9" else j - 4) if j > 4 else j for i, j in enumerate(count)]
## Initialize an empty string for the final message
message = "" 
## Define a dictionary mapping keyboard keys to characters
dict = {
    "2": ("a", "b", "c", "2"),  
    "3": ("d", "e", "f", "3"),
    "4": ("g", "h", "i", "4"),
    "5": ("j", "k", "l", "5"),
    "6": ("m", "n", "o", "6"),
    "7": ("p", "q", "r", "s", "7"),
    "8": ("t", "u", "v", "w", "8"),
    "9": ("w", "x", "y", "z", "9"),
    "0": (" ", "0")
}

## Build the message by mapping characters based on the keyboard key and count
for key in zip(keyboard, count):
    message += dict[key[0]][key[1] - 1]  

print(message.title()) 
