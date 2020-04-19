k=int(input())
lines = []
for a in range(k):
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    if(l!=lines[-1]):
       print(l)
    else:
       print(l,end="")