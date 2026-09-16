name = "Sofia"
surname = "Stotska"

full_name = name + surname
vowels_list = "aeiouy"

vowels_count = 0
consonants_count = 0

for char in full_name:
    if char.isalpha():
        if char.lower() in vowels_list:
            vowels_count += 1
        else:
            consonants_count += 1

print(f"{name} {surname}")
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {vowels_count + consonants_count}")