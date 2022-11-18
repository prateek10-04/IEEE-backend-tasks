dict = {}
i=int(input("Enter the number of elements"))

for j in range(i):
    ke=input('Enter the key :')
    v=input('Enter the value :')
    dict.update({ke:v})

print(sorted(dict.items())) #sorting according to key
print(sorted(dict.items(),key=lambda x:x[1]))
