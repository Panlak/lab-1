alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypt = input("Enter a clear message")
key = int(input("Please enter a key (number from 1-25): "))
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet [newPosition]
    else:
        encrypted = encrypted + letter
print("Your clipher is: ", encrypted)

