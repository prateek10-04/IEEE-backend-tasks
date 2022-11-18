test=int(input('Enter the number of test cases '))

for i in range(0,test):
    n=int(input('Enter the number of letters in the string '))
    s=input('Enter the string ')
    a=int(n/2)
    if s[0:a]==s[a:n]:
        print('Yes')
    else:
        print('No')
