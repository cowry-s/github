def fizz_buzz(n):
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

if __name__ == "__main__":
    n = int(input("请输入 N: "))
    fizz_buzz(n)
