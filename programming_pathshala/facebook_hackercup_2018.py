def interception():
    N = int(input())
    for _ in range(N+1):
        _ = int(input())
    return "1\n0.0" if N % 2 == 1 else "0"

for case in range(int(input())):
    print('Case ' + "#"  ,(case+1, interception()))

