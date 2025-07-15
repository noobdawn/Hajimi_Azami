import os
import shutil
from PIL import Image
import imageio

ATLAS_DIR = "Atlas"
GIF_DIR = "GIF"
SPLIT_DIR = "Split"

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
            if a == 0:
                image.putpixel((x, y), (0, 0, 0, 255))
    return image
    

def split(atlas_path, file_prefix, scale=1):
    atlas = Image.open(atlas_path)
    width, height = atlas.size
    tile_width = 128
    tile_height = 128
    rows = height // tile_height
    cols = width // tile_width

    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height
            
            tile = atlas.crop((left, upper, right, lower))
            tile_name = f"{file_prefix}_{col + row * cols}.png"
            tile_path = os.path.join(SPLIT_DIR, tile_name)
            if not is_empty_image(tile):
                tile = fill_empty_image(tile)
            if scale != 1:
                # 用nearest neighbor缩放
                tile = tile.resize((tile_width * scale, tile_height * scale), Image.NEAREST)
                # 颠倒
                tile = tile.transpose(Image.FLIP_TOP_BOTTOM)
                tile.save(tile_path)

# 使用imageio将分割的图片转换为GIF
def create_gif_from_split(file_prefix):
    split_images = []
    for f in os.listdir(SPLIT_DIR):
        if f.startswith(file_prefix) and f.endswith('.png'):
            split_images.append(os.path.join(SPLIT_DIR, f))
    
    if not split_images:
        return
    
    split_images.sort()  # 确保顺序正确
    images = [imageio.imread(img) for img in split_images]
    gif_path = os.path.join(GIF_DIR, f"{file_prefix}.gif")
    imageio.mimsave(gif_path, images, duration=0.3, loop=0)

pngs = [f for f in os.listdir(ATLAS_DIR) if f.endswith('.png')]
for png in pngs:
    atlas_path = os.path.join(ATLAS_DIR, png)
    gif_name = os.path.splitext(png)[0]
    
    split(atlas_path, gif_name, 4)
    create_gif_from_split(gif_name)
shutil.rmtree(SPLIT_DIR)  # 清空分割目录以便下次使用