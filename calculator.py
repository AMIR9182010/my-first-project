print("=" * 30)
print("   Simple Calculator")
print("=" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operator (+ or -): ")

if operation == "+":
    result = num1 + num2
    print("Result: " + str(result))
elif operation == "-":
    result = num1 - num2
    print("Result: " + str(result))
else:
    print("Invalid operator!")
  اضافه کردن ماشین حساب ساده با چهار عمل
