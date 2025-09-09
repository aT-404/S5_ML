a=int(input("Enter the starting value: "))
b=int(input("Enter the last value: "))
 
odd_sum=0
even_sum=0

for i in range(a,b+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i

print("\nThe sum of odd numbers is:",odd_sum,"\nThe sum of even numbers is:",even_sum)
