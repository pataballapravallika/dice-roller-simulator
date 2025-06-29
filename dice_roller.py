import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_animation():
    animation = ["Rolling.", "Rolling..", "Rolling...", "Rolling....", "Rolling....."]
    for frame in animation:
        clear_screen()
        print(frame)
        time.sleep(0.3)

def roll_dice():
    input("🎲 Press Enter to roll the dice...")
    roll_animation()
    result = random.randint(1, 6)
    clear_screen()
    print(f"🎲 You rolled a {result}!")

if __name__ == "__main__":
    while True:
        roll_dice()
        again = input("\nDo you want to roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break
