while True:
    len1,len2,len3 = sorted(map(int,input().split()))

    if len1 == 0 and len2 == 0 and len3 == 0:
        break
    elif len3**2 == len1**2 + len2**2:
        print("right")
    else:
        print("wrong")