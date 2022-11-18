class Romannum:
    def binary_int(bin1,lnth):
        num_1=0
        for j in range(0,lnth):
            if bin1[j]=='1':
                num_1=num_1+(2**(lnth-j-1))
        return num_1


    binnum=input('Enter binary number:')
    length=len(binnum)
    q=binary_int(binnum,length)
    print(q)
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    s=''
    i=12
    while q!=0:
        if q>=num[i]:
            q=q-num[i]
            s=s+roman[i]
        else:
            i-=1
    print(s)


