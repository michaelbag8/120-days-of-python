import os
import shutil
import subprocess
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def ask_for_minutes():
    while True:
        try:
            minutes = int(input("How many minutes do you want to focus? "))
        except ValueError:
            print("Please enter a valid whole number of minutes.")
            continue

        if minutes <= 0:
            print("Please enter a number greater than zero.")
            continue

        return minutes


def play_alarm():
    alarm_path = os.path.join(os.path.dirname(__file__), "alarm.wav")

    if os.name == "nt":
        try:
            os.startfile(alarm_path)
        except AttributeError:
            subprocess.Popen(["powershell", "-c", f"(New-Object Media.SoundPlayer '{alarm_path}').PlaySync()"], shell=True)
        return

    if shutil.which("afplay"):
        subprocess.Popen(["afplay", alarm_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif shutil.which("paplay"):
        subprocess.Popen(["paplay", alarm_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif shutil.which("play"):
        subprocess.Popen(["play", alarm_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def countdown(minutes):
    total_seconds = minutes * 60

    while total_seconds > 0:
        clear_screen()
        mins, secs = divmod(total_seconds, 60)
        print(f"Focus time remaining: {mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1

    clear_screen()
    print("Time's up! Take a break.")
    play_alarm()


def main():
    while True:
        minutes = ask_for_minutes()
        countdown(minutes)

        again = input("Would you like to start another focus session? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Great job. See you next time!")
            break


if __name__ == "__main__":
    main()
