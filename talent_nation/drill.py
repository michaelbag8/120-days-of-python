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
