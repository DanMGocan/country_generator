from PIL import Image
import random
import time

def randColor(amount):
    all_colours = []
    for element in range (0, amount):
        new_colour = []

        while len(new_colour) < 3:
            new_colour.append(random.randrange(0, 255, 1))

        all_colours.append(new_colour)

    return all_colours

def ratio_and_breakpoints(ratio, model):
    width = 600
    height = width * ratio
    
    # Ratio 1/2 and various models #
    if ratio <= 1/2:
        if model is "standing_tricolour":
            width_breakpoints = [0, width * 0.33, width * 0.66, width]
            height_breakpoints = [0, height]

        elif model is "laid_tricolour":
            width_breakpoints = [0, width]
            height_breakpoints = [0, height * 0.33, height * 0.66, height]

        elif model is "top_left_corner":
            width_breakpoints = [0, width*0.5, width]
            height_breakpoints = [0, height * 0.5, height]

        elif model is "thin_top_thin_bottom":
            width_breakpoints = [0, width]
            height_breakpoints = [0, height * 0.05, height * 0.95, height]

        elif model is "thin_edges":
            width_breakpoints = [0, width * 0.05, width * 0.95, width]
            height_breakpoints = [0, height]

        else:
            pass
    else:
        pass





def newImg():
    img = Image.new('RGB', (600, 200))
    flag_colours = randColor(3)

    for width in range(0, 600):
        for height in range (0, 600):
            if width <= 200:
                img.putpixel((width, height), (flag_colours[0][0], flag_colours[0][1], flag_colours[0][2]))
            elif width >= 200 and width <= 400:
                img.putpixel((width, height), (flag_colours[1][0], flag_colours[1][1], flag_colours[1][2]))
            elif width >= 400:
                img.putpixel((width, height), (flag_colours[2][0], flag_colours[2][1], flag_colours[2][2]))

        
    #img.putpixel((30,60), (155,155,55))
    img.save('sqr.png')

    return img

i = 0
while i < 10000:

    wallpaper = newImg()
    wallpaper.show() 
    i = i + 1

