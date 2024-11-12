num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
print('Select operator:')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
choice=int(input("Enter choice(1/2/3/4):"))

if choice==1:
    print(f'Result:{num1+num2}')
elif choice==2:
    print(f'Result:{num1-num2}')
elif choice==3:
    print(f'Result:{num1*num2}')
elif choice==4:
    print(f'Result:{num1/num2}')
else:
    print('Invalid input') 