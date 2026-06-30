print("=" * 30)
print("   🎯 Age & Goal Checker")
print("=" * 30)

name = input("Your name: ")
age = int(input("Your age: "))
goal = input("Your goal: ")

if age < 18:
    status = "teenager"
elif age == 18:
    status = "exactly 18"
else:
    status = "adult"

print("\n" + "=" * 30)
print("   📋 Your Profile")
print("=" * 30)
print("Name: " + name)
print("Age: " + str(age))
print("Status: " + status)
print("Goal: " + goal)

if age < 18:
    print("💪 You have time! Keep going!")
else:
    print("🚀 Go for it! Start now!")
  اضافه کردن برنامه Age & Goal Checker
