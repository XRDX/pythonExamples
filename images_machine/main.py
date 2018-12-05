from PIL import Image, ImageDraw, ImageFont

imageFile = "template.jpg"
font_size = 64
font = ImageFont.truetype(r'C:\Windows\Fonts\simkai.ttf', font_size)

def product_image(name):
    template = Image.open(imageFile)
    
    draw = ImageDraw.Draw(template)
    x = template.size[0] - (875+len(name)*font_size/2)
    y = template.size[1] - 775
    draw.text((x, y), name, fill=(75, 75, 75), font=font)

    template.save(name + ".jpg")


f = open('name.txt', 'r')    
for line in f.readlines():
    line = line.strip('\n') #依次读取每行
    product_image(line)
    print(line)
