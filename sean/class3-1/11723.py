import sys

# sys.stdin = open("input.txt", "r")

bit_set = 0
for _ in range(int(sys.stdin.readline())):
    command, *arg = sys.stdin.readline().split()
    if arg:
        arg = int(arg[0]) - 1
        if command == "add":
            bit_set |= 1 << arg
        elif command == "remove":
            bit_set &= ~(1 << arg)
        elif command == "check":
            sys.stdout.write(f"{1 if (bit_set & (1 << arg)) else 0}\n")
        elif command == "toggle":
            bit_set ^= 1 << arg
    else:
        if command == "all":
            bit_set = (1 << 21) - 1
        elif command == "empty":
            bit_set = 0
