#错误检测
try:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the first number:"))
    print(num1/num2)
except Exception as arr:
        print('Something wrong')
        print(err)
