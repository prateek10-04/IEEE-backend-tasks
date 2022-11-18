s=input('Enter the list of integers (separated by a space) ')
l=[[]]
class subset:
    def convert(s):
        list_num = s.split()
        num=len(list_num)

        for i in range(0,num+1):
            for j in range(0,i):

                l.append(list_num[j:i])
        return l

print(subset.convert(s))