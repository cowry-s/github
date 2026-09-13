def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("输入无效，请输入一个数字。")

def main():
    print("=== 简易计算器 ===")
    print("支持操作: +, -, *, /")
    
    while True:
        try:
            num1 = get_number("请输入第一个数字: ")
            op = input("请输入运算符 (+, -, *, /): ").strip()
            num2 = get_number("请输入第二个数字: ")
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("不支持的运算符！")
                continue
                
            print(f"结果: {num1} {op} {num2} = {result}")
            
        except ValueError as e:
            print(f"错误: {e}")
            
        choice = input("是否继续计算？(y/n): ").lower()
        if choice != 'y':
            print("感谢使用，再见！")
            break

if __name__ == "__main__":
    main()
