from time import time
from colors import items
from PIL import Image
from numpy import asarray
from argparse import ArgumentParser

def rgb8(value):
    r, g, b = [int(c/51) for c in value]
    return 16 + 36*r + 6*g + b

def rgb(query):
    return min( items, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( items.get(subject), query ) ) )

def img_8bit(array):
    out = []
    for y in range(int(len(array)/2)):
        if y != 0: out.append('\n')
        for x in range(len(array[y])):
            top_col = '{}'.format(array[2*y][x])
            bot_col = '{}'.format(array[2*y+1][x])
            out.append(''.join(('\x1B[38;5;', bot_col, ';48;5;', top_col, 'm▄')))
        out.append('\033[0m')
    return ''.join(out)

def convert(list): return tuple(i for i in list)

def convertArray(array):
    out = []
    for y in array:
        yArray = []
        for x in y:
            yArray.append(rgb(convert(x)))
        out.append(yArray)
    return out

def convertImage(path, pixels):
    original = Image.open(path)
    width, height = original.size
    height = int(height/(width/pixels))
    width = pixels
    image = original.resize((width, height))
    return convertArray(asarray(image))


def main():
    parser = ArgumentParser(description='display image to terminal')
    parser.add_argument('-i', '--img', help='image file to display', default='./picture.jpg')
    parser.add_argument('-w', '--width', help='width of output', default=80, type=int)
    args = parser.parse_args()

    start_time = time()
    
    print(img_8bit(convertImage(args.img, args.width)))

    print('{:.2f} seconds'.format(time() - start_time) )


if __name__ == '__main__':
    main()