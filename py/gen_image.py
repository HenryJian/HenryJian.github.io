from PIL import Image, ImageDraw, ImageFont

def create_image(filename, text, wh, color):
    image = Image.new('RGB', (wh, wh), color=color)
    try_font = ImageFont.truetype('Roboto-Regular.ttf', size=100)

    text_size_x, text_size_y = try_font.getsize(text)
    text_size_max = max(text_size_x, text_size_y)
    size_to_use = (70 * wh / text_size_max)

    font = ImageFont.truetype('Roboto-Regular.ttf', size=size_to_use)
    text_size_x, text_size_y = font.getsize(text)

    start_x, start_y = (wh-text_size_x) // 2, int((wh-text_size_y) // 2 * 0.8)


    draw = ImageDraw.Draw(image)
    draw.text((start_x, start_y), text, fill='black', font=font)
    image.save(filename)


def create_images():
    dp2px = {
        'mdpi' : 1,
        'hdpi': 1.5,
        'xhdpi': 2,
        'xxhdpi': 3,
        'xxxhdpi': 4,
    }
    app_dp, mask_dp = 48, 83
    app_px, mask_px = {}, {}
    for density, ratio in dp2px.items():
        app_px[density] = int(dp2px[density] * app_dp)
        mask_px[density] = int(dp2px[density] * mask_dp)

        if density == 'xxhdpi':
            mask_px[density] = 250

    for density, wh in app_px.items():
        create_image("icons/%s.png" % density, density[:-3], wh, 'orange')
    
    for density, wh in mask_px.items():
        create_image("icons/maskable-%s.png" % density, density[:-3], wh, 'blue')

    create_image("icons/splash-xxhdpi.png", "splash_xxh", 384, 'green')
    create_image('icons/splash-xxxhdpi.png', 'splash_xxxh', 512, 'green')


if __name__ == "__main__":
    create_images()
