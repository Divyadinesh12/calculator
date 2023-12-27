def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multliplication(a,b):
    return(a*b)
def deviation(a,b):
    return(a/b)
operations_dict={
    "+":add,
     "-":subtract,
     "*":multliplication,
     "/":deviation}
def calculator():
 number1=int(input("enter the first number:"))
 for osymbol in operations_dict:
   print(osymbol) 
 flag=True
 while flag:
  symbol=input("pick one symbol:")
  number2=int(input("enter the second  number:"))
  calculater_function=operations_dict[osymbol]
  output=calculater_function(number1,number2)
  print(f"{number1}{symbol}{number2}={output}")
  should_conditnoue=input((f"prsee y to continue with {output} or press n to start a new number or prss x to exit:")).lower()
  if should_conditnoue=="y":
    number1=output
  elif should_conditnoue=="n":
     flag=False
     calculator()
  else:
     flag=False
     print("thank you")
     
calculator()    




                 
                 


