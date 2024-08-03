n,k = map(int,input().split())


def josephus(n,k):
    
    arr = list(range(1,n+1))
    result = []
    index = 0
    
    while arr:    
        index = (index + k - 1) % len(arr)
        result.append(arr.pop(index))        
    
    return tuple(result)


print("<" + ", ".join(map(str, josephus(n, k))) + ">")
