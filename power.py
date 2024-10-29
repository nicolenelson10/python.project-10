'''
author name:nicole
date:22-10-2024
'''
string_input=input("enter a string")
vowels="aeiouAEIOU"
vowels_count=0
consonants_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
print(f"no of vowels in the given string{string_input}={vowels_count}")
print(f"no of consonants in the given string{string_input}={consonants_count}")
