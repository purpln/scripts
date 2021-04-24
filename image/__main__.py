from time import time
from colors import items
from PIL import Image
import numpy as np
from numpy import asarray
from argparse import ArgumentParser

start_time = time()

def rgb8algorithm(query):
    r, g, b = [int(c/51) for c in query]
    return 16 + 36*r + 6*g + b

def rgb8palette(query):
    return min( items, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( items.get(subject), query ) ) )

def closest(query):
    colors = np.array(list(items.values()))
    color = np.array(query)
    distances = np.sqrt(np.sum((colors-color)**2, axis=1))
    index_of_smallest = np.where(distances == np.amin(distances))
    return index_of_smallest[0][0]

def img_8bit(array):
    out = []
    for y in range(int(len(array)/2)):
        for x in range(len(array[y])):
            top_col = '{}'.format(closest(array[2*y][x]))
            bot_col = '{}'.format(closest(array[2*y+1][x]))
            out.append(''.join(('\x1B[38;5;', bot_col, ';48;5;', top_col, 'm▄')))
        out.append('\033[0m\n')
    return ''.join(out)

def convert(list): return tuple(i for i in list)

def convertImage(path, pixels):
    original = Image.open(path)
    width, height = original.size
    height = int(height/(width/pixels))
    width = pixels
    image = original.resize((width, height))
    return asarray(image)


def main():
    parser = ArgumentParser(description='display image to terminal')
    parser.add_argument('-i', '--img', help='image file to display', default='./picture.jpg')
    parser.add_argument('-w', '--width', help='width of output', default=80, type=int)
    args = parser.parse_args()
    
    print(img_8bit(convertImage(args.img, args.width)))

    print('{:.2f} seconds'.format(time() - start_time) )


if __name__ == '__main__':
    main()