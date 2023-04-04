N=int(input("Digite o número:"))
P="S"
for v in range(N-1,1,-1):
    if N % v ==0:
        P+='nm'
        break
    if P=='S':
        print(f"{N},é primo")
    else:
        print(f"{N},não é primo")