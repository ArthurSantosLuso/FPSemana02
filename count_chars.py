
phrase = input()
# phrase = ''.join(char for char in phrase if char.isalnum())

count_char = {}

for char in phrase.lower():
    if char.isspace() or not char.isalnum():
        continue
    elif char in count_char:
        count_char[char] += 1
    else:
        count_char[char] = 1

print(count_char)
