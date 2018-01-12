# get a filename using argv
from sys import argv
# unpack argv
script, filename = argv
# set the txt variable with the file
txt = open(filename)
# print a message with the filename
print(f"Here's your file {filename}:")
# read and print the file content 
print(txt.read())
# # print a message
# print("Type the filename again:")
# # get a filename using input
# file_again = input(">")
# # set the txt_again with the file 
# txt_again = open(file_again)
# # read and print the file content
# print(txt_again.read())