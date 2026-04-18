numbers = [10,20,10,30,20,10,40]

count_dict={}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)
