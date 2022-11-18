s=""
for i in range(0,7):
    for j in range(0,7):
        if (i==0 or i==6) or (j==6-i) :
            s=s+"*"
        else:
            s=s+" "
    s=s+"\n"
print(s)

q=""
for i in range(0,6):
    for j in range(65,76):
        if 71-i<=j<=69+i:
            q=q+" "
        elif 65<=j<=70-i:
            q=q+chr(j)
        elif 70+i<=j<=75:
            q=q+chr(65+75-j)
    if 0<=i<=4:
        q=q+"\n"
print(q)
z=''
for x in range(0,5):
    for y in range(65,76):
        if 70-(3-x)<=y<=70+(3-x):
            z=z+' '
        elif 65<=y<=66+x:
            z=z+chr(y)
        elif 74-x<=y<=75:
            z=z+chr(140-y)
    z=z+'\n'
print(z)















