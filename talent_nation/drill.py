def censor(message, word):
    if not word:
        return message
        
    return message.replace(word, "[REDACTED]")
   
   
print(censor("enemy at the gate", "enemy"))

