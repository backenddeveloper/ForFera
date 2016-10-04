import sys
from src.Application import Application

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
#            Application(sys.argv[0] , '/var/tmp/wordlist.txt')
            Application(sys.argv[1] , 'wordlist.txt')
        except UnboundLocalError:
            print('One or more of the files can not be read.')
    else:
        print('Please input a filename')
