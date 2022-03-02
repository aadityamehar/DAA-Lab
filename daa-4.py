
tests = int(input())
for _ in range(tests):
    n = int(input())
    t1 = list(map(int, input().split())) 
    t2 = list(map(int, input().split()))
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    assert len(s1) == len(t1) - 1
    assert len(s2) == len(t1) - 1
    t = []
    t.append(t1)
    t.append(t2)
    f1 = f2 = [0] * len(t1)
    f1[0] = t1[0]
    f2[0] = t2[0]
    for i in range(1, len(t1)):
        if f1[i-1] + t1[i] <= f2[i-1] + s1[i-1] + t2[i]:
            f1[i] = f1[i-1] + t1[i] 
        else:
            f2[i] = f2[i-1] + s1[i-1] + t2[i]
        
        if f2[i-1] + t2[i] <= f1[i-1] + s2[i-1] + t1[i]:
            f2[i] = f2[i-1] + t2[i] 
        else:
            f1[i] = f1[i-1] + s2[i-1] + t1[i]

    print()
    print(min(f1[len(f1)-1], f2[len(f1)-1]))