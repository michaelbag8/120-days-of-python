import re
text = "hello#"

word = text.replace("#", "").upper()

print(word)

text = "hello#world"

before, after = text.split("#", 1)

result = before.upper() + after

print(result)

word = "welcome back home Mr smith (cap) your house is cleaned"

parts = word.split()

for i in range(len(parts)):
    if parts[i] == "(cap)":
        parts[i - 1] = parts[i - 1].capitalize()
        parts.pop(i)
        break

word = " ".join(parts)

print(word)

word = "welcome back home Mr smith (cap, 3) your house is cleaned"

words = word.split()

for i in range(len(words)):
    if words[i].startswith("(cap,"):
        marker = words[i]

        # Get the number
        n = int(marker[5:-1])

        # Capitalize the previous n words
        for j in range(i - n, i):
            words[j] = words[j].capitalize()

        # Remove the marker
        words.pop(i)
        break

word = " ".join(words)

print(word)

word = "welcome back home Mr smith (cap, 3) your house is cleaned"

match = re.search(r"\(cap,\s*(\d+)\)", word)

if match:
    n = int(match.group(1))

    words = word.split()

    marker_index = words.index(match.group(0))

    start = marker_index - n

    for i in range(start, marker_index):
        words[i] = words[i].capitalize()

    words.pop(marker_index)

    word = " ".join(words)

print(word)
