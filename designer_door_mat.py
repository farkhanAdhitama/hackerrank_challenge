N, M = map(int, input().split())

# atas
for i in range(1, N, 2):
    if i == N :
        break
    print((".|." * i).center(M,"-"))

# middle
print("WELCOME".center(M,"-"))

# bawah
for i in range(N-2, 0, -2):
    print((".|." * i).center(M,"-"))

