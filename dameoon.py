import time
import random
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController
from pynput import mouse, keyboard
from colorama import init, Fore, Style

init(autoreset=True)

INACTIVITE_MAX = 60
KEYBOARD = True
MOUSE = True

dernier_mouvement = time.time()
kb = KeyboardController()
ms = MouseController()

def random_count(t):
    return random.randint(1, t)

def reset_timer(_):
    global dernier_mouvement
    dernier_mouvement = time.time()

keyboard.Listener(on_press=reset_timer).start()
mouse.Listener(on_move=reset_timer, on_click=reset_timer, on_scroll=reset_timer).start()

def print_status(message, level="info"):
    now = time.strftime("%H:%M:%S")
    if level == "info":
        print(f"{Fore.CYAN}[{now}] {message}{Style.RESET_ALL}")
    elif level == "warning":
        print(f"{Fore.YELLOW}[{now}] {message}{Style.RESET_ALL}")
    elif level == "error":
        print(f"{Fore.RED}[{now}] {message}{Style.RESET_ALL}")

def print_ascii():
    art = r"""
      ____    _    __  __ _____    ___   ___  _   _ 
     |  _ \  / \  |  \/  | ____|  / _ \ / _ \| \ | |
     | | | |/ _ \ | |\/| |  _|   | | | | | | |  \| |
     | |_| / ___ \| |  | | |___  | |_| | |_| | |\  |
     |____/_/   \_\_|  |_|_____|  \___/ \___/|_| \_|
                                                   
        Anti-AFK Roblox Script - By NycolazSec
"""
    print(Fore.GREEN + art + Style.RESET_ALL)

print_ascii()
print_status("Anti-AFK Roblox lancé... (Ctrl+C pour quitter)", "info")

try:
    while True:
        temps_inactif = time.time() - dernier_mouvement

        if temps_inactif > INACTIVITE_MAX:
            print_status(f"Inactif depuis {int(temps_inactif)} secondes. Simulation d'activité...", "warning")

            if KEYBOARD:
                for _ in range(random_count(3)):
                    kb.press(Key.space)
                    kb.release(Key.space)
                    time.sleep(random.uniform(0.1, 0.3))

                for _ in range(random_count(3)):
                    kb.press('z')
                    time.sleep(random.uniform(0.3, 0.6))
                    kb.release('z')
                    time.sleep(random.uniform(0.1, 0.3))
                    kb.press('s')
                    time.sleep(random.uniform(0.3, 0.6))
                    kb.release('s')
                    time.sleep(random.uniform(0.1, 0.3))

            if MOUSE:
                dx = random.randint(-5, 5)
                dy = random.randint(-5, 5)
                ms.move(dx, dy)
                time.sleep(random.uniform(0.1, 0.3))
                ms.move(-dx, -dy)

            dernier_mouvement = time.time()
            print_status("Activité simulée.", "info")

        time.sleep(random.uniform(5, 10))

except KeyboardInterrupt:
    print_status("Anti-AFK arrêté. À bientôt !", "error")
