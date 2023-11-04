password = input("Enter your password: ")
if 8 > len(password):
      message = "Your password must be at least 8 characters" 
else:
      capital_letter = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
      small_letter = set("abcdefghijklmnopqrstuvwxyz")
      number = set("1234567890")
      password = set(password)
      match password:
            case password.isdisjoint(capital_letter):
                  message ="Your password do not contain uppercase letter"
            case password.isdisjoint(small_letter):
                  message ="Your password do not contain lowercase letter"
            case password.isdisjoint(number):
                  message ="Your password do not contain number"
            case _:
                  message ="Your password is strong"
print(message)
