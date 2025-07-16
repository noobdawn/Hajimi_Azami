import os
import shutil
from PIL import Image

ATLAS_DIR = "Atlas"
GIF_DIR = "GIF"
SPLIT_DIR = "Split"

BACKGROUND_COLOR = (0, 0, 0, 0)
INTERNAL = 100 # milliseconds
SCALE = 4

# clear directory
def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

clear_directory(GIF_DIR)
clear_directory(SPLIT_DIR)


# 判断是否为空图片，即Alpha通道全为0
def is_empty_image(image):
    if image.mode != 'RGBA':
        return False
    alpha = image.split()[-1]
    return not alpha.getbbox()

# 遍历图片所有像素，若像素alpha=0，则填充为白色
def fill_empty_image(image):
    if image.mode != 'RGBA':
        return image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            if a == 0 and BACKGROUND_COLOR[3] != 0:
                image.putpixel((x, y), BACKGROUND_COLOR)
    return image
    

def split(atlas_path, file_prefix, scale=1):
    atlas = Image.open(atlas_path)
    atlas = atlas.transpose(Image.FLIP_TOP_BOTTOM)
    width, height = atlas.size
    parent_dir = os.path.dirname(atlas_path)
    parent_dir = os.path.basename(parent_dir)  # 获取Atlas目录下的子目录名
    tile_size = parent_dir.split('x')
    tile_width = int(tile_size[0]) if len(tile_size) > 0 else 128
    tile_height = int(tile_size[1]) if len(tile_size) > 1 else 128
    rows = height // tile_height
    cols = width // tile_width

    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height
            
            tile = atlas.crop((left, upper, right, lower))
            index_str = f"{col + row * cols:02d}"
            tile_name = f"{file_prefix}_{index_str}.png"
            tile_path = os.path.join(SPLIT_DIR, tile_name)
            if is_empty_image(tile):
                continue
            tile = fill_empty_image(tile)
            if scale != 1:
                # 用nearest neighbor缩放
                tile = tile.resize((tile_width * scale, tile_height * scale), Image.NEAREST)
            tile.save(tile_path)

# 使用PIL库的imageio保存为GIF
def create_gif_from_split(file_prefix):
    split_images = []
    for f in os.listdir(SPLIT_DIR):
        if f.startswith(file_prefix) and f.endswith('.png'):
            split_images.append(os.path.join(SPLIT_DIR, f))
    
    if not split_images:
        return
    
    split_images.sort()  # 确保顺序正确
    images = [Image.open(img) for img in split_images]
    gif_path = os.path.join(GIF_DIR, f"{file_prefix}.gif")
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=INTERNAL, transparency=0, loop=0, disposal=2)

pngs = []
# 遍历Atlas目录下的所有png文件
for root, dirs, files in os.walk(ATLAS_DIR):
    for file in files:
        if file.endswith('.png'):
            full_path = os.path.join(root, file)
            pngs.append(os.path.relpath(full_path, ATLAS_DIR))
for png in pngs:
    atlas_path = os.path.join(ATLAS_DIR, png)
    gif_name = os.path.splitext(png)[-2]
    gif_name = gif_name.split(os.sep)[-1]  # 获取文件名
    
    split(atlas_path, gif_name, SCALE)
    create_gif_from_split(gif_name)
shutil.rmtree(SPLIT_DIR)  # 清空分割目录以便下次使用