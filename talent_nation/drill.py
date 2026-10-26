def censor(message, word):
    if not word:
        return message
        
    return message.replace(word, "[REDACTED]")
   
   
print(censor("enemy at the gate", "enemy"))

def is_valid_transmission(message):
    separator = "//"
    if message.startswith("BEGIN") and message.endswith("END") and separator in message:
        return True
    return False

print(is_valid_transmission("BEGIN move out END"))

def count_until(text, marker):
    count = 0
    for char in text:
        if char == marker:
            break
        count += 1
    return count

print(count_until("ABCDE", "C"))
print(count_until("ABCDE", "Z"))



def count_active(report):
    count = 0
    for dot in report:
        if dot == ".":
            continue
        count +=1
    return count

print(count_active("...."))



def find_first(text, target):
    if len(target) == 0 or target not in text:
        return -1
    count = 0
    while count < len(text):
        if text[count] == target:
            break
            count+=1
        count += 1
    return count


print(find_first("ABCABC","C"))
print(find_first("ABCABC","Z"))


def dog_tag(name, service_number):
    return name + " | SN-" + str(service_number)


def safe_measure(raw):
    raw_cleaned = raw.strip()
    if raw_cleaned.count(".") <= 1 and raw_cleaned.replace(".", "").isdigit():
        return float(raw_cleaned)
    else:
        return "invalid"



print(safe_measure("3.14"))
print(safe_measure("3.14.15"))
