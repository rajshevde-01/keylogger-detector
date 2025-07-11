# gui.py
import tkinter as tk
from tkinter import ttk
import threading
import time
import psutil
from detector.utils import is_suspicious_name
from detector.keyboard_hook_check import check_keyboard_hooks

class KeyloggerDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Keylogger Detector")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        self.monitoring = False
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Status: Idle", font=("Arial", 14))
        self.label.pack(pady=10)

        self.log_area = tk.Text(self.root, height=17, width=80, bg="#f5f5f5")
        self.log_area.pack(pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.toggle_button = ttk.Button(btn_frame, text="Start Monitoring", command=self.toggle_monitoring)
        self.toggle_button.grid(row=0, column=0, padx=10)

        self.hook_button = ttk.Button(btn_frame, text="Check Keyboard Hook", command=self.check_hooks)
        self.hook_button.grid(row=0, column=1, padx=10)

    def toggle_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.label.config(text="Status: Stopped")
            self.toggle_button.config(text="Start Monitoring")
        else:
            self.monitoring = True
            self.label.config(text="Status: Scanning...")
            self.toggle_button.config(text="Stop Monitoring")
            threading.Thread(target=self.scan_loop, daemon=True).start()

    def scan_loop(self):
        while self.monitoring:
            suspicious_found = False
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    pname = proc.info['name'].lower()
                    if is_suspicious_name(pname):
                        msg = f"[!] Suspicious process: {pname} (PID: {proc.info['pid']})\n"
                        self.log_area.insert(tk.END, msg)
                        self.log_area.see(tk.END)
                        suspicious_found = True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            if not suspicious_found:
                self.log_area.insert(tk.END, "[✓] No suspicious processes detected.\n")
                self.log_area.see(tk.END)

            time.sleep(10)

    def check_hooks(self):
        self.log_area.insert(tk.END, "\n🔎 Running keyboard hook detection...\n")
        result = check_keyboard_hooks()
        self.log_area.insert(tk.END, result + "\n")
        self.log_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerDetectorGUI(root)
    root.mainloop()
