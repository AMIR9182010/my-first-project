# -*- coding: utf-8 -*-
"""
پروژه: معرفی من (امیرمحمد)
هدف: تمرین پایتون و ساخت اولین پروژه برای گیت‌هاب
تاریخ: ۱۷ ژوئن ۲۰۲۶
"""

import time

# ======================
# اطلاعات من
# ======================
my_name = "امیرمحمد"
my_age = 14
my_school = "عرفان ۱"
my_goal = "تحصیل هوش مصنوعی در سوئیس با بورسیه"
my_github = "AMIR9182010"
my_email = "amirnori828@gmail.com"
languages = ["فارسی", "انگلیسی (در حال یادگیری)", "آلمانی (در حال یادگیری)"]
skills = ["پایتون (تازه شروع)", "تمرین تایپ", "کار با گیت‌هاب"]

# ======================
# توابع (Functions)
# ======================

def show_header():
    """نمایش هدر"""
    print("\n" + "=" * 50)
    print("        🚀 به پروژه من خوش آمدید!")
    print("=" * 50)

def show_intro():
    """معرفی اولیه"""
    print(f"\n👋 سلام! من {my_name} هستم.")
    print(f"🎂 {my_age} سال دارم.")
    print(f"🏫 دانش‌آموز مدرسه {my_school}.")
    print(f"🎯 هدف من: {my_goal}")

def show_skills():
    """نمایش مهارت‌ها"""
    print("\n📚 مهارت‌های من:")
    for skill in skills:
        print(f"   ✅ {skill}")

def show_languages():
    """نمایش زبان‌ها"""
    print("\n🗣️ زبان‌هایی که بلدم یا یاد می‌گیرم:")
    for lang in languages:
        print(f"   🌐 {lang}")

def show_contact():
    """نمایش راه‌های ارتباطی"""
    print("\n📫 راه‌های ارتباطی:")
    print(f"   📧 ایمیل: {my_email}")
    print(f"   🐙 گیت‌هاب: github.com/{my_github}")

def show_menu():
    """نمایش منوی اصلی"""
    print("\n" + "-" * 50)
    print("📋 منوی اصلی:")
    print("   1. معرفی من")
    print("   2. مهارت‌های من")
    print("   3. زبان‌های من")
    print("   4. ارتباط با من")
    print("   5. خروج")
    print("-" * 50)

def loading_animation():
    """یک انیمیشن ساده برای جذابیت"""
    print("\n⏳ در حال بارگذاری...", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n✅ انجام شد!")

# ======================
# اجرای اصلی برنامه
# ======================

def main():
    while True:
        show_header()
        show_intro()
        show_menu()

        choice = input("\n🔢 لطفاً یک گزینه را انتخاب کنید (1-5): ")

        if choice == "1":
            show_intro()
            input("\n🔹 برای ادامه، Enter را بزنید...")

        elif choice == "2":
            show_skills()
            input("\n🔹 برای ادامه، Enter را بزنید...")

        elif choice == "3":
            show_languages()
            input("\n🔹 برای ادامه، Enter را بزنید...")

        elif choice == "4":
            show_contact()
            input("\n🔹 برای ادامه، Enter را بزنید...")

        elif choice == "5":
            print("\n👋 خداحافظ! موفق باشی!")
            print("💪 به یاد داشته باش: هر روز یه قدم به سوئیس نزدیک‌تر!")
            break

        else:
            print("\n❌ گزینه نامعتبر! لطفاً عددی بین 1 تا 5 وارد کن.")
            time.sleep(1)

# ======================
# اجرای برنامه
# ======================

if __name__ == "__main__":
    main()
