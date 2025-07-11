# detector/monitor.py
import psutil
import time
from colorama import Fore, Style
from .utils import is_suspicious_name

def detect_keylogger():
    print(Fore.YELLOW + "[*] Scanning for suspicious processes..." + Style.RESET_ALL)
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            if is_suspicious_name(pname):
                print(Fore.RED + f"[!] Possible keylogger: {pname} (PID: {proc.info['pid']})" + Style.RESET_ALL)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def start_monitoring(interval=10):
    while True:
        detect_keylogger()
        time.sleep(interval)
