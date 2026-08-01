#mini text analyser 
sentence = input("Enter a sentence: ").strip()

character_count = len(sentence)
uppercase = sentence.upper()
lowercase = sentence.lower()
titlecase = sentence.title()
contains_python = "python" in lowercase
first_character = sentence[0]
last_character = sentence[-1]

print(f"Original Sentence: {sentence}")
print(f"Character Count: {character_count}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Title Case: {titlecase}")
print(f"Contains 'Python': {contains_python}")
print(f"First Character: {first_character}")
print(f"Last Character: {last_character}")
