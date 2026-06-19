# -*- coding: utf-8 -*-
"""
Project: Age Calculator & Special Message
Name: AmirMohammad
Age: 14 years old
School: Erfan 1
Goal: Artificial Intelligence in Switzerland
Date: June 20, 2026
"""

print("=" * 40)
print("     🎂 Age Calculator & Special Message")
print("=" * 40)

# My information (pre-filled)
first_name = "AmirMohammad"
last_name = "Nouri"
city = "Bojnord"
birth_year = 2012  # Gregorian

# Calculate age
current_year = 2026
age = current_year - birth_year

# Display information
print("\n" + "=" * 40)
print("     📋 My Information")
print("=" * 40)

print("👤 First Name: " + first_name)
print("👤 Last Name: " + last_name)
print("📍 City: " + city)
print("📅 Birth Year: " + str(birth_year))
print("🎂 My Age: " + str(age) + " years old")
print("🏫 School: Erfan 1")
print("🎯 Goal: Artificial Intelligence in Switzerland with scholarship")

# Special message based on age
print("\n" + "=" * 40)
print("     💬 Special Message for Me")
print("=" * 40)

if age < 18:
    print("👦 " + first_name + "! You are " + str(age) + " years old.")
    print("📚 You still have time to achieve great goals!")
    print("🎯 Focus on studying, programming, and learning German.")
    print("🇨🇭 Switzerland is waiting for you!")
else:
    print("🧑 " + first_name + "! You are " + str(age) + " years old.")
    print("🚀 Now it's time to seriously pursue your goals!")

print("\n" + "=" * 40)
print("😎 This code was written by AmirMohammad.")
print("📅 June 20, 2026")
print("🚀 Towards Artificial Intelligence and Switzerland!")
print("=" * 40)
