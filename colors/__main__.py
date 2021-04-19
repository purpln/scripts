from random import randint
from colors import items
from PIL import Image
from numpy import asarray

def rgb8(value):
    r, g, b = value
    if all([ abs(r-g) < 10, abs(r-b) < 10, abs(g-b) < 10]):
        avg = (r+g+b)/3
        grayscale_step = int(avg/10.625)-1
        code = 232 + grayscale_step

    else:
        r_, g_, b_ = [int(c/51) for c in (r, g, b)]
        code = 16 + 36*r_ + 6*g_ + b_

    return code

def img_8bit(array):
    out = []
    for y in range(int(len(array)/2)):
        if y != 0: out.append('\n')
        y2 = 2 * y
        for x in range(len(array[y])):
            top_col = '{}'.format(array[y2][x])
            bot_col = '{}'.format(array[y2+1][x])
            out.append(''.join(('\x1B[38;5;', top_col, ';48;5;', bot_col, 'm▄')))#▀▄
        out.append('\033[0m')
    return ''.join(out)

def convert(list):
    return tuple(i for i in list)

def convertArray(array):
    out = []
    for y in array:
        yArray = []
        for x in y:
            yArray.append(convert(x))
        out.append(yArray)
    return out

def convertImage(path, pixels):
    original = Image.open(path)
    width, height = original.size
    step = width/pixels
    height = int(height/step)
    width = pixels
    image = original.resize((width, height))
    return convertArray(asarray(image))

def rgb(value):
    r, g, b = value
    byte = int(bin(int(round(r*7/255)) << 5), 2) + int(bin(int(round(g*7/255)) << 2), 2) + int(bin(int(round(b*3/255))), 2)
    return byte

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Display image to terminal')
    parser.add_argument('-img', help='Image file to display', default=None)
    parser.add_argument('-width', default=80, help='Character width of output', type=int)
    args = parser.parse_args()
    
    array = convertImage(args.img, args.width)
    lists = convertArray(array)

    out = []
    for y in lists:
        yArray = []
        for x in y:
            yArray.append(rgb(x))
        out.append(yArray)
    
    print(img_8bit(out))


if __name__ == '__main__':
    main()