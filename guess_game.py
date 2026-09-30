import random
import sys

# รองรับการแสดงผลภาษาไทยบน Windows Terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")



def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_input = input("ทายเลข 1-100: ")
        except (KeyboardInterrupt, EOFError):
            print("\nออกจากเกม")
            break

        try:
            guess = int(user_input.strip())
            if not 1 <= guess <= 100:
                print("กรุณากรอกตัวเลขระหว่าง 1 ถึง 100!")
                continue
        except ValueError:
            print("กรุณากรอกตัวเลขจำนวนเต็ม!")
            continue

        attempts += 1

        if guess < secret_number:
            print("น้อยไป!")
        elif guess > secret_number:
            print("มากไป!")
        else:
            print(f"ถูกต้อง! ทายทั้งหมด {attempts} ครั้ง")
            break
        


if __name__ == "__main__":
    play_game()
