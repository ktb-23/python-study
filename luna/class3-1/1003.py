import sys

input = sys.stdin.read
data = input().splitlines()

nums_target = list(map(int, data[1:]))
memo = {0: (1, 0), 1: (0, 1)}

def fibo_cnt(i):
    if i not in memo:
        prev1 = fibo_cnt(i - 1)
        prev2 = fibo_cnt(i - 2)
        memo[i] = (prev1[0] + prev2[0], prev1[1] + prev2[1])
    return memo[i]

output = "\n".join(f"{fibo_cnt(nums)[0]} {fibo_cnt(nums)[1]}" for nums in nums_target)

sys.stdout.write(output + '\n')