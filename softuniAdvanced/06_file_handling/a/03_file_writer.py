# Create a program that creates a file called my_first_file.txt.
# In that file, write a single line with the content: 'I just created my first file!'

file = open("txt_files/creating_file.txt", "w")

file.write(input())

file = open("txt_files/creating_file.txt")

print(file.read())
