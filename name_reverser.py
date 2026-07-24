# -*- coding: utf-8 -*-
print("=" * 40)
print("   🔄 Name Reverser")
print("=" * 40)

name = input("👤 Enter your name: ")

reversed_name = ""

for letter in name:
    reversed_name = letter + reversed_name

print("🔁 Reversed name: " + reversed_name)
