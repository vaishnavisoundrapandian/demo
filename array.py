#create an array of integers by using module.
#search whether a particulate element is present in the array or not
#without using inbuilt functions.

import array as arr
'''a=arr.array('i',[1,2,3,4,5,6,7,8,9])
chk=False
ele=int(input("Element to find: "))
for x in range(len(a)):
    if a[x]==ele:
        chk=True
if chk==True:
    print("Element found")
else:
    print("Not found")'''

#insert and delete element in an array wihout using any inbuilt functions
a=arr.array('i',[0]*10)
n=int(input("Enter no of elements"))
if n>10:
    print("Size should be less than 10")
else:
    c=0
    for i in range(n):
        ele=int(input("Enter element"))
        a[c]=ele
        c+=1
    print(a)
    ele1=int(input("Enter element to be inserted"))
    pos=int(input("Enter position"))
    for j in range(9,pos-1,-1):
        a[j]=a[j-1]
    a[pos-1]=ele1
    print(a)
    ele2=int(input("enter element to be deleted"))
    pos2=0
    for k in range(len(a)):
        if a[k]==ele2:
            pos2+=i
    for l in range(pos2-1,9):
        a[l-1]=a[l]
    print(a)
        
    
    
