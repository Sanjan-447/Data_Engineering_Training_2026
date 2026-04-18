emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]

domains=[]
for i in emails:
    domains.append(i[6:])
print(domains)

count={}
for dom in domains:
    if  dom in count:
        count[dom]+=1
    else:
        count[dom]=1
print(count)
