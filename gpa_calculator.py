# -*- coding: utf-8 -*-
print("=" * 30)
print("   📊 Grade Point Average (GPA)")
print("=" * 30)

total = 0
count = int(input("How many courses? "))

for i in range(1, count + 1):
    grade = float(input("Grade for course " + str(i) + ": "))
    total = total + grade

average = total / count

print("\n" + "=" * 30)
print("   📋 Result")
print("=" * 30)
print("Total courses: " + str(count))
print("Total grade: " + str(total))
print("Average GPA: " + str(average))

if average >= 17:
    print("🎉 Excellent!")
elif average >= 14:
    print("👍 Good job!")
elif average >= 10:
    print("📚 Keep going!")
else:
    print("💪 Don't give up! Study harder.")
  اضافه کردن پروژه ماشین حساب معدل
