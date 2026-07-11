# -*- coding: utf-8 -*-
print("=" * 30)
print("   📊 Table de Multiplication")
print("=" * 30)

num = int(input("Enter a number: "))

print("\nTable de multiplication de " + str(num) + ":")
print("-" * 20)

for i in range(1, 11):
    result = num * i
    print(str(num) + " × " + str(i) + " = " + str(result))
    اضافه کردن برنامه جدول ضرب
