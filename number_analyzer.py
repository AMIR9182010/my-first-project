# Number Analyzer: Sum, Average, and Maximum of 5 numbers
print("=" * 30)
print("   Number Analyzer")
print("=" * 30)

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
num3 = float(input("Number 3: "))
num4 = float(input("Number 4: "))
num5 = float(input("Number 5: "))

total = num1 + num2 + num3 + num4 + num5
average = total / 5
maximum = max(num1, num2, num3, num4, num5)

print("\n" + "=" * 30)
print("   Results")
print("=" * 30)
print("Sum: " + str(total))
print("Average: " + str(average))
print("Maximum: " + str(maximum))
اضافه کردن برنامه تحلیل‌گر ۵ عدد
