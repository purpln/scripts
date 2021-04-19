#from colors import bcolors

def cpu():
    return ''

def uptime():
    return ''

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Display image to terminal')
    parser.add_argument('-flag', dest='flag_exists', action='store_true')
    args = parser.parse_args()
    if args.flag_exists:
        print('true')
    print(cpu())
    print(uptime())