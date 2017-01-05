from sys import argv  #inport argv from moudle sys

script, file_name = argv  # give the numbers of paraemters of argv

txt = open(file_name) #open the ex15_example.txt and read the content to variable txt

print ("Here's your file %r:" % file_name) # print the string and filename
print (txt.read()) # print the content in txt ,read then print

print ("Type the filename again:") # print the string
file_again = input("> ") # input the fileanme again after the character > and give the filename to file_again

txt_again = open(file_again) # output the content of file to txt_again
print (txt_again.read()) #print the content of the file again

txt.close()
txt_again.close()
