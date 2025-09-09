l1 = list(map(int,input("\nEnter the elements of first list: ").split()))
l2 = list(map(int,input("Enter the elements of second list: ").split()))

l3 = []
for i in l1:
    l3.append(i)
for i in l2:
    if i not in l1:
        l3.append(i)

l4 = []
for k in l1:
    if k in l2:
        l4.append(k)

print(f"\nThe union of the two lists are: {l3}")
print(f"\nThe intersection of the two lists are: {l4}\n")