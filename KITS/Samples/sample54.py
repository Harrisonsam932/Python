'''
import os
import sys
import ctypes
import winreg


def is_running_as_admin():
    '''
import admin
Checks if the script is running with administrative privileges.
Returns True if is running as admin, False otherwise.
'''
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def execute():
    if not is_running_as_admin():
        print('[!] The script is NOT running with administrative privileges')
    else:
        print('[+] The script is running with administrative privileges!')


if __name__ == '__main__':
    execute()

'''

path = "C:\\users\harrison\desktop\python\KITS\samples"


def readFile(path):
    if os.path.exists(path):
        file1 = open(path, 'r')
        for item in file1.readlines():
            print(item)
        file1.close()
        print(file1)


readFile(path)
