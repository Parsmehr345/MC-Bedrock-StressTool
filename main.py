import ttkbootstrap as tb
from ttkbootstrap.constants import *
import threading
import socket
import time
import random

class StressTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Bedrock Stress Tester")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.style = tb.Style("darkly")  # تم تاریک خفن

        self.running = False
        self.total_packets_sent = 0
        self.start_time = 0

        self.setup_gui()

    def setup_gui(self):
        padding = 10

        header = tb.Label(self.root, text="🎯 Minecraft Bedrock Stress Tester", 
                          font=("Segoe UI", 20, "bold"), bootstyle="info")
        header.pack(pady=padding)

        frame = tb.Frame(self.root, padding=padding)
        frame.pack(fill=X, padx=20)

        # IP Entry
        tb.Label(frame, text="Server IP:", font=("Segoe UI", 12)).grid(row=0, column=0, sticky=W, pady=5)
        self.ip_entry = tb.Entry(frame, font=("Segoe UI", 12))
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.grid(row=0, column=1, sticky=EW, pady=5, padx=10)

        # Port Entry
        tb.Label(frame, text="Port:", font=("Segoe UI", 12)).grid(row=1, column=0, sticky=W, pady=5)
        self.port_entry = tb.Entry(frame, font=("Segoe UI", 12))
        self.port_entry.insert(0, "19132")
        self.port_entry.grid(row=1, column=1, sticky=EW, pady=5, padx=10)

        # Threads Entry
        tb.Label(frame, text="Threads:", font=("Segoe UI", 12)).grid(row=2, column=0, sticky=W, pady=5)
        self.threads_entry = tb.Entry(frame, font=("Segoe UI", 12))
        self.threads_entry.insert(0, "50")
        self.threads_entry.grid(row=2, column=1, sticky=EW, pady=5, padx=10)

        frame.columnconfigure(1, weight=1)

        # Buttons Frame
        btn_frame = tb.Frame(self.root, padding=padding)
        btn_frame.pack(pady=10)

        self.start_button = tb.Button(btn_frame, text="🔥 Start", bootstyle="success-outline", width=15, command=self.start_test)
        self.start_button.grid(row=0, column=0, padx=15)

        self.stop_button = tb.Button(btn_frame, text="🛑 Stop", bootstyle="danger-outline", width=15, command=self.stop_test, state=DISABLED)
        self.stop_button.grid(row=0, column=1, padx=15)

        # Status Label
        self.status = tb.Label(self.root, text="Status: Idle", font=("Segoe UI", 14), bootstyle="secondary")
        self.status.pack(pady=15)

        # Progress Bar
        self.progress = tb.Progressbar(self.root, mode='indeterminate', length=400, bootstyle="info")
        self.progress.pack(pady=5)

        # Report Label
        self.report = tb.Label(self.root, text="Packets Sent: 0   Time: 0s", font=("Segoe UI", 12), bootstyle="light")
        self.report.pack(pady=10)

        # Footer
        footer = tb.Label(self.root, text="Created by ParsMehr — The Code Alchemist", font=("Segoe UI", 10, "italic"), bootstyle="secondary")
        footer.pack(side="bottom", pady=8)

    def start_test(self):
        if self.running:
            return
        self.running = True
        self.total_packets_sent = 0
        self.start_time = time.time()
        self.status.config(text="Status: Running...", bootstyle="success")
        self.start_button.config(state=DISABLED)
        self.stop_button.config(state=NORMAL)
        self.progress.start(10)

        ip = self.ip_entry.get()
        try:
            port = int(self.port_entry.get())
            threads = int(self.threads_entry.get())
        except ValueError:
            self.status.config(text="Status: Invalid Port or Threads!", bootstyle="danger")
            self.stop_test()
            return

        for _ in range(threads):
            threading.Thread(target=self.send_ping, args=(ip, port), daemon=True).start()

        self.update_report()

    def stop_test(self):
        self.running = False
        self.status.config(text="Status: Stopped", bootstyle="warning")
        self.start_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)
        self.progress.stop()

    def send_ping(self, ip, port):
        while self.running:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    packet = b'\x01' + random.randbytes(24)
                    s.sendto(packet, (ip, port))
                    self.total_packets_sent += 1
            except Exception:
                pass
            time.sleep(0.05)

    def update_report(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.report.config(text=f"Packets Sent: {self.total_packets_sent}   Time: {elapsed}s")
            self.root.after(1000, self.update_report)

if __name__ == "__main__":
    root = tb.Window()
    app = StressTesterApp(root)
    root.mainloop()
