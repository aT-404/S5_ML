import matplotlib.pyplot as plt
import csv
from collections import Counter

with open('exp2/sentence.csv','r') as f:
    reader = csv.reader(f)
    sent = ''
    for row in reader:
        sent+=''.join(row)
    
char_freq = Counter(sent)

plt.bar(char_freq.keys(),char_freq.values())
plt.title("Charecter Frequency")
plt.xlabel("Charecters")
plt.ylabel("Frequencies")
plt.show()