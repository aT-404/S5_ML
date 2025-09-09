text = open("exp6/textfile.txt").read().lower()
text = text.strip('&*#@!.,/?+-_=')

words = text.split()

print()
done = []
max=0
for i in words:
    if i not in done:
        done.append(i)
    else:
        continue
    c = 0
    for j in words:
        if i == j:
            c+=1
    if c > max:
        max = c
        word = i

print(f"The most frequent word in the text file is {word}\n")