# This program adds numbers until the user enters 0
print("=" * 30)
print("   Add numbers until 0")
print("=" * 30)

total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum:", total)
اضافه کردن برنامه جمع اعداد تا صفر
