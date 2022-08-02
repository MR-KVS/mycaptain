list1 = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    list1.append(item)
print("User list is ", list1)
list2=[]
for x in list1:
    if x>0:
        list2.append(x)
print ("The possitive numbers are",list2)
