"""
Karis Kim
CIS 2348
1624226
"""
x = input().strip()


left = 0 #left
right = len(x)-1 #right


result = True
while(left<right):
    if(x[left]!=x[right]):
        result = False
        break
    else:
        left+=1
        right-=1
if (result):
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")