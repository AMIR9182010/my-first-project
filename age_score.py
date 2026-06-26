# -*- coding: utf-8 -*-
"""
پروژه: تشخیص سن و نمره
نویسنده: امیرمحمد
تاریخ: ۱۴۰۵/۰۴/۰۶
"""

print("=" * 30)
print("   برنامه تشخیص سن و نمره")
print("=" * 30)

# بخش اول: تشخیص سن
name = input("Your name: ")
age = int(input("Your age: "))

if age > 18:
    print(name + ", you are an adult.")
elif age == 18:
    print(name + ", you are exactly 18!")
else:
    print(name + ", you are a teenager.")

print("\n" + "-" * 30)

# بخش دوم: تشخیص نمره
score = int(input("Your score: "))

if score >= 50:
    print("✅ Passed! Well done!")
else:
    print("❌ Failed. Don't give up! Try again.")

print("\n" + "=" * 30)
print("😎 Code by AmirMohammad")
print("📅 ۱۴۰۵/۰۴/۰۶")
print("=" * 30)
