from colorama import init, Fore, Style
import sys
import time
import random


init(autoreset=True)

def type_writer(text, speed=0.001):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(speed)
    print()

def loading_bar(task="Processing", length=10, speed=0.01):
    bar = "█" * length
    sys.stdout.write(f"\r{Fore.CYAN}{task}: {bar}")
    sys.stdout.flush()
    time.sleep(speed)
    print()

def glitch_effect(text, times=1):
    sys.stdout.write(f"\r{Fore.RED}{''.join(random.sample(text, len(text)))}")
    sys.stdout.flush()
    time.sleep(0.05)
    print(f"\r{Fore.GREEN}{text}")

def menu():
    type_writer(f"{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════════════╗")
    type_writer(f"{Fore.LIGHTGREEN_EX}║   AD WATCHER AUTOMATION SYSTEM v1.0       ║")
    type_writer(f"{Fore.LIGHTGREEN_EX}╚═══════════════════════════════════════════╝")
    type_writer(f"{Fore.YELLOW}Select an option:")
    print(f"{Fore.CYAN}[1] Watch One Ad")
    print(f"{Fore.CYAN}[2] Watch 5 Ads")
    print(f"{Fore.CYAN}[3] Exit")
    choice = input(f"{Fore.MAGENTA}>> ")
    return choice