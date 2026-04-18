# with open("data.txt","w") as file:
#     file.write("These are the students.\n")
#     file.write("To be expelled.\n")
#     file.write("From school.\n")

languages=["Python\n","Java\n","C++\n"]
with open("data_1.txt", "w") as file:
    file.writelines(languages)
