from platform import platform, system, release, version, machine, processor, node
from socket import gethostname, gethostbyname
from re import findall
from uuid import getnode
from psutil import cpu_percent, virtual_memory, swap_memory, disk_usage, sensors_battery, boot_time
from psutil import users as usrs
from os import popen
from datetime import datetime, timedelta
from time import time

def date(): return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def cpu(): return cpu_percent()
def uptime(): return timedelta(seconds=round(time() - boot_time()))
def architecture(): return machine()

def ram(): return virtual_memory().used / (1024.0 **2), virtual_memory().total / (1024.0 **2)
def swap(): return swap_memory().used / (1024.0 **2), swap_memory().total / (1024.0 **2)
def disk(): return disk_usage('/').used / (1024.0 **3), disk_usage('/').total / (1024.0 **3)

def host(): return gethostname() #node()
def ip(): return gethostbyname(gethostname())
def mac(): return ':'.join(findall('..', '%012x' % getnode()))

def battery(): return sensors_battery().percent
def users(): return len(usrs())

def percent(self):
    if self[1] != 0:
        return self[0]*100/self[1]
    return 0
    
def all():
    return '''
date: {0}
uptime: {1}

cpu: {2}%
ram: {3[0]:.0f}mb/{3[1]:.0f}mb {4:.1f}%
swap: {5[0]:.0f}mb/{5[1]:.0f}mb {6:.1f}%
disk: {7[0]:.0f}gb/{7[1]:.0f}gb {8:.1f}%

ip-address: {9}
users: {10}
'''.format(date(), uptime(), cpu(), ram(), percent(ram()), swap(), percent(swap()), disk(), percent(disk()), ip(), users())

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='description')
    parser.add_argument('-a', '--all', action='store_true', help='description')
    parser.add_argument('-f', '--flag', action='store_true', help='description')
    args = parser.parse_args()

    print(all())