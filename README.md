# 🔐 Keylogger Detector


A real-time keylogger detection tool built with Python for Windows systems. This tool detects suspicious processes and active global keyboard hooks — common indicators of keylogging behavior. It includes both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** built with Tkinter.

---

## 🚀 Features

- 🕵️ Detects suspicious process names (`keylog`, `logger`, `hook`, etc.)
- 🧠 Detects global keyboard hook activity using Windows APIs (`pywin32`)
- 🖥️ GUI version for interactive use (start/stop monitoring, run hook scan)
- 💻 CLI version for terminal-based detection
- 🔁 Scans continuously every 10 seconds (customizable)
- ✅ Lightweight and easy to extend
- 🧪 Unit test support with basic test case

---


🧑‍💻 Installation
1. Clone the Repository

git clone https://github.com/rajshevde-01/keylogger-detector.git
cd keylogger-detector

1. Create and Activate a Virtual Environment

python -m venv venv

# Windows

venv\Scripts\activate

# Linux/macOS (GUI won't work)

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

▶️ Usage
👉 Run the CLI Version

python run.py

✅ Checks for global keyboard hook interference (Windows only)

🔄 Continuously scans for suspicious processes

👉 Run the GUI Version

python gui.py
🟢 Click Start Monitoring to begin live process detection

🛡️ Click Check Keyboard Hook to scan for suspicious keyboard API hooks

🧪 Run Unit Tests

python -m unittest discover tests
⚙️ Requirements
Python 3.8+

Windows OS (for keyboard hook detection)

Dependencies:
psutil
pywin32
colorama
tkinter (comes built-in with Python)

🏁 Convert to .exe (Optional)
Use PyInstaller to convert GUI into a Windows executable:

pip install pyinstaller
pyinstaller --noconsole --onefile gui.py
.exe will be generated inside the dist/ folder

🛡️ License
This project is licensed under the MIT License.

👤 Author
Raj Shevde
📧 rajshevde_01

⭐️ Star This Repo
If you found this tool useful, please ⭐️ star the repository to show your support!

🔮 Future Enhancements
 Show which process installed a keyboard hook
 Real-time system tray alerts
 Network traffic inspection for exfiltration attempts
 Export scan results to .txt or .csv
 Automatically block or kill flagged processes