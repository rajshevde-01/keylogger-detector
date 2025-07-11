# detector/keyboard_hook_check.py
import win32api
import win32con
import win32gui
import win32process
import ctypes
from ctypes import wintypes
import psutil

def get_foreground_window_process_name():
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        return psutil.Process(pid).name()
    except:
        return "Unknown"

def check_keyboard_hooks():
    WH_KEYBOARD_LL = 13
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

    # Try setting a dummy keyboard hook to see if another process intercepts
    def low_level_keyboard_proc(nCode, wParam, lParam):
        return user32.CallNextHookEx(None, nCode, wParam, lParam)

    hook_pointer = HOOKPROC(low_level_keyboard_proc)

    hook = user32.SetWindowsHookExA(
        WH_KEYBOARD_LL,
        hook_pointer,
        kernel32.GetModuleHandleW(None),
        0
    )

    if hook == 0:
        return "[!] Another process might be intercepting the keyboard globally (possible keylogger detected!)"
    else:
        user32.UnhookWindowsHookEx(hook)
        return "[✓] No global keyboard hook interference detected."

if __name__ == "__main__":
    print(check_keyboard_hooks())
    print("Focused window process:", get_foreground_window_process_name())
