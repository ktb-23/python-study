import sys
from typing import List

ROW_COUNT = 2
COLUMN_COUNT = 3

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])  
    index = 1
    
    results: List[str] = []
    
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        stickers = [list(map(int, input_data[index:index + n])), list(map(int, input_data[index + n:index + 2 * n]))]
        index += 2 * n
        
        if n == 1:
            results.append(str(max(stickers[0][0], stickers[1][0])))
            continue
        
        dp = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
        
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        
        dp[0][1] = stickers[1][0] + stickers[0][1]
        dp[1][1] = stickers[0][0] + stickers[1][1]
        
        for i in range(2, n):
            curr = i % COLUMN_COUNT
            prev = (i - 1) % COLUMN_COUNT
            prev_prev = (i - 2) % COLUMN_COUNT
            
            dp[0][curr] = max(dp[1][prev], dp[1][prev_prev]) + stickers[0][i]
            dp[1][curr] = max(dp[0][prev], dp[0][prev_prev]) + stickers[1][i]
        
        results.append(str(max(dp[0][(n-1) % COLUMN_COUNT], dp[1][(n-1) % COLUMN_COUNT])))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()