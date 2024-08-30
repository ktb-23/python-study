man, kill = map(int, input().split())

alive = list(range(1, man+1))
target = 0
killed_list = []

while alive:
    target = (target + kill - 1) % len(alive)
    killed_list.append(alive.pop(target))

print(f"<{', '.join(map(str, killed_list))}>")