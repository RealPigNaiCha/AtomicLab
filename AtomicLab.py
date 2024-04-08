"""
作者真猪奶茶吃货
文件作用：程序主体文件
"""
import tkinter as tk
from PIL import Image, ImageTk
import json
import os

# 元素数据文件夹路径
info_folder = "./resources/info"


# 获取元素数据列表，并按照原子序数排序
def get_element_data():
    elements = []
    files = os.listdir(info_folder)
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(info_folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                element_data = json.load(f)  # 使用json模块加载文件内容
                elements.append(element_data)

    # 按照原子序数对元素列表进行排序
    elements.sort(key=lambda x: x["atomic_number"])

    return elements

# 点击元素按钮后显示详细信息的回调函数
def show_element_info(element):
    popup = PopupWindow(window, element)
    window.wait_window(popup)  # 等待弹出式窗口关闭

# 创建主窗口
window = tk.Tk()
window.title("元素周期表")

# 弹出式窗口类
class PopupWindow(tk.Toplevel):
    def __init__(self, parent, element):
        super().__init__(parent)
        self.title("详细信息")
        self.geometry("300x200")  # 设置弹出式窗口大小为300x200
        
        # 获取元素信息
        name = element["name"]
        symbol = element["symbol"]
        atomic_number = element["atomic_number"]
        atomic_mass = element["atomic_mass"]
        
        # 创建并显示元素信息的标签
        name_label = tk.Label(self, text="名称: " + name)
        name_label.pack()

        symbol_label = tk.Label(self, text="符号: " + symbol)
        symbol_label.pack()

        atomic_number_label = tk.Label(self, text="原子序数: " + str(atomic_number))
        atomic_number_label.pack()

        atomic_mass_label = tk.Label(self, text="原子量: " + str(atomic_mass))
        atomic_mass_label.pack()


# 获取元素数据列表
elements = get_element_data()

# 根据给定的周期数组创建元素按钮
buttons = []
row, col = 0, 0
periods = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,4,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10],
    [11,12,0,0,0,0,0,0,0,0,0,0,13,14,15,16,17,18],
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],
    [37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
    ]  # 给定的周期数组
for period_elements in periods:
    for atomic_number in period_elements:
        if atomic_number == 0:
            col += 1
        else:
            element = elements[atomic_number - 1]  # 元素的索引是原子序数-1
            
            # 加载图像
            symbol = element["symbol"].lower()
            image_path = f"./resources/images/element_{symbol}.png"
            image = Image.open(image_path)
            image = image.resize((64, 64))  # 调整图像大小
            button_image = ImageTk.PhotoImage(image)

            # 创建图像按钮
            button = tk.Button(window, image=button_image, padx=10, pady=10, width=64, height=64)
            button.config(command=lambda e=element: show_element_info(e))
            
            # 防止图像对象被垃圾回收
            button.image = button_image

            buttons.append(button)
            button.grid(row=row, column=col)
            
            col += 1
            if col == 18:  # 每行最多放18个元素
                col = 0
                row += 1

    row += 1

# 根据周期对按钮进行排版，并将周期标题放在每个周期的最右端
for i in range(len(periods)):
    period = i + 1
    # 创建空白标签部件作为周期的标题，并设置背景色和文字颜色
    label = tk.Label(window, text=str(period), font=("Arial", 12, "bold"), bg="white", fg="black")
    label.grid(row=i*2, column=18, rowspan=2, sticky="nsew")

window.mainloop()
