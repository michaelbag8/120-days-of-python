text = "hello#"

word = text.replace("#", "").upper()

print(word)

text = "hello#world"

before, after = text.split("#", 1)

result = before.upper() + after

print(result)
