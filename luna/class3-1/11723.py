import sys

def set_commands():
    set_S = set()
    
    for line in sys.stdin:
        command = line.strip()
        if command.startswith("add"):
            _, value = command.split()
            set_S.add(int(value))
        elif command.startswith("remove"):
            _, value = command.split()
            set_S.discard(int(value))
        elif command.startswith("check"):
            _, value = command.split()
            sys.stdout.write(f"{1 if int(value) in set_S else 0}\n")
        elif command.startswith("toggle"):
            _, value = command.split()
            value = int(value)
            if value in set_S:
                set_S.remove(value)
            else:
                set_S.add(value)
        elif command == "all":
            set_S = set(range(1, 21))
        elif command == "empty":
            set_S.clear()
    
set_commands()