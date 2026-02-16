# Keylogger Detector

Detects suspicious processes and global keyboard hooks on Windows. The project ships with both a CLI and a Tkinter GUI for quick checks and continuous monitoring.

## Features

- Process scanning for suspicious names (e.g., `keylog`, `logger`, `hook`).
- Global keyboard hook detection using Windows APIs (`pywin32`).
- CLI mode for fast terminal checks.
- GUI mode with start/stop monitoring and on-demand hook scans.
- Configurable scan interval (default: 10 seconds).
- Lightweight and easy to extend.

## Requirements

- Windows 10/11
- Python 3.8+
- Dependencies: `psutil`, `pywin32`, `colorama` (Tkinter ships with Python)

### Install

1. Clone the repo.

```bash
git clone https://github.com/rajshevde-01/keylogger-detector.git
cd keylogger-detector
```

2. Create and activate a virtual environment.

```bash
python -m venv venv
venv\Scripts\activate
```


3. **Install required dependencies** (this step is *required*):

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI:

```bash
python run.py
```

Run the GUI:

```bash
python gui.py
```

GUI tips:

- Click Start Monitoring to begin process detection.
- Click Check Keyboard Hook to run a hook scan.

## Tests

```bash
python -m unittest discover tests
```

## Build an .exe (optional)

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile gui.py
```

The executable will be generated in `dist/`.

### Project Layout

```text
keylogger-detector/
├── gui.py
├── run.py
├── requirements.txt
├── README.md
├── detector/
│   ├── keyboard_hook_check.py
│   ├── monitor.py
│   ├── utils.py
│   └── __pycache__/
└── tests/
```

## License

MIT

## Author

Raj Shevde

## Roadmap

- Show which process installed a keyboard hook.
- System tray alerts.
- Export scan results to TXT/CSV.
- Optional auto-kill for flagged processes.
