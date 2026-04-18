import csv

data=[["name","marks"],
["Rahul",85],
["Sneha",92]]

with open("output.csv", "w",newline="") as file:
    writer=csv.writer(file)

    writer.writerows(data)