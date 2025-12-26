# by @tgnicehub
# written by zoulib
# obf будит сам размберешшся йобанарод

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
import re

IP_PATTERN = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')  # простая валидация "цифры.точки"

def draw_mask(canvas, w, h):
    """Пример простого рисунка "маски" на canvas (стилизованный)."""
    canvas.create_oval(10, 10, w-10, h-10, fill="#111", outline="#222", width=3)  # лицо
    # глаза
    canvas.create_oval(w*0.22, h*0.28, w*0.38, h*0.46, fill="#fff", outline="#000")
    canvas.create_oval(w*0.62, h*0.28, w*0.78, h*0.46, fill="#fff", outline="#000")
    # зрачки
    canvas.create_oval(w*0.28, h*0.33, w*0.33, h*0.38, fill="#000")
    canvas.create_oval(w*0.68, h*0.33, w*0.73, h*0.38, fill="#000")
    # рот - зловещая улыбка
    canvas.create_arc(w*0.25, h*0.45, w*0.75, h*0.85, start=200, extent=140, style=tk.CHORD, fill="#220000", outline="#440000", width=2)
    # текст Fsocial (стилизованно)
    canvas.create_text(w/2, h*0.12, text="Fsocial", font=("Arial", 20, "bold"), fill="#ff5555")

def start_fake_process(parent, ip_text):
    """Открывает новое окно и запускает фейковую анимацию/логи."""
    win = tk.Toplevel(parent)
    win.title("Process - Fsocial")
    win.geometry("700x450")
    win.resizable(False, False)

    # Прогресс и текст логов
    progress = ttk.Progressbar(win, orient=tk.HORIZONTAL, length=600, mode='determinate')
    progress.pack(pady=(10,5))

    log_frame = tk.Frame(win)
    log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    text = tk.Text(log_frame, state=tk.DISABLED, bg='black', fg='#33FF33', font=('Consolas', 10))
    text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    scrollbar = tk.Scrollbar(log_frame, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text['yscrollcommand'] = scrollbar.set

    def append_log(line):
        text.configure(state=tk.NORMAL)
        text.insert(tk.END, line + "\n")
        text.see(tk.END)
        text.configure(state=tk.DISABLED)

    # Список фейковых сообщений (вымышленное содержание)
    fake_steps = [
        "Initializing Fsocial core...",
        f"Target input: {ip_text}",
        "Resolving route...",
        "Pinging target...",
        "Handshake emulation started...",
        "Loading fake exploit modules...",
        "Injecting dramatic noise...",
        "Bypassing imaginary firewall (sim)...",
        "Harvesting theatrical data...",
        "Encrypting non-existent payload...",
        "Finalizing show...",
    ]

    def worker():
        total = 100
        progress['maximum'] = total
        cur = 0

        # сначала пару быстрых строк
        append_log(">>> Fsocial v1.0 (simulated)")
        time.sleep(0.6)

        for step in fake_steps:
            # случайная задержка для драматичности
            for _ in range(random.randint(2, 6)):
                # добавляем мелкие "шумовые" строки
                noise = random.choice([
                    "... scanning ports",
                    "... checking response",
                    "... cryptic handshake",
                    "... allocating buffer",
                    "... loading libs",
                ])
                append_log(noise)
                inc = random.randint(1, 3)
                cur = min(total, cur + inc)
                progress['value'] = cur
                time.sleep(0.12 + random.random() * 0.25)

            append_log(f"[STEP] {step}")
            cur = min(total, cur + random.randint(3, 8))
            progress['value'] = cur
            time.sleep(0.4 + random.random() * 0.6)

        # добиваем прогресс
        while cur < total:
            cur += random.randint(1, 5)
            progress['value'] = min(total, cur)
            append_log("... finalizing")
            time.sleep(0.08 + random.random() * 0.1)

        append_log(">>> PROCESS COMPLETE. (This was a fake demo.)")
        messagebox.showinfo("Done", "Фейковый процесс завершён.")

    threading.Thread(target=worker, daemon=True).start()


def on_submit(root, entry):
    ip = entry.get().strip()
    if not IP_PATTERN.match(ip):
        messagebox.showerror("Ошибка", "Введите IP в формате: цифры и точки (пример: 192.168.0.1)")
        return
    # Откроем окно фейкового процесса
    start_fake_process(root, ip)


def main():
    root = tk.Tk()
    root.title("Fsocial - Поделиться (демо)")
    root.geometry("420x380")
    root.resizable(False, False)

    # Canvas с "маской"
    canvas = tk.Canvas(root, width=380, height=220, bg="#222")
    canvas.pack(pady=10)
    draw_mask(canvas, 380, 220)

    # Поле ввода IP
    label = tk.Label(root, text="Введите IP (только цифры и точки):")
    label.pack(pady=(6,0))
    entry = tk.Entry(root, width=30, font=("Consolas", 12))
    entry.pack(pady=6)
    entry.insert(0, "192.168.0.1")  # пример по умолчанию

    # Подсказка / этика
    note = tk.Label(root, text="Это локальная демонстрация. Никакие данные не отправляются.", fg="gray", font=("Arial", 8))
    note.pack()

    btn = tk.Button(root, text="Отправить и запустить", command=lambda: on_submit(root, entry), width=22)
    btn.pack(pady=12)

    # Быстрая помощь: закрыть окно по Esc
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()
