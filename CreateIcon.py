"""
作者真猪奶茶吃货
这是一个生成彩色图片的脚本
"""
from PIL import Image, ImageDraw, ImageFont
import os
import json

# 定义元素类型与对应背景颜色的映射关系
element_type_colors = {
    "metalloids": (87, 195, 194),              # 绿色
    "alkali_metals": (173, 101, 152),       # 紫色
    "transition_metals": (86, 152, 195),       # 蓝色
    "non_metals": (185, 222, 201),              # 浅绿色
    "alkali_earth_metals": (230, 204, 255), # 淡紫色
    "metals": (237, 90, 101),                  # 红色
    "halogens": (255, 153, 0),              # 橙色
    "noble_gases": (248, 223, 114),           # 黄色
    "transactinides": (0, 255, 255),        # 青色
}

# 定义字体文件路径
font_path = "./resources/fonts/ArialUni.ttf"

# 创建图标
def create_element_icon(element, atomic_number, atomic_mass):
    # 创建新的图像对象
    image = Image.new("RGB", (64, 64), "white")
    
    # 创建绘图对象
    draw = ImageDraw.Draw(image)
    # 绘制矩形背景
    background_color = element_type_colors.get(element_type, (255, 255, 255))  # 默认为白色背景
    draw.rectangle([(0, 0), (64, 64)], fill=background_color)
    # 加载字体
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)
    
    # 绘制原子序数
    atomic_number_text = str(atomic_number)
    draw.text((2, 2), atomic_number_text, font=font, fill="black")

    # 绘制元素符号
    symbol_font_size = 32
    symbol_font = ImageFont.truetype(font_path, symbol_font_size)
    symbol_text = element
    symbol_text_bbox = draw.textbbox((0, 0), symbol_text, font=symbol_font)
    symbol_width = symbol_text_bbox[2] - symbol_text_bbox[0]
    symbol_height = symbol_text_bbox[3] - symbol_text_bbox[1]
    symbol_x = (64 - symbol_width) // 2
    symbol_y = (64 - symbol_height) // 2 - 6
    draw.text((symbol_x, symbol_y), symbol_text, font=symbol_font, fill="black")

    # 绘制原子质量
    atomic_mass_text = str(atomic_mass)
    atomic_mass_text_bbox = draw.textbbox((0, 0), atomic_mass_text, font=font)
    atomic_mass_text_width = atomic_mass_text_bbox[2] - atomic_mass_text_bbox[0]
    atomic_mass_text_height = atomic_mass_text_bbox[3] - atomic_mass_text_bbox[1]
    atomic_mass_x = (64 - atomic_mass_text_width) // 2
    atomic_mass_y = 64 - atomic_mass_text_height - 2-4
    draw.text((atomic_mass_x, atomic_mass_y), atomic_mass_text, font=font, fill="black")
    
    return image

# 创建目录
if not os.path.exists("resources/images"):
    os.makedirs("resources/images")

# 元素列表
elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
            "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
            "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
            ]

# 遍历元素列表，并根据info文件夹中的json文件创建图标
for element in elements:
    # 加载json文件
    info_file = f"resources/info/info_{element}.json"
    with open(info_file, "r", encoding='utf-8-sig') as f:
        info_data = json.load(f)

    # 获取元素信息
    name = info_data["name"]
    atomic_number = info_data["atomic_number"]
    atomic_mass = info_data["atomic_mass"]
    element_type = info_data["element_type"]   # 根据数据源获取元素类型

    # 生成图标并保存
    icon = create_element_icon(name, atomic_number, atomic_mass)
    save_path = f"resources/images/element_{element}.png"
    icon.save(save_path)
    print(f"已保存图标：{save_path}")
