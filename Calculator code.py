"""Basic Calculator Code"""
a=int(input("What's the first number you'd like to work on :"))
b=int(input("What's the second number : "))
op=input("Operation (+,-,*,/)   : ")
if op== '+':
 print(a+b)
elif op=="-":
 print(a-b)
elif op== "*":
 print(a*b)
elif op== "/":
 print(a/b)
else:
 print("INALID OPERATOR")
