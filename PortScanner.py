import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime


def scan_port(target, port, result_box):
    """Scan a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # per-socket timeout
            result = s.connect_ex((target, port))
            if result == 0:
                result_box.insert(tk.END, f"[OPEN] Port {port}\n")
    except Exception as e:
        result_box.insert(tk.END, f"[ERROR] Port {port}: {e}\n")


def start_scan(target, start_port, end_port, result_box):
    """Start scanning in background threads."""
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "-" * 50 + "\n")
    result_box.insert(tk.END, f"Scanning Target: {target}\n")
    result_box.insert(tk.END, f"Time Started: {datetime.now()}\n")
    result_box.insert(tk.END, "-" * 50 + "\n")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        messagebox.showerror("Error", "Invalid hostname.")
        return

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port, result_box))
        t.daemon = True
        t.start()


def on_start():
    """Callback for Start button."""
    target = entry_target.get().strip()
    port_range = entry_ports.get().strip()

    if not target or not port_range:
        messagebox.showwarning("Input Error", "Please enter target and port range.")
        return

    try:
        start_port, end_port = map(int, port_range.split("-"))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Invalid port range. Use format: 1-1024")
        return

    start_scan(target, start_port, end_port, text_results)


# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Python Port Scanner")
root.geometry("600x400")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Target (IP/Domain):").grid(row=0, column=0, padx=5)
entry_target = tk.Entry(frame_top, width=30)
entry_target.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Port Range (e.g. 1-1024):").grid(row=1, column=0, padx=5)
entry_ports = tk.Entry(frame_top, width=30)
entry_ports.grid(row=1, column=1, padx=5)

btn_start = tk.Button(frame_top, text="Start Scan", command=on_start, bg="green", fg="white")
btn_start.grid(row=2, column=0, columnspan=2, pady=10)

text_results = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
text_results.pack(pady=10)

root.mainloop()
