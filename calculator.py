class calculator:
     def add(self,num1,num2):
        return num1+num2
     def sub(self,num1,num2):
        return num1-num2
     def mul(self,num1,num2):
         return num1-num2
     def div(self,num1,num2):
         try:
             return num1/ num2
         except ZeroDivisionError:
             return "ERROR:DIVISION BY ZERO IS NOT ALLOWED"
c1=calculator()
print("calc")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice=int(input("enter your choice:"))
if choice==1:
    print("result:",c1.add(num1,num2))
elif choice==2:
    print("result:",c1.sub(num1,num2))
elif choice==3:
    print("result:",c1.mul(num1,num2))
elif choice==4:
    print("result:",c1.div(num1,num2))
else:
    print("Invalid choice")
