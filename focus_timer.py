import time 
focus_time = int(input("How many minutes do you want to focus? "))
total_seconds = focus_time * 60
while total_seconds > 0:
    time.sleep(1)
    get_minutes= total_seconds // 60
    get_seconds = total_seconds % 60
    print(f"{get_minutes:02d}:{get_seconds:02d}")
    total_seconds -= 1
print("Time's up! Take a break.")
print("\a")



#Your Focus Timer is now functionally complete: takes input, counts down in MM:SS, alerts + beeps at the end. Nice work building it piece by piece.
#A couple of optional polish ideas if you want to keep going, or we can stop here and move to the next project:
#Clear the screen each tick so the countdown updates in place instead of scrolling (os.system('cls' if os.name == 'nt' else 'clear'))
#Input validation — what if the user types letters instead of a number?
#Loop the whole thing — ask "focus again?" after it ends
