import sys
from PIL import Image, ImageDraw, ImageFont
import itertools


def old_main():
    args = sys.argv
    old_name = args[1]
    sizes = args[3].split('x')

    w, h = int(sizes[0]), int(sizes[1])

    new_name = 'maskable_' + old_name
    content = old_name + '\nmaskalbe'

    img = Image.new('RGB', (w, h), color = 'white')


    d = ImageDraw.Draw(img)
    d.text((0,0), content, fill='black', font=font)
    img.save(new_name)

def gen_image(filename, wh, color, text):
    img = Image.new('RGB', (wh, wh), color = color)
    
    d = ImageDraw.Draw(img)
    middle = wh // 2 - 10
    
    # font = ImageFont.load_default()
    # f2 = ImageFont.truetype(font, size=10)



    d.text((middle,middle), text, fill='black', aligh='center')

    img.save(filename+'.png')

def ret_all_icons():
    maskable = [True, False]
    sizes = ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']

    r = []
    for m in maskable:
        for s in sizes:
            r.append((m, s))
    return r

def main():
    print list(itertools.combinations(ret_all_icons(), 2))

    

if __name__ == '__main__':
    main()