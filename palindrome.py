x=input('Enter the word to check ')
print(x)
l=len(x)
print(l)
m=0
p=(l-1)
for n in range(len(x)):
    if x[n]==x[p] :
        m+=1
    p=p-1
#print(m)
if(m==l):
    print('palindrome')
else:
    print('not palindrome')






