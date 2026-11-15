
import os
import sys
import time
import math
import random
import shutil

# ==========================================
# PROJECT APOCALYPSE - TURBO EDITION
# ==========================================

os.system("cls" if os.name == "nt" else "clear")
os.system("")

W, H = shutil.get_terminal_size((100, 35))
W = min(W, 110)
H = min(H, 38)

COLORS = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m",
    "\033[97m"
]

RESET = "\033[0m"
BOLD = "\033[1m"

def color():
    return random.choice(COLORS)

def cursor(x, y):
    print(f"\033[{y};{x}H", end="")

def clear():
    print("\033[2J\033[H", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

# ==========================================
# INTRO GLITCH
# ==========================================

def intro():
    title = "PROJECT APOCALYPSE"

    for _ in range(6):
        clear()
        cursor(W//2-10, H//2)
        print(color() + BOLD +
              "".join(random.choice("!@#$%01<>") for _ in title))
        time.sleep(0.025)

    clear()
    cursor(W//2-10, H//2)

    for c in title:
        print(color() + BOLD + c, end="", flush=True)
        time.sleep(0.015)

    time.sleep(0.2)

# ==========================================
# HYPERSPACE
# ==========================================

def hyperspace():
    stars = [
        [random.uniform(-W, W),
         random.uniform(-H, H),
         random.uniform(1, 40)]
        for _ in range(120)
    ]

    for frame in range(100):
        screen = [[" " for _ in range(W)] for _ in range(H)]

        for star in stars:
            star[2] -= 0.9

            if star[2] <= 0:
                star[:] = [
                    random.uniform(-W, W),
                    random.uniform(-H, H),
                    40
                ]

            x = int(W/2 + star[0] / star[2] * 3)
            y = int(H/2 + star[1] / star[2])

            if 0 <= x < W and 0 <= y < H:
                screen[y][x] = random.choice([".", "+", "*", "✦"])

        cursor(1, 1)

        for row in screen:
            print(color() + "".join(row) + RESET)

        time.sleep(0.012)

# ==========================================
# 3D SPHERE
# ==========================================

def sphere():
    angle = 0

    for frame in range(120):
        screen = [[" " for _ in range(W)] for _ in range(H)]

        for lat in range(0, 180, 10):
            for lon in range(0, 360, 7):

                a = math.radians(lat)
                b = math.radians(lon) + angle

                x = math.sin(a) * math.cos(b)
                y = math.sin(a) * math.sin(b)

                scale = 12 / (math.cos(a) + 2.5)

                px = int(W/2 + x * scale * 3)
                py = int(H/2 + y * scale)

                if 0 <= px < W and 0 <= py < H:
                    screen[py][px] = random.choice(
                        ["@", "#", "*", "+", "o"]
                    )

        cursor(1, 1)

        for row in screen:
            print(color() + "".join(row) + RESET)

        angle += 0.16
        time.sleep(0.015)

# ==========================================
# RADAR
# ==========================================

def radar():
    cx, cy = W//2, H//2
    angle = 0

    for frame in range(120):
        screen = [[" " for _ in range(W)] for _ in range(H)]

        for radius in range(4, min(W//3, H//2), 5):
            for degree in range(0, 360, 3):
                a = math.radians(degree)
                x = int(cx + radius * math.cos(a) * 2)
                y = int(cy + radius * math.sin(a))

                if 0 <= x < W and 0 <= y < H:
                    screen[y][x] = "."

        for _ in range(12):
            a = random.uniform(0, math.pi*2)
            r = random.uniform(3, min(W//4, H//2-1))

            x = int(cx + r * math.cos(a) * 2)
            y = int(cy + r * math.sin(a))

            if 0 <= x < W and 0 <= y < H:
                screen[y][x] = "x"

        for r in range(1, min(W//3, H//2)):
            x = int(cx + r * math.cos(angle) * 2)
            y = int(cy + r * math.sin(angle))

            if 0 <= x < W and 0 <= y < H:
                screen[y][x] = "*"

        cursor(1, 1)

        for row in screen:
            print("\033[92m" + "".join(row) + RESET)

        angle += 0.16
        time.sleep(0.012)

# ==========================================
# COUNTDOWN
# ==========================================

def countdown():
    for number in range(5, 0, -1):
        clear()

        cursor(W//2-8, H//2-2)
        print(color() + BOLD + "CRITICAL EVENT" + RESET)

        cursor(W//2, H//2)
        print(color() + BOLD + str(number) + RESET)

        time.sleep(0.25)

# ==========================================
# FINAL TAKEOVER
# ==========================================

def final_screen():
    messages = [
        "REALITY BREACH DETECTED",
        "SYSTEM OVERLOAD",
        "ALL DIMENSIONS UNSTABLE",
        "PROJECT APOCALYPSE COMPLETE"
    ]

    for msg in messages:
        clear()

        for _ in range(3):
            cursor(random.randint(1, max(1, W-len(msg))),
                   random.randint(1, H))
            print(color() + BOLD + msg + RESET)
            time.sleep(0.035)

    clear()

    art = [
        " █████╗ ██████╗  ██████╗ ",
        "██╔══██╗██╔══██╗██╔═══██╗",
        "███████║██████╔╝██║   ██║",
        "██╔══██║██╔═══╝ ██║   ██║",
        "██║  ██║██║     ╚██████╔╝",
        "╚═╝  ╚═╝╚═╝      ╚═════╝ "
    ]

    for i, line in enumerate(art):
        cursor(W//2-15, H//2-4+i)
        print(color() + BOLD + line + RESET)
        time.sleep(0.04)

    # CREATOR CREDITS
    time.sleep(0.2)
    cursor(W//2-12, H//2+5)
    print("\033[96m" + BOLD + "MADE BY ABDUL MOEZ" + RESET)

    cursor(W//2-13, H//2+7)
    print("\033[97m>>> SIMULATION ENDED <<<" + RESET)
    time.sleep(90)

# ==========================================
# RUN
# ==========================================

try:
    hide_cursor()

    intro()
    hyperspace()
    sphere()
    radar()
    countdown()
    final_screen()

except KeyboardInterrupt:
    pass

finally:
    show_cursor()
    print(RESET)

