sent = input("Enter the sentence: ")
sent = sent.strip('.,/?+-_=')
words = sent.lower().split()

print()
done = []
for i in words:
    if i not in done:
        done.append(i)
    else:
        continue
    c = 0
    for j in words:
        if i == j:
            c+=1

    print(f"The count of '{i}' is {c}")