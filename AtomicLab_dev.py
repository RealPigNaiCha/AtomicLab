import tkinter as tk
from PIL import ImageTk, Image

# 元素数据
elements = [
    {"symbol": "H", "name": "氢", "atomic_number": 1, "atomic_mass": 1.00784},
    {"symbol": "", "name": "", "atomic_number": None, "atomic_mass": None},  # 空的占位按钮
    {"symbol": "He", "name": "氦", "atomic_number": 2, "atomic_mass": 4.0026},
    # 填入所有元素的数据...
]

# 创建主窗口
window = tk.Tk()
window.title("元素周期表")
window.geometry("800x600")  # 将窗口大小设置为800x600像素

# 点击元素后显示详细信息的回调函数
def show_element_info(element):
    if element["atomic_number"] is not None:
        info = f"名称：{element['name']}\n" \
               f"符号：{element['symbol']}\n" \
               f"原子序数：{element['atomic_number']}\n" \
               f"原子质量：{element['atomic_mass']}"
    else:
        info = ""
    info_label.config(text=info)

# 创建元素按钮
buttons = []
row, col = 0, 0
for i, element in enumerate(elements):
    if element["atomic_number"] is None:
        # 创建空的占位按钮
        button = tk.Label(window, padx=10, pady=10)
    else:
        # 加载图像
        image_path = f"./element_{element['symbol']}.png"
        image = Image.open(image_path)
        image = image.resize((50, 50))  # 调整图像大小
        button_image = ImageTk.PhotoImage(image)

        # 创建图像按钮
        button = tk.Button(window, image=button_image, padx=10, pady=10)
        button.config(command=lambda e=element: show_element_info(e))
        
        # 防止图像对象被垃圾回收
        button.image = button_image

    buttons.append(button)
    button.grid(row=row, column=col)
    
    col += 1
    if col == 18:  # 每行最多放18个元素
        col = 0
        row += 1

# 创建显示详细信息的标签
info_label = tk.Label(window, text="点击元素可查看详细信息", padx=10, pady=10)
info_label.grid(row=row+1, columnspan=18)

# 运行程序
window.mainloop()
