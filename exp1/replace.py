sent=input("Enter a sentence: ")

while True:
    str1=input("Enter the string to be replaced: ")

    flag=0
    l=sent.split()
    for i in l:
        if i==str1:
            flag=1

    if flag==0:
        print("It does not exist!!")
    else:
        break


str2=input("Enter the new string: ")

n_sent=sent.replace(str1,str2)
print("\nOld sentence is:",sent)
print("\nNew sentence is:",n_sent)