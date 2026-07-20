# -*- coding: utf-8 -*-
import random

print("=" * 40)
print("   🎲 Random Picker")
print("=" * 40)

options = [
    "Python",
    "Switzerland",
    "Wengen",
    "Google",
    "AI",
    "Fitness",
    "Night Snow"
]

print("📋 Available options:")
for i, item in enumerate(options, 1):
    print(f"{i}. {item}")

choice = random.choice(options)

print("\n" + "=" * 40)
print("   🎯 Result:")
print("=" * 40)
print(f"✨ Random choice: {choice}")
print("=" * 40)

print("\n😎 Code by AmirMohammad")
print("📅 July 2026")
