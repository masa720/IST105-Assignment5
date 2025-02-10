import sys
import math
import random

# Get command line arguments
number = int(sys.argv[1])
text = sys.argv[2]

# Number Puzzle
if number % 2 == 0:
    number_result = f"- The number {number} is even. Its square root is {math.sqrt(number)}."
else:
    number_result = f"- The number {number} is odd. Its cube is {number ** 3}."

# Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

# Treasure Hunt
secret_number = random.randint(1, 100)
attempts = 0
found = False
guess_log = []

while attempts < 5:
    guess = random.randint(1, 100)
    attempts += 1
    if guess == secret_number:
        found = True
        break
    elif guess > secret_number:
        guess_log.append(f"- Attempt {attempts}: {guess} (Too high!)")
    else:
        guess_log.append(f"- Attempt {attempts}: {guess} (Too low!)")

if found:
    guess_log.append(f"- Attempt {attempts}: {secret_number} (Correct!)")
    treasure_result = "- You found the treasure!"
else:
    treasure_result = "- You did not find the treasure."

# Result
# print(number_result)
# print(f"Binary: {binary_text}")
# print(f"Vowel Count: {vowel_count}")
# print("\nTreasure Hunt:")
# print("\n".join(guess_log))
# print(treasure_result)

result = "\n".join([
    "Number Puzzle:",
    number_result,
    "",
    "Text Puzzle:",
    f"- Binary: {binary_text}",
    f"- Vowel Count: {vowel_count}",
    "",
    "Treasure Hunt:",
    "\n".join(guess_log),
    treasure_result
])

print(result)
