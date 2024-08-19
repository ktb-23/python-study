import sys

s = 0
input = sys.stdin

for line in input:
    command = line.split()

    if command[0] == 'add':
        s |= (1 << (int(command[1]) - 1))
    elif command[0] == 'remove':
        s &= ~(1 << (int(command[1]) - 1))
    elif command[0] == 'check':
        if s & (1 << (int(command[1]) - 1)):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command[0] == 'toggle':
        s ^= (1 << (int(command[1]) - 1))
    elif command[0] == 'all':
        s = (1 << 20) - 1
    elif command[0] == 'empty':
        s = 0

