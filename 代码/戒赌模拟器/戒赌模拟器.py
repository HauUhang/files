import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random

#----------------------底层逻辑----------------------
# 卡片类型及其概率
card_types = ["⭐⭐⭐(就这？)", "⭐⭐⭐⭐(紫气东来)", "⭐⭐⭐⭐⭐(吃点好的吧)"]
probabilities = [0.9, 0.2, 0.001]

# 初始化抽卡次数和结果列表
draw_count = 0
draw_results = {"⭐⭐⭐(就这？)": 0, "⭐⭐⭐⭐(紫气东来)": 0, "⭐⭐⭐⭐⭐(吃点好的吧)": 0}

# 抽卡函数
def draw_card():
    return random.choices(card_types, probabilities)[0]

# 抽一次
def draw_once():
    global draw_count
    global draw_results
    result = draw_card()
    draw_count += 1
    draw_results[result] += 1
    show_result([result])

# 抽十次
def draw_ten_times():
    global draw_count
    global draw_results
    results = [draw_card() for _ in range(10)]
    draw_count += 10
    for result in results:
        draw_results[result] += 1
    show_result(results)

# 显示抽卡结果的弹出窗口
def show_result(results):
    result_window = tk.Toplevel(root)
    result_window.title("抽卡结果")
    
    result_label = tk.Label(result_window, text="抽到了以下卡片：\n" + "\n".join(results))
    result_label.pack()

# 显示抽卡统计的弹出窗口
def show_statistics():
    statistics_window = tk.Toplevel(root)
    statistics_window.title("抽卡统计")
    
    statistics_label = tk.Label(statistics_window, text="抽卡次数: {}\n".format(draw_count))
    for card_type, count in draw_results.items():
        statistics_label.config(text=statistics_label.cget("text") + "{}: {}\n".format(card_type, count))
    statistics_label.pack()

# 退出应用程序
def quit_app():
    root.quit()
    root.destroy()

#----------------------界面布置----------------------
# 创建主窗口
root = tk.Tk()
root.title("戒赌模拟器")

# 加入背景图片
background_image = Image.open("C:/Users/Lenovo/Desktop/戒赌模拟器/background.jpg")
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# 设置窗口的大小与图片尺寸一致
# 获取背景图片的宽度和高度
window_width = background_image.width
window_height = background_image.height
root.geometry(f"{window_width}x{window_height}")

# 创建一个Frame用于包含按钮
button_frame = tk.Frame(root)
button_frame.pack(expand=True)  # 允许Frame扩展以填充可用空间

# 创建按钮
draw_once_button = tk.Button(button_frame, text="抽一次", command=draw_once)
draw_ten_times_button = tk.Button(button_frame, text="抽十次", command=draw_ten_times)
show_statistics_button = tk.Button(button_frame, text="抽卡统计", command=show_statistics)
exit_button = tk.Button(button_frame, text="退出", command=quit_app)

# 将按钮水平居中
draw_once_button.pack(fill="both", expand=True)
draw_ten_times_button.pack(fill="both", expand=True)
show_statistics_button.pack(fill="both", expand=True)
exit_button.pack(fill="both", expand=True)

# 启动GUI主循环
root.mainloop()
