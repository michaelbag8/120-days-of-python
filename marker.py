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
