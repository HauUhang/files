import tkinter as tk
from tkinter import ttk
import time

# 创建主窗口
root = tk.Tk()
root.title("任务进度条")

# 创建进度条
progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=20)

# 更新进度条的函数
def update_progress():
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()  # 更新窗口
        time.sleep(0.1)  # 模拟任务进度更新延迟
    progress['value'] = 0  # 任务完成后重置进度条

# 创建更新按钮
update_button = tk.Button(root, text="开始任务", command=update_progress)
update_button.pack()

# 运行主循环
root.mainloop()
