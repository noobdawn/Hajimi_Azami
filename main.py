import os
import shutil
from PIL import Image
from utils import save_transparent_gif

GIF_DIR = "GIF"
SPRITE_DIR = "Sprites"

BACKGROUND_COLOR = (0, 0, 0, 0)
INTERNAL = 100 # milliseconds

# clear directory
def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

clear_directory(GIF_DIR)

# 遍历图片所有像素，若像素alpha=0，则填充为白色
def fill_empty_image(image):
    if image.mode != 'RGBA':
        return image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            if a == 0:
                image.putpixel((x, y), BACKGROUND_COLOR)
    return image

# 使用PIL库的imageio保存为GIF
def create_gif_from_tiles(file_prefix, images):
    # 排序
    images.sort(
        key=lambda x: int(os.path.basename(x).split('_')[-1].split('.')[0])
    )

    images = [Image.open(img) for img in images]
    if BACKGROUND_COLOR[3] != 0:
        images = [fill_empty_image(img) for img in images]

    for scale in [1, 2, 3, 4]:
        os.makedirs(os.path.join(GIF_DIR, "x" + str(scale)), exist_ok=True)
        gif_path = os.path.join(GIF_DIR, "x" + str(scale), file_prefix + ".gif")
        scaled_images = [img.resize((img.width * scale, img.height * scale), Image.NEAREST) for img in images]

        save_transparent_gif(scaled_images, INTERNAL, gif_path)

if __name__ == "__main__":
    current_prefix = ""
    current_images = []
    for file in os.listdir(SPRITE_DIR):
        if file.endswith(".png"):
            # 命名格式 %s_%d.png
            file_prefix = file[:-4]
            file_prefix = '_'.join(file_prefix.split('_')[:-1])
            if file_prefix != current_prefix:
                if len(current_images) > 0:
                    create_gif_from_tiles(current_prefix, current_images)
                current_prefix = file_prefix
                current_images = []
            current_images.append(os.path.join(SPRITE_DIR, file))
    if len(current_images) > 0:
        create_gif_from_tiles(current_prefix, current_images)

