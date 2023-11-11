#rows = int(input("enter the number of rows my lord: "))
#columns = int(input("enter the number of columns my lord: "))
symbol = input("enter the symbol you want my lord: ")
def Special_Char(symbol):
  for i in symbol:
    if i != "@" or i!= "!" or i !="&" :
      continue 
    else: 
      return symbol[i]
print(Special_Char(symbol))  
  
  
#for k in range(rows):
  #for j in range(columns):
  #  print(Special_Char(symbol), end="")
 # print()  