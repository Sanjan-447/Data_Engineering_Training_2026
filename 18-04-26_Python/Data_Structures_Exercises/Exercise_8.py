sentence = "python is easy and python is powerful"
sen=sentence.split()
count={}

for word in sen:
    if word in count:
        count[word]+=1
    else:
        count[word]=1

print(count)