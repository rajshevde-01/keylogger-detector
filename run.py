# run.py
from detector.monitor import start_monitoring
from detector.keyboard_hook_check import check_keyboard_hooks
import time

def run_keylogger_detector():
    print("🔐 Starting Keylogger Detection Tool")
    print("\n🔎 Checking for active keyboard hooks...")
    print(check_keyboard_hooks())
    print("\n🚀 Starting process scan...\n")
    start_monitoring()

if __name__ == "__main__":
    run_keylogger_detector()
