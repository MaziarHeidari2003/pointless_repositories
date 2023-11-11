while True:
  phone_number = input("enter your number bitch: ")
  if phone_number != "":
    break

for i in phone_number:
  if i =="-":
    continue
  print(i, end="")
print()  