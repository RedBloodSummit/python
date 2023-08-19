def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "除数不能为零"

print("选择操作：")
print("1. 相加")
print("2. 相减")
print("3. 相乘")
print("4. 相除")

choice = input("输入你的选择（1/2/3/4）: ")

num1 = float(input("输入第一个数: "))
num2 = float(input("输入第二个数: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("输入无效")
